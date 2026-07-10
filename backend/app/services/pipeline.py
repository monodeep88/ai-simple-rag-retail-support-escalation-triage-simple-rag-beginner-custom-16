from app.config import CHROMA_DIR, DATA_DIR, PROJECT_TYPE
from app.domain import BUSINESS_RULES, DOMAIN_SUMMARY, TOOL_CATALOG, WORKFLOW_STEPS
from app.schemas import AskResponse, Source, TimelineStep
from app.services.llm import get_answer_model
from app.services.text import chunk_documents, load_documents
from app.services.tools import calculate, planning_checklist, summarize_csv
from app.services.vector_store import build_vector_index


FLOW_STYLE = 'Simple RAG'


def _step(name: str, detail: str, status: str = "completed") -> TimelineStep:
    return TimelineStep(step=name, status=status, detail=detail)


def _tool_call(question: str) -> str:
    lowered = question.lower()
    if "calculate:" in lowered:
        return "Calculator result: " + calculate(question.split(":", 1)[1].strip())
    if "csv:" in lowered:
        return "CSV analysis: " + summarize_csv(question.split(":", 1)[1])
    domain_tools = ", ".join(f"{tool['name']}: {tool['description']}" for tool in TOOL_CATALOG[:3])
    return "Checklist: " + " | ".join(planning_checklist(question)[:3]) + f" | Available domain tools: {domain_tools}"


def run_pipeline(question: str) -> AskResponse:
    steps: list[TimelineStep] = []
    documents = load_documents(DATA_DIR)
    steps.append(_step("document_loader", f"Loaded {len(documents)} sample documents."))

    chunks = chunk_documents(documents)
    steps.append(_step("text_splitter", f"Created {len(chunks)} searchable chunks."))

    index = build_vector_index(chunks, CHROMA_DIR)
    steps.append(_step("embedding_and_vector_store", "Indexed chunks with ChromaDB when available, otherwise local embeddings."))

    plan = planning_checklist(question)
    if FLOW_STYLE in {"Agentic RAG", "AI Agent", "Multi-Agent AI", "CrewAI multi-agent", "Pinecone RAG", "LangGraph workflow", "LangChain tool-calling agent"}:
        steps.append(_step("planner", " -> ".join(plan[:3])))
    steps.append(_step("domain_profile", DOMAIN_SUMMARY))
    for rule_number, rule in enumerate(BUSINESS_RULES[:3], start=1):
        steps.append(_step(f"business_rule_{rule_number}", rule))

    results = index.similarity_search(question, k=4)
    steps.append(_step("retriever", f"Retrieved {len(results)} relevant chunks."))
    for workflow_number, workflow_step in enumerate(WORKFLOW_STEPS[:4], start=1):
        steps.append(_step(f"domain_workflow_{workflow_number}", workflow_step))

    if FLOW_STYLE == "Multi-Agent AI":
        steps.append(_step("researcher_agent", "Collected evidence from retrieved documents."))
        steps.append(_step("analyst_agent", "Compared evidence with the user question."))
        steps.append(_step("reviewer_agent", "Checked citations and final answer quality."))
    elif FLOW_STYLE == "CrewAI multi-agent":
        from app.services.crew import run_crewai_crew

        crew_result = run_crewai_crew(question, [item.text for item in results], TOOL_CATALOG)
        for crew_step in crew_result["steps"]:
            steps.append(_step(crew_step["step"], crew_step["detail"]))
        steps.append(_step("crewai_process", f"Runtime: {crew_result['runtime']}. CrewAI uses Agent, Task, Crew, and Process.sequential when enabled."))
    elif FLOW_STYLE == "Pinecone RAG":
        from app.services.pinecone_store import run_pinecone_search

        pinecone_result = run_pinecone_search(question, [item.text for item in results])
        for pinecone_step in pinecone_result["steps"]:
            steps.append(_step(pinecone_step["step"], pinecone_step["detail"]))
        steps.append(_step("pinecone_runtime", f"Runtime: {pinecone_result['runtime']}. Pinecone client is used when PINECONE_API_KEY and PINECONE_INDEX_NAME are configured."))
    elif FLOW_STYLE == "LangGraph workflow":
        from app.services.graph import run_langgraph_workflow

        graph_result = run_langgraph_workflow(question, [item.text for item in results])
        for graph_step in graph_result["steps"]:
            steps.append(_step(graph_step["step"], graph_step["detail"]))
        steps.append(_step("langgraph_runtime", f"Runtime: {graph_result['runtime']}. StateGraph orchestration is used when available."))
    elif FLOW_STYLE == "LangChain tool-calling agent":
        from app.services.langchain_tools import run_langchain_tool_call

        tool_result = run_langchain_tool_call(question)
        for tool_step in tool_result["steps"]:
            steps.append(_step(tool_step["step"], tool_step["detail"]))
        steps.append(_step("langchain_tool_runtime", f"Runtime: {tool_result['runtime']}."))
    elif FLOW_STYLE in {"Agentic RAG", "AI Agent"}:
        steps.append(_step("reasoning", "Reasoned over retrieved context and plan."))
        steps.append(_step("tool_call", _tool_call(question)))

    reasoning = " ".join(step.detail for step in steps[-3:])
    if FLOW_STYLE == "CrewAI multi-agent":
        answer = crew_result["answer"]
    elif FLOW_STYLE == "LangGraph workflow":
        answer = graph_result["answer"]
    elif FLOW_STYLE == "Pinecone RAG":
        pinecone_context = " ".join(pinecone_result["matches"][:2]) or "No Pinecone matches were available."
        answer = get_answer_model().invoke(question, results, reasoning + " Pinecone matches: " + pinecone_context)
    elif FLOW_STYLE == "LangChain tool-calling agent":
        answer = get_answer_model().invoke(question, results, reasoning + " Tool output: " + tool_result["output"])
    else:
        answer = get_answer_model().invoke(question, results, reasoning)
    steps.append(_step("final_answer", "Generated answer with source citations."))

    return AskResponse(
        answer=answer,
        sources=[Source(title=item.title, snippet=item.text[:240], score=item.score) for item in results],
        steps=steps,
        project_type=PROJECT_TYPE,
    )
