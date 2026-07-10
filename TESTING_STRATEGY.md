# Testing Strategy

## Unit Tests

Test text splitting, tool helpers, domain configuration, and schema validation.

## Integration Tests

Test `POST /api/ask` returns answer, sources, steps, and project type.

## AI/RAG Tests

Verify retrieval returns relevant source chunks and fallback mode works without provider keys.

## Agent Workflow Tests

Validate timeline steps for Simple RAG and ensure project-type markers exist in generated code.

## Security Tests

Test oversized input rejection, secret-safe logs, CORS settings, and no provider keys in frontend files.

## Database Tests

Test run logs are saved and recent runs are returned in the expected order.

## Frontend Tests

Run `npm run build` and manually verify answer, source, and timeline rendering.

## Docker Validation

Run `docker compose config` and `docker compose build`.

## Suggested CI Pipeline

1. Install backend dependencies.
2. Run `pytest`.
3. Install frontend dependencies.
4. Run `npm run build`.
5. Run Docker Compose config/build validation.
