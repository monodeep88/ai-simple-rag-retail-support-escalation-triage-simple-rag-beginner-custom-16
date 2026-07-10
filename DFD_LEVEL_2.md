# DFD Level 2

  ```mermaid
  flowchart TB
P3A((3.1 Build Prompt Context)) -->|prompt package| P3B((3.2 Execute Simple RAG))
P3B -->|draft answer| P3C((3.3 Validate Grounding))
P3C -->|needs fallback| P3D((3.4 Use Local Fallback))
P3C -->|approved answer| P3E((3.5 Create Timeline))
P3D --> P3E
P3E -->|run record| D2[(Run Log Store)]
D1[(Source Document Store)] -->|retrieved evidence| P3A
PROVIDER[Optional LLM Provider] -->|model response| P3B
  ```

  ## Explanation

  Level 2 decomposes the most important process: RAG Query Processing. It separates prompt/context preparation, execution, grounding validation, fallback, and timeline persistence.

  ## DFD Rules Used

  - External entities are outside the system boundary.
  - Processes use action-oriented names.
  - Data stores use noun names and are drawn separately from processes.
  - This DFD shows data movement, not deployment infrastructure.
