# Interview Guide

## How To Explain The Project

This is a Beginner **Simple RAG** project for **Retail Support Escalation Triage Simple RAG - Beginner Custom 16**. It demonstrates a React user interface, FastAPI backend, retrieval/workflow pipeline, stored run history, Docker setup, and tests.

## System Design Explanation

Start with the user request, then explain validation, retrieval/context, orchestration, final answer formatting, and run logging.

## Database Explanation

The core table is `run_logs`; supporting tables track source documents, retrieved chunks, and timeline steps so outputs are explainable.

## RAG/AI Explanation

User question -> load documents -> split chunks -> embed -> Chroma similarity search -> answer with citations.

## Suggested Questions And Answers

### Why is this architecture suitable?

It separates UI, API, workflow, retrieval, persistence, and deployment concerns while remaining runnable as a portfolio project.

### How does the DFD differ from the architecture diagram?

DFDs show data movement between processes, stores, and external entities. Architecture diagrams show runtime components and deployment responsibilities.

### How would you secure it for production?

Add authentication, per-user authorization, rate limits, secret management, safe logging, prompt-injection defenses, and tenant-aware retrieval filters.

### How would you scale it?

Move long jobs to a queue, use PostgreSQL, use managed vector DB, add caching, run multiple API workers, and monitor latency/error/token metrics.
