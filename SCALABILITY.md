# Scalability Design

## Current MVP Architecture

The MVP is a single FastAPI service, React frontend, SQL database, and local/vector retrieval layer.

## Bottlenecks

- Long LLM calls block request threads.
- Local vector storage does not scale to many tenants.
- SQLite is local-demo only.
- Repeated prompts can waste provider tokens.

## Scaling Plan

- Frontend: serve static assets through CDN.
- FastAPI: run multiple workers behind a load balancer.
- Database: use PostgreSQL, indexes, read replicas when needed.
- Vector DB: move large datasets to managed Chroma/Pinecone.
- Background jobs: offload indexing and long agent runs to Redis/Celery/RQ.
- Caching: cache retrieval results and repeated answer drafts where safe.
- Multi-tenancy: add tenant IDs to documents, chunks, and run logs.
- Monitoring: track latency, error rate, token usage, retrieval count, and fallback rate.
