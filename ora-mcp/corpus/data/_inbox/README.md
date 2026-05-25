# _inbox/ — staging area for new CSV exports

Drop ISTAT / OECD / Eurostat / etc. CSV exports here. The ingestion pipeline
(`memory/scripts/autonomous_data_pipeline_prompt.md`) consumes from this folder,
routes each file to `_raw/<topic-folder>/<DATASET_CODE>/`, and clears the inbox.

Never commit raw files here — they belong in `_raw/<topic>/...` after processing.
