# DFD Level 1

  ```mermaid
  flowchart LR
USER[External User] -->|question| P1((1.0 Validate Request))
P1 -->|valid task| P2((2.0 Retrieve Context))
P2 -->|chunks| P3((3.0 Run Simple RAG))
P3 -->|timeline and answer| P4((4.0 Format Response))
P4 -->|answer with sources| USER
P2 -->|read chunks| D1[(Source Document Store)]
P3 -->|write run| D2[(Run Log Store)]
P4 -->|read run metadata| D2
  ```

  ## Explanation

  Level 1 decomposes the system into validation, retrieval, workflow execution, and response formatting. Data stores are nouns and processes are actions.

  ## DFD Rules Used

  - External entities are outside the system boundary.
  - Processes use action-oriented names.
  - Data stores use noun names and are drawn separately from processes.
  - This DFD shows data movement, not deployment infrastructure.
