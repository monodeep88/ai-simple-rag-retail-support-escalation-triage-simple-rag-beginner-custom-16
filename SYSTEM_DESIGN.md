# System Design

## Problem Statement

Build **Retail Support Escalation Triage RAG Assistant**, a Beginner Simple RAG application for **Retail Support Escalation Triage Simple RAG - Beginner Custom 16** that turns a user question into an explainable answer with citations, timeline steps, and stored run history.

## Target Users

- Students building portfolio proof
- Developers learning production AI workflows
- Recruiters or interviewers reviewing implementation quality

## Functional Requirements

- Accept a user question or task from the React UI.
- Validate request shape and reject empty input.
- Execute the Simple RAG workflow with observable timeline steps.
- Return answer, cited sources, timeline, and project metadata.
- Persist each run for debugging, demos, and interview explanation.

## Non-Functional Requirements

- Keep local deterministic fallback behavior so the repo runs without paid API keys.
- Avoid logging secrets or raw provider credentials.
- Keep API responses stable enough for frontend and tests.
- Support Docker-based local deployment and PostgreSQL production storage.
- Keep generated documentation accurate enough for portfolio review.

## Main Entities

- RunLog
- SourceDocument
- RetrievedChunk
- TimelineStep
- EmbeddingRecord
- VectorCollection

## Main Workflows

- 1. Customer Issue: A customer presents an issue or asks a question to a support agent.
- 2. Agent Input: The support agent types a summary of the customer's issue into the RAG assistant's input field.
- 3. Query Submission: The agent clicks 'Submit' or presses Enter.
- 4. Backend Processing:
-    a. The backend receives the query.
-    b. The query is embedded into a vector.
-    c. The vector database is queried to find the most relevant internal knowledge documents.
-    d. The retrieved documents, along with the original query, are formatted into a prompt for the LLM.

## High-Level Architecture

React handles the user workspace. FastAPI validates requests and calls the pipeline service. The pipeline retrieves local or vector context, applies the Simple RAG orchestration strategy, calls an optional LLM provider when configured, and stores the run in SQL.

## API Boundaries

- `POST /api/ask`: synchronous user-facing workflow execution.
- `GET /api/runs`: read-only run history for demos and debugging.
- `GET /api/health`: operational health check.

## Data Storage Strategy

SQLite keeps the generated demo easy to run. Docker Compose uses PostgreSQL-ready connection settings for production. Run logs and timeline evidence are separate from source documents to avoid mixing user output with reference content.

## Vector Database Strategy

The project retrieves chunks from ChromaDB/local vector fallback and can move to Pinecone or managed Chroma for larger datasets.

## Agent Orchestration Strategy

The main flow is service-oriented rather than multi-agent, keeping the control path simple for this project type.

## Background Jobs

MVP execution is synchronous for simplicity. Production should move long LLM/tool calls, indexing, and GitHub operations to Celery/RQ/Redis or a managed queue.

## Authentication And Authorization

The generated repo is a portfolio demo. Add JWT/session authentication, user ownership checks, and admin-only routes before storing private user data.

## Error Handling

Validate input, return friendly API errors, use deterministic fallback answers when LLM keys are absent, and store enough timeline information to debug failures.

## Logging And Monitoring

Log request IDs, latency, provider mode, validation failures, and retrieval count. Do not log API keys, prompts containing secrets, or raw private documents.

## Security Considerations

Keep secrets in environment variables, restrict CORS, validate inputs, avoid unsafe code execution, and add rate limiting before production exposure.

## Scaling Plan

MVP documentation with simple flows, 3-5 core entities, and clear local setup.

## Deployment Plan

Use Docker Compose locally. For production, deploy FastAPI behind a managed HTTPS platform, React as static assets, PostgreSQL as managed storage, and vector DB as a managed service when data grows.

## Future Improvements

- Add authentication and user-owned run logs.
- Add background indexing and queue-backed execution.
- Add observability dashboards.
- Add richer dataset upload and review workflow.
