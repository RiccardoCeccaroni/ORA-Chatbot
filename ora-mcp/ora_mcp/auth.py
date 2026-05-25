"""Permissive OAuth 2.1 authorization server provider for the ORA! MCP.

This module exists ONLY to satisfy claude.ai's connector handshake requirement
that remote MCP servers expose OAuth endpoints. The implementation is
deliberately *permissive*: anyone can register a client, anyone can complete
the authorize -> token exchange, no human approval is involved.

Why this is acceptable for ORA: the data exposed by the MCP is the party's
PUBLIC corpus (manifesto, leader views, ISTAT figures). There is no
confidential information to protect. The OAuth layer is pure protocol
satisfaction -- same effective access as the no-auth sibling project (D09),
but wrapped in OAuth so claude.ai's connector flow accepts it.

NOTE on durability: All state lives in process memory. A Fly machine restart
wipes the client/code/token stores, which means existing users would need to
re-authorize (claude.ai typically does this transparently). Acceptable for
demo traffic; swap for a persistent store (SQLite, Redis) if you outgrow it.
"""

from __future__ import annotations

import secrets
import time

from mcp.server.auth.provider import (
    AccessToken,
    AuthorizationCode,
    AuthorizationParams,
    OAuthAuthorizationServerProvider,
    RefreshToken,
    construct_redirect_uri,
)
from mcp.shared.auth import OAuthClientInformationFull, OAuthToken


_AUTH_CODE_TTL_SECONDS = 600                   # 10 minutes -- long enough for the round-trip
_ACCESS_TOKEN_TTL_SECONDS = 60 * 60 * 24 * 365 # 1 year -- effectively long-lived for demo


class PermissiveOAuthProvider(
    OAuthAuthorizationServerProvider[AuthorizationCode, RefreshToken, AccessToken]
):
    """OAuth provider that approves everything, validates almost nothing.

    Implements the full MCP `OAuthAuthorizationServerProvider` protocol so
    `FastMCP` will auto-register all the standard OAuth endpoints
    (`/authorize`, `/token`, `/register`, `/.well-known/*`). See module
    docstring for rationale on the permissive design.
    """

    def __init__(self) -> None:
        self._clients: dict[str, OAuthClientInformationFull] = {}
        self._auth_codes: dict[str, AuthorizationCode] = {}
        self._access_tokens: dict[str, AccessToken] = {}
        self._refresh_tokens: dict[str, RefreshToken] = {}

    # ----------------------------------------------------------------------
    # client registration (Dynamic Client Registration, RFC 7591)
    # ----------------------------------------------------------------------

    async def get_client(self, client_id: str) -> OAuthClientInformationFull | None:
        return self._clients.get(client_id)

    async def register_client(self, client_info: OAuthClientInformationFull) -> None:
        # No validation -- accept whatever client metadata the caller sends.
        # The SDK's /register handler has already generated client_id/secret
        # by this point.
        self._clients[client_info.client_id] = client_info

    # ----------------------------------------------------------------------
    # authorization code flow
    # ----------------------------------------------------------------------

    async def authorize(
        self, client: OAuthClientInformationFull, params: AuthorizationParams
    ) -> str:
        """Auto-approve: mint an auth code and redirect back to the client.

        No user consent UI -- we trust the client's redirect_uri (it was
        validated at registration time by the SDK handler).
        """
        code = secrets.token_urlsafe(32)  # ~256 bits of entropy
        self._auth_codes[code] = AuthorizationCode(
            code=code,
            scopes=params.scopes or [],
            expires_at=time.time() + _AUTH_CODE_TTL_SECONDS,
            client_id=client.client_id,
            code_challenge=params.code_challenge,
            redirect_uri=params.redirect_uri,
            redirect_uri_provided_explicitly=params.redirect_uri_provided_explicitly,
            resource=params.resource,
        )
        return construct_redirect_uri(
            str(params.redirect_uri),
            code=code,
            state=params.state,
        )

    async def load_authorization_code(
        self, client: OAuthClientInformationFull, authorization_code: str
    ) -> AuthorizationCode | None:
        code = self._auth_codes.get(authorization_code)
        if code is None or code.client_id != client.client_id:
            return None
        if code.expires_at < time.time():
            self._auth_codes.pop(authorization_code, None)
            return None
        return code

    async def exchange_authorization_code(
        self,
        client: OAuthClientInformationFull,
        authorization_code: AuthorizationCode,
    ) -> OAuthToken:
        # Single-use: drop the code now (the SDK handler has already validated PKCE).
        self._auth_codes.pop(authorization_code.code, None)
        return self._issue_token_pair(
            client_id=client.client_id,
            scopes=authorization_code.scopes,
            resource=authorization_code.resource,
        )

    # ----------------------------------------------------------------------
    # refresh token flow
    # ----------------------------------------------------------------------

    async def load_refresh_token(
        self, client: OAuthClientInformationFull, refresh_token: str
    ) -> RefreshToken | None:
        token = self._refresh_tokens.get(refresh_token)
        if token is None or token.client_id != client.client_id:
            return None
        return token

    async def exchange_refresh_token(
        self,
        client: OAuthClientInformationFull,
        refresh_token: RefreshToken,
        scopes: list[str],
    ) -> OAuthToken:
        # Rotate: drop the old refresh token, issue a fresh pair.
        self._refresh_tokens.pop(refresh_token.token, None)
        effective_scopes = scopes or refresh_token.scopes
        return self._issue_token_pair(
            client_id=client.client_id,
            scopes=effective_scopes,
            resource=None,
        )

    # ----------------------------------------------------------------------
    # access token validation (called on every MCP request)
    # ----------------------------------------------------------------------

    async def load_access_token(self, token: str) -> AccessToken | None:
        access = self._access_tokens.get(token)
        if access is None:
            return None
        if access.expires_at is not None and access.expires_at < int(time.time()):
            self._access_tokens.pop(token, None)
            return None
        return access

    # ----------------------------------------------------------------------
    # revocation
    # ----------------------------------------------------------------------

    async def revoke_token(self, token: AccessToken | RefreshToken) -> None:
        self._access_tokens.pop(token.token, None)
        self._refresh_tokens.pop(token.token, None)

    # ----------------------------------------------------------------------
    # internal: mint a fresh access + refresh token pair
    # ----------------------------------------------------------------------

    def _issue_token_pair(
        self,
        *,
        client_id: str,
        scopes: list[str],
        resource: str | None,
    ) -> OAuthToken:
        access_str = secrets.token_urlsafe(32)
        refresh_str = secrets.token_urlsafe(32)
        expires_at = int(time.time() + _ACCESS_TOKEN_TTL_SECONDS)

        self._access_tokens[access_str] = AccessToken(
            token=access_str,
            client_id=client_id,
            scopes=scopes,
            expires_at=expires_at,
            resource=resource,
        )
        self._refresh_tokens[refresh_str] = RefreshToken(
            token=refresh_str,
            client_id=client_id,
            scopes=scopes,
            expires_at=None,  # refresh tokens don't expire in this demo provider
        )
        return OAuthToken(
            access_token=access_str,
            token_type="Bearer",
            expires_in=_ACCESS_TOKEN_TTL_SECONDS,
            refresh_token=refresh_str,
            scope=" ".join(scopes) if scopes else None,
        )
