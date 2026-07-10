# DFD Level 0

  ```mermaid
  flowchart LR
USER[External User] -->|question or task| P0((Retail Support Escalation Triage RAG Assistant))
P0 -->|answer with sources| USER
P0 -->|run history| STORE[(Run Log Store)]
P0 -->|retrieval request| DOCS[Source Documents]
  ```

  ## Explanation

  Level 0 keeps the whole application as one process. It shows only the external user, the generated system, reference documents, and durable run history.

  ## DFD Rules Used

  - External entities are outside the system boundary.
  - Processes use action-oriented names.
  - Data stores use noun names and are drawn separately from processes.
  - This DFD shows data movement, not deployment infrastructure.
