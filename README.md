# Agentic RAG with Persistent Memory

This project implements a retrieval-augmented LLM agent that maintains persistent memory across conversations.

## Architecture
User Query → Embedding → FAISS Vector Store → Relevant Memory → LLM → Response → Memory Update

## Features
- Embedding-based retrieval
- Long-term memory store
- Context-aware responses
- Continual personalization

## Run
```bash
python agent.py
