# Security Design

## Threat Model

Main risks are prompt injection, unsafe user input, leaked API keys, excessive API usage, poisoned RAG content, and accidental logging of private data.

## Controls

- Authentication: add JWT/session auth before storing private user data.
- Authorization: enforce user ownership for run logs and uploaded sources.
- Input validation: reject empty or oversized requests.
- Secret management: use `.env` locally and deployment secret manager in production.
- API key handling: never return provider keys to the frontend.
- Prompt injection: separate system instructions from retrieved text and cite sources.
- RAG data leakage: filter private documents by user/tenant before retrieval.
- File upload risks: scan files, restrict MIME types, and avoid executing uploaded code.
- Rate limiting: throttle `/api/ask` and login endpoints.
- CORS: allow only known frontend origins.
- Logging: record request IDs and statuses, not secrets.
