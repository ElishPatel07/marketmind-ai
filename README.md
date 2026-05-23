# MarketMind AI

Production grade Financial Market Intelligence Agent built with FastAPI, NLP pipelines, RAG architecture, vector search, Docker infrastructure, and MLOps engineering practices.

---

## Overview

MarketMind AI is an end to end AI powered financial intelligence platform designed to aggregate, process, analyze, retrieve, and summarize financial information from multiple data sources.

The system combines:
- Financial news ingestion
- Market data pipelines
- NLP sentiment analysis
- Retrieval Augmented Generation (RAG)
- Semantic vector search
- AI powered market research
- Production grade backend engineering
- Containerized infrastructure

The goal is to simulate a real world AI platform similar to internal fintech research systems used by hedge funds, trading firms, and financial startups.

---

## Goals

- Build a scalable AI financial intelligence platform
- Practice production grade ML engineering
- Implement real world backend architecture
- Learn MLOps and infrastructure engineering
- Demonstrate industry style software engineering practices
- Build a portfolio project suitable for ML Engineer and AI Engineer interviews

---

## Tech Stack

| Category | Tools |
|---|---|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.0 |
| Database Migrations | Alembic |
| Async DB Driver | asyncpg |
| Cache | Redis |
| Vector Database | ChromaDB |
| NLP | Transformers, Sentence Transformers |
| LLM | Ollama, Groq |
| Infrastructure | Docker, Docker Compose |
| MLOps | MLflow |
| Monitoring | Prometheus, Grafana |
| Logging | Loguru |
| Testing | Pytest |
| Linting | Ruff |
| Configuration | Pydantic Settings |
| CI/CD | GitHub Actions |

---

## Current Project Status

### Completed

#### Phase 1A
- Project planning
- System architecture design
- Repository initialization
- FastAPI backend foundation
- Initial engineering setup

#### Phase 1B Part 1
- Environment configuration
- Typed settings management
- Structured logging
- Centralized config architecture

#### Phase 1B Part 2
- Ruff linting and formatting
- Pytest setup
- Pre-commit hooks
- Makefile automation
- API router structure
- Health check endpoint

#### Phase 1C
- Docker Compose infrastructure
- PostgreSQL container
- Redis container
- Persistent Docker volumes
- Environment driven container setup
- Infrastructure health checks
- Local infrastructure orchestration

#### Phase 1D
- Async PostgreSQL integration
- SQLAlchemy ORM setup
- Alembic migration system
- Async database sessions
- Database dependency injection
- Initial financial news schema
- Database connectivity health checks

#### Phase 1E Part 1
- Pydantic schema architecture
- Request validation models
- Response serialization models
- API data contracts
- Schema based validation pipelines

#### Phase 1E Part 2
- Repository pattern architecture
- Async CRUD repository layer
- Reusable database access abstraction
- SQLAlchemy async query layer
- Centralized persistence logic

#### Phase 1E Part 3
- Service layer architecture
- Business workflow abstraction
- Repository orchestration layer
- Layered backend architecture
- Service based API flow

---

## Architecture

```text
                           Frontend Dashboard
                                   │
                                   ▼
                            FastAPI Gateway
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
   RAG Service               NLP Service            Ingestion Service
        │                          │                          │
        ▼                          ▼                          ▼
   ChromaDB                  PostgreSQL                  Redis
        │
        ▼
   Embedding Pipelines