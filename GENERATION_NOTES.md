# Generation Notes

Mode: ai

Model: gemini / gemini-2.5-flash

Fallback reason: OpenAI limit reached. Automatically switched to Gemini.

Architecture: Customer Support KB Search

Template path: templates/simple-rag/customer-support-kb-search

Short description:

A beginner-friendly Retrieval-Augmented Generation (RAG) assistant designed to help retail support agents quickly triage customer issues, recommending appropriate escalation paths (e.g., IT, Manager, General Support) based on internal knowledge documents.

Architecture notes:

- This architecture emphasizes simplicity suitable for beginners. FastAPI is chosen for its ease of use and modern Python capabilities. React provides a responsive single-page application experience. The RAG core uses common components: an open-source embedding model (e.g., `sentence-transformers/all-MiniLM-L6-v2`), a lightweight vector database like ChromaDB (can be run in-memory or file-based), and an open-source LLM (e.g., a quantized Llama 3 or Gemma) for local execution to keep costs down and simplify deployment. No complex microservices or cloud infrastructure are strictly required for the core functionality, making it easy to run locally. The focus is on demonstrating the core RAG pattern: retrieve relevant information, then generate an informed answer.

Project planner agent workflow:

- Architecture Agent: Define app boundaries, data flow, runtime stack, and integration points. Outputs: This architecture emphasizes simplicity suitable for beginners. FastAPI is chosen for its ease of use and modern Python capabilities. React provides a responsive single-page application experience. The RAG core uses common components: an open-source embedding model (e.g., `sentence-transformers/all-MiniLM-L6-v2`), a lightweight vector database like ChromaDB (can be run in-memory or file-based), and an open-source LLM (e.g., a quantized Llama 3 or Gemma) for local execution to keep costs down and simplify deployment. No complex microservices or cloud infrastructure are strictly required for the core functionality, making it easy to run locally. The focus is on demonstrating the core RAG pattern: retrieve relevant information, then generate an informed answer.
- Backend Agent: Design FastAPI modules, service contracts, validation, and error handling. Outputs: RAG Service: Handles the core RAG logic: embedding incoming queries, searching the vector database for relevant documents, and passing context to the LLM for response generation.; Document Management Service (Basic): Provides endpoints to (re)index documents into the vector database. For a beginner project, this might be a simple POST endpoint that triggers re-embedding all documents.
- Frontend Agent: Design React screens, state flow, controls, and user feedback states. Outputs: Query Input Field: A text area for the support agent to type the customer's issue or question.; Submit Button: Triggers the RAG process by sending the query to the backend.; Escalation Recommendation Display: Clearly shows the recommended escalation path (e.g., 'Escalate to IT Support') and a concise reason.; Relevant Documents Display: Lists the titles or snippets of the knowledge documents that were used to form the recommendation, providing transparency.; Loading Indicator: Provides visual feedback during backend processing.
- Database Agent: Design persistence models, sample data, indexes, and audit records. Outputs: Run history; Source document metadata; Generated workflow audit records
- Testing Agent: Define contract tests, smoke tests, and generated project validation. Outputs: {'type': 'Unit Tests', 'scope': 'Individual functions (e.g., embedding creation, vector search, prompt formatting, LLM invocation).', 'details': 'Ensure correct input/output for each component.'}; {'type': 'Integration Tests', 'scope': 'Backend API endpoints and the RAG chain components.', 'details': 'Verify that the /api/triage endpoint correctly processes a query, interacts with the vector DB and LLM, and returns a structured response. Use mock LLM responses for faster testing.'}; {'type': 'RAG Retrieval Quality Tests', 'scope': 'Vector database retrieval accuracy.', 'details': 'Provide specific queries and assert that the top-k retrieved documents contain expected relevant information. This ensures the embedding model and vector search are working as intended.'}; {'type': 'End-to-End Tests (Simple)', 'scope': 'Frontend to Backend interaction.', 'details': 'Simulate a user typing a query and clicking submit, then assert that the correct escalation path and documents are displayed on the UI. (Using tools like Playwright or Selenium, or simpler mock API calls for beginner scope).'}
- DevOps Agent: Define environment variables, Docker workflow, and repository packaging. Outputs: Docker-ready project; Environment sample file; GitHub repository upload
- Reviewer Agent: Review the generated plan for completeness, security, and portfolio quality. Outputs: 1. Customer Issue: A customer presents an issue or asks a question to a support agent.; 2. Agent Input: The support agent types a summary of the customer's issue into the RAG assistant's input field.; 3. Query Submission: The agent clicks 'Submit' or presses Enter.; 4. Backend Processing:;    a. The backend receives the query.;    b. The query is embedded into a vector.
