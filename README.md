# Retail Support Escalation Triage RAG Assistant

## Project Overview

Retail Support Escalation Triage RAG Assistant is a complete full-stack AI project for **Simple RAG** at **Beginner** difficulty. It includes a FastAPI backend, a React frontend, sample documents, vector search with ChromaDB support, source citations, timeline logs, structured run storage, Docker files, and tests.

Retail support often involves a high volume of diverse customer inquiries, ranging from simple product questions to complex technical issues or policy exceptions. Efficiently triaging these issues to the correct department or individual (e.g., IT, store manager, specific product team) is crucial for customer satisfaction and operational efficiency. This project addresses the challenge of providing instant, context-aware guidance to frontline agents to minimize misroutes and resolution times.

Difficulty controls project complexity, architecture depth, AI model selection, and how advanced the generated codebase is.

- Architecture depth: minimal backend, simple folder structure, easy README, low-cost/free model
- Selected architecture: Customer Support KB Search
- Template path: templates/simple-rag/customer-support-kb-search
- Generated stack: FastAPI backend, React UI, local vector fallback, simple tests
- README style: beginner-friendly setup and clear expected output

## Tech Stack

- Backend: Python, FastAPI, Pydantic, SQLAlchemy
- AI/RAG: LangChain-ready prompt layer, ChromaDB vector storage, local deterministic fallback model
- Workflow: Agent pipeline with planner, retrieval, tool, reasoning, and final answer steps
- Frontend: React and Vite
- Database: SQLite by default, PostgreSQL through Docker Compose
- Testing: pytest
- Difficulty: Beginner

## Generation Method

This project was generated with a template-based architecture engine. AI is used only for the blueprint, domain customization, sample data, prompts, and documentation. The codebase is produced from tested FastAPI/React/Docker templates rather than raw LLM source output.

## Why This Project Satisfies Simple RAG

This repository satisfies **Simple RAG** because it includes runnable implementation evidence, domain-specific workflow steps, validation gates, and portfolio documentation instead of only describing the idea.

## Project Type Satisfaction Map

This generated project satisfies **Simple RAG** through the runtime path below. The implementation is not only a README claim: the files listed after the diagram are generated in the repository and validated before GitHub push.

```text
[User]
  |
  | question / task details / tone / constraints
  v
[React Frontend]
  |
  | POST /api/ask
  v
[FastAPI Backend]
  |
  +--> [Vector Store / Sample Docs]
  |        |
  |        +-- retrieved context / cited sources
  |
  v
[Retriever]
  |
  v
[Citation Answer Builder]
  |
  v
[Final Answer Builder]
  |
  | answer + sources + timeline steps
  v
[React Frontend]
  |
  v
[User sees final output + agent timeline]
```

Runtime proof points:

- `frontend/src/App.jsx` renders the user workspace, starter prompts, answer panel, cited sources, and timeline.
- `backend/app/main.py` exposes `POST /api/ask` and returns the final answer, sources, timeline steps, and project type.
- `backend/app/services/pipeline.py` orchestrates the project-type flow: Retriever, Citation Answer Builder.
- `backend/app/services/vector_store.py` loads sample documents and retrieves relevant cited context.
- `backend/app/domain.py` contains the generated topic-specific workflow steps, business rules, tools, persona, and starter questions.
- `backend/app/db.py` stores each run so the generated app behaves like a real workflow tool instead of a static prompt demo.
- `backend/tests/test_project_contract.py` validates the API contract and project-type behavior.

Type-specific behavior:

- Flow style: User question -> load documents -> split chunks -> embed -> Chroma similarity search -> answer with citations.
- Visible output: final answer, cited sources, timeline steps, and project type.
- Validation gate: pytest, frontend build, Docker Compose config, and Docker build before repository upload.

## Folder Structure

```text
ai-simple-rag-retail-support-escalation-triage-simple-rag-beginner-custom-16/
  backend/
app/
  main.py
  config.py
  db.py
  schemas.py
  data/sample_docs/
  services/
text.py
vector_store.py
llm.py
tools.py
pipeline.py
tests/
  test_project_contract.py
requirements.txt
Dockerfile
  frontend/
src/
  App.jsx
  main.jsx
  styles.css
package.json
Dockerfile
  docker-compose.yml
  .env.example
  README.md
  ARCHITECTURE.md
  SYSTEM_DESIGN.md
  DATABASE_DESIGN.md
  API_DESIGN.md
  DFD_LEVEL_0.md
  DFD_LEVEL_1.md
  DFD_LEVEL_2.md
  ER_DIAGRAM.md
  SEQUENCE_DIAGRAMS.md
  SECURITY.md
  SCALABILITY.md
  TESTING_STRATEGY.md
  INTERVIEW_GUIDE.md
  WHY_THIS_PROJECT.md
  DEPLOYMENT.md
  docs/screenshots/app-preview.svg
```

## Environment Variables

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
USE_CREWAI_RUNTIME=false
PINECONE_API_KEY=
PINECONE_INDEX_NAME=
DATABASE_URL=sqlite:///./app.db
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
VITE_API_URL=http://localhost:8000
```

The app runs without an OpenAI key by using a deterministic local answer model. Add `OPENAI_API_KEY` to use LangChain with OpenAI. For CrewAI projects, set `USE_CREWAI_RUNTIME=true` after installing dependencies to run the live CrewAI Agent/Task/Crew workflow; otherwise the app uses a deterministic CrewAI-shaped fallback.

For Pinecone projects, add `PINECONE_API_KEY` and `PINECONE_INDEX_NAME` to use a live Pinecone index. Without them, the repo still runs using local ChromaDB/local retrieval fallback.

## Installation

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
cd ../frontend
npm install
```

## Run Backend

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

## Run Frontend

```bash
cd frontend
npm run dev
```

## Run With Docker

```bash
docker compose up --build
```

## Example API Request

```bash
curl -X POST http://localhost:8000/api/ask ^
  -H "Content-Type: application/json" ^
  -d "{\"question\": \"What is the refund policy?\"}"
```

## Example User Question

```text
What should I do if a customer asks for a refund without an order id?
```

## Expected Output

The API returns:

- `answer`: a grounded answer generated from retrieved context
- `sources`: cited document chunks with similarity scores
- `steps`: planner, retriever, reasoning, tool-call, and final-answer timeline logs
- `project_type`: `Simple RAG`

## How The RAG/Agent Flow Works

User question -> load documents -> split chunks -> embed -> Chroma similarity search -> answer with citations.

## Project Documentation

- [System Design](SYSTEM_DESIGN.md)
- [Architecture](ARCHITECTURE.md)
- [Database Design](DATABASE_DESIGN.md)
- [API Design](API_DESIGN.md)
- [DFD Level 0](DFD_LEVEL_0.md)
- [DFD Level 1](DFD_LEVEL_1.md)
- [DFD Level 2](DFD_LEVEL_2.md)
- [ER Diagram](ER_DIAGRAM.md)
- [Sequence Diagrams](SEQUENCE_DIAGRAMS.md)
- [Deployment](DEPLOYMENT.md)
- [Security](SECURITY.md)
- [Scalability](SCALABILITY.md)
- [Testing Strategy](TESTING_STRATEGY.md)
- [Interview Guide](INTERVIEW_GUIDE.md)

## Project Planner Agent Workflow

User -> React Dashboard -> FastAPI -> Project Planner Agent -> Specialist Agents -> Generated Project -> Auto Testing -> GitHub Repository Creation -> Push Code -> Return GitHub URL

- **Architecture Agent**: Define app boundaries, data flow, runtime stack, and integration points. Outputs: This architecture emphasizes simplicity suitable for beginners. FastAPI is chosen for its ease of use and modern Python capabilities. React provides a responsive single-page application experience. The RAG core uses common components: an open-source embedding model (e.g., `sentence-transformers/all-MiniLM-L6-v2`), a lightweight vector database like ChromaDB (can be run in-memory or file-based), and an open-source LLM (e.g., a quantized Llama 3 or Gemma) for local execution to keep costs down and simplify deployment. No complex microservices or cloud infrastructure are strictly required for the core functionality, making it easy to run locally. The focus is on demonstrating the core RAG pattern: retrieve relevant information, then generate an informed answer..
- **Backend Agent**: Design FastAPI modules, service contracts, validation, and error handling. Outputs: RAG Service: Handles the core RAG logic: embedding incoming queries, searching the vector database for relevant documents, and passing context to the LLM for response generation.; Document Management Service (Basic): Provides endpoints to (re)index documents into the vector database. For a beginner project, this might be a simple POST endpoint that triggers re-embedding all documents..
- **Frontend Agent**: Design React screens, state flow, controls, and user feedback states. Outputs: Query Input Field: A text area for the support agent to type the customer's issue or question.; Submit Button: Triggers the RAG process by sending the query to the backend.; Escalation Recommendation Display: Clearly shows the recommended escalation path (e.g., 'Escalate to IT Support') and a concise reason.; Relevant Documents Display: Lists the titles or snippets of the knowledge documents that were used to form the recommendation, providing transparency.; Loading Indicator: Provides visual feedback during backend processing..
- **Database Agent**: Design persistence models, sample data, indexes, and audit records. Outputs: Run history; Source document metadata; Generated workflow audit records.
- **Testing Agent**: Define contract tests, smoke tests, and generated project validation. Outputs: {'type': 'Unit Tests', 'scope': 'Individual functions (e.g., embedding creation, vector search, prompt formatting, LLM invocation).', 'details': 'Ensure correct input/output for each component.'}; {'type': 'Integration Tests', 'scope': 'Backend API endpoints and the RAG chain components.', 'details': 'Verify that the /api/triage endpoint correctly processes a query, interacts with the vector DB and LLM, and returns a structured response. Use mock LLM responses for faster testing.'}; {'type': 'RAG Retrieval Quality Tests', 'scope': 'Vector database retrieval accuracy.', 'details': 'Provide specific queries and assert that the top-k retrieved documents contain expected relevant information. This ensures the embedding model and vector search are working as intended.'}; {'type': 'End-to-End Tests (Simple)', 'scope': 'Frontend to Backend interaction.', 'details': 'Simulate a user typing a query and clicking submit, then assert that the correct escalation path and documents are displayed on the UI. (Using tools like Playwright or Selenium, or simpler mock API calls for beginner scope).'}.
- **DevOps Agent**: Define environment variables, Docker workflow, and repository packaging. Outputs: Docker-ready project; Environment sample file; GitHub repository upload.
- **Reviewer Agent**: Review the generated plan for completeness, security, and portfolio quality. Outputs: 1. Customer Issue: A customer presents an issue or asks a question to a support agent.; 2. Agent Input: The support agent types a summary of the customer's issue into the RAG assistant's input field.; 3. Query Submission: The agent clicks 'Submit' or presses Enter.; 4. Backend Processing:;    a. The backend receives the query.;    b. The query is embedded into a vector..

## AI-Customized Domain Workflow

- 1. Customer Issue: A customer presents an issue or asks a question to a support agent.
- 2. Agent Input: The support agent types a summary of the customer's issue into the RAG assistant's input field.
- 3. Query Submission: The agent clicks 'Submit' or presses Enter.
- 4. Backend Processing:
-    a. The backend receives the query.
-    b. The query is embedded into a vector.
-    c. The vector database is queried to find the most relevant internal knowledge documents.
-    d. The retrieved documents, along with the original query, are formatted into a prompt for the LLM.

## Business Rules

- If the customer's issue contains keywords like 'POS system', 'network error', 'scanner malfunction', 'printer not working', or 'software update', escalate to 'IT Support'.
- If the customer's issue mentions 'refund amount over $100', 'policy override', 'customer complaint about staff', 'special discount', or 'unusual return', escalate to 'Manager'.
- If the customer's issue relates to general product information, store hours, basic returns within policy, or stock availability, recommend 'General Support'.
- Always provide a brief, actionable reason for the recommended escalation path.
- Prioritize direct keyword matches for immediate escalation; otherwise, rely on semantic similarity from RAG.
- In cases of ambiguity (e.g., equally relevant IT and Manager documents), default to the most critical (e.g., Manager for customer satisfaction) or 'General Support' for further investigation.

1. The backend loads sample documents from `backend/app/data/sample_docs`.
2. Documents are split into chunks.
3. Chunks are embedded and stored in ChromaDB when available, with a local fallback for development.
4. User questions are matched against relevant chunks.
5. Agent-specific steps run: planner, retriever, tool call, reasoning, reviewer, or graph nodes.
6. The final answer is returned with source citations and a timeline.

## Testing

```bash
cd backend
pytest
```

## Validation Gates Before GitHub Push

The SaaS validates generated projects before creating and pushing the GitHub repository:

- `pytest`
- `npm install`
- `npm run build`
- `docker compose config`
- `docker compose build`

## Portfolio Proof Files

- `WHY_THIS_PROJECT.md`: explains why this repo satisfies the selected project type.
- `SYSTEM_DESIGN.md`, `ARCHITECTURE.md`, and DFD files: document the design, runtime flow, data movement, and validation strategy.
- `DATABASE_DESIGN.md`, `ER_DIAGRAM.md`, and `API_DESIGN.md`: connect generated code to data and API contracts.
- `SECURITY.md`, `SCALABILITY.md`, and `TESTING_STRATEGY.md`: explain production hardening and quality checks.
- `INTERVIEW_GUIDE.md`: helps students explain the project in interviews.
- `DEPLOYMENT.md`: gives Render, Railway, Vercel, and Docker deployment options.
- `docs/screenshots/app-preview.svg`: generated UI preview image for README/profile use.

## Deployment

See `DEPLOYMENT.md` for Render, Railway, Vercel, and Docker deployment steps.
