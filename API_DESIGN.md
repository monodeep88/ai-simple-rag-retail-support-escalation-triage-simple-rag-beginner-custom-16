# API Design

## Endpoint List

| Method | Path | Purpose | Auth |
| --- | --- | --- | --- |
| GET | `/api/health` | Health check for deployment and monitoring. | No auth in demo; add JWT for production |
| POST | `/api/ask` | Run the Simple RAG workflow for a user question. | No auth in demo; add JWT for production |
| GET | `/api/runs` | Return recent stored run logs for review and debugging. | No auth in demo; add JWT for production |

## POST /api/ask

Request body:

```json
{"question": "What should the user do next?"}
```

Response body:

```json
{
  "answer": "Grounded answer",
  "sources": [{"title": "Source", "snippet": "Evidence", "score": 0.82}],
  "steps": [{"name": "retriever", "status": "completed", "message": "Found context"}],
  "project_type": "Simple RAG"
}
```

## Error Responses

- `400`: invalid or empty request.
- `422`: schema validation failed.
- `500`: unexpected server error with friendly message.

## Rate Limiting Notes

Add IP/user-based throttling before public production use, especially for `POST /api/ask`.

## Example curl

```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Explain the main workflow."}'
```
