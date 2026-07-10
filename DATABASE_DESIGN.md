# Database Design

## Database Overview

The generated demo uses SQLite by default and is PostgreSQL-ready through `DATABASE_URL`. The schema focuses on storing explainable run history for **Retail Support Escalation Triage RAG Assistant**.

## Entity List

- RunLog
- SourceDocument
- RetrievedChunk
- TimelineStep
- EmbeddingRecord
- VectorCollection

## Table Definitions

### run_logs

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Primary key |
| question | text | User request |
| answer | text | Final generated or fallback answer |
| project_type | varchar | Generated project type |
| created_at | datetime | Indexed for recent history |

### source_documents

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Primary key |
| title | varchar | Document title |
| source_path | varchar | Local file or external source |
| content_hash | varchar | Deduplication key |

### retrieved_chunks

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Primary key |
| run_log_id | integer | Foreign key to run_logs.id |
| document_id | integer | Foreign key to source_documents.id |
| chunk_text | text | Evidence returned to the user |
| score | float | Similarity/relevance score |

### timeline_steps

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Primary key |
| run_log_id | integer | Foreign key to run_logs.id |
| step_name | varchar | Planner/retriever/tool/final answer stage |
| status | varchar | completed, fallback, failed |
| message | text | Safe debug message |

## Indexes

- `run_logs.created_at`
- `retrieved_chunks.run_log_id`
- `timeline_steps.run_log_id`
- `source_documents.content_hash`

## Constraints

- Run question and answer must not be empty.
- Retrieved chunks must reference a valid run.
- Timeline steps must reference a valid run.

## Example Queries

```sql
SELECT id, question, project_type, created_at
FROM run_logs
ORDER BY created_at DESC
LIMIT 10;
```

```sql
SELECT step_name, status, message
FROM timeline_steps
WHERE run_log_id = :run_id
ORDER BY id;
```

## Migration Notes

Start with SQLite for local demos. For production, create Alembic migrations and use PostgreSQL with explicit foreign keys and indexes.

## Data Retention And Privacy

Delete old run logs when they contain private prompts. Never store API keys or provider secrets in tables.
