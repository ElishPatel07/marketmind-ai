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

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root API endpoint |
| GET | `/health` | API and database connectivity health check |
| POST | `/news/` | Create financial news article |
| GET | `/news/{article_id}` | Retrieve article by ID |
| GET | `/news/` | List all financial news articles |

---

## Environment Configuration

The application uses typed environment based configuration.

Environment variables are validated through Pydantic settings.

### Supported Environments

- development
- staging
- production

### Configuration File

Create a `.env` file using:

```bash
cp .env.example .env
```
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

#### Phase 1E Part 4
- Production CRUD API architecture
- Modular FastAPI route structure
- Response model validation
- Structured API error handling
- Feature based route organization

#### Phase 1F Part 1
- Custom exception architecture
- Centralized FastAPI exception handlers
- Structured API error responses
- Service level domain exceptions
- Global error handling middleware

#### Phase 1F Part 2
- FastAPI middleware architecture
- Request correlation ID system
- Request lifecycle tracing
- Response timing headers
- Request scoped context propagation

#### Phase 1G Part 1
- Structured logging architecture
- Request scoped contextual logging
- Middleware request lifecycle logging
- Correlation ID log tracing
- Centralized logger configuration

#### Phase 1G Part 2
- Structured exception logging
- Contextual request linked error tracing
- Stack trace observability
- Centralized production diagnostics
- Severity based logging architecture

#### Phase 1G Part 3
- JSON structured logging
- Machine readable observability pipelines
- Environment aware logging configuration
- Production log serialization
- Semantic API access logging

#### Phase 1H
- Typed configuration architecture
- Environment aware runtime settings
- Centralized application settings management
- Deployment safe configuration validation
- Environment specific logging behavior

#### Phase 1I Part 1
- Pytest testing architecture
- Async FastAPI integration testing
- Reusable pytest fixtures
- API validation testing
- Structured failure path testing

#### Phase 1I Part 2
- Isolated async database testing
- Rollback based transaction fixtures
- Dedicated PostgreSQL test database
- Repository integration testing
- Deterministic database isolation

#### Phase 1I Part 3
- Service layer testing architecture
- Async dependency mocking
- Business logic isolation testing
- Failure path validation
- Layered backend testing design

#### Phase 1J Part 1
- Async background task architecture
- Non blocking ingestion processing
- Structured task observability
- Background AI pipeline orchestration
- FastAPI async task workflows

#### Phase 1J Part 2
- Real time RSS financial news ingestion
- Async ingestion pipeline architecture
- Financial article normalization workflows
- Deduplication and data quality processing
- Structured ingestion observability

#### Phase 1J Part 3
- Persistent financial article ingestion
- Database level duplicate prevention
- Historical article metadata tracking
- Scalable RSS persistence workflows
- Structured ingestion storage architecture

#### Phase 1K Part 1
- ChromaDB vector database integration
- Semantic embedding generation pipelines
- Persistent vector storage architecture
- Transformer based semantic retrieval
- AI powered similarity search workflows

#### Phase 1K Part 2
- Automated embedding ingestion pipelines
- Hybrid SQL and vector database architecture
- Semantic indexing workflows
- Background vector generation pipelines
- AI powered financial semantic retrieval

#### Phase 1L
- Semantic financial search API
- ChromaDB powered retrieval endpoints
- Vector similarity search workflows
- Hybrid SQL and vector retrieval architecture
- AI ready retrieval APIs

#### Phase 1M
- Retrieval Augmented Generation (RAG) architecture
- Groq Llama 3 integration
- Context aware financial question answering
- ChromaDB powered semantic retrieval workflows
- Grounded AI responses using retrieved financial news
- Centralized LLM client architecture
- RAG service layer implementation
- Financial intelligence query endpoint (`POST /rag/query`)
- End to end retrieval and generation pipeline
- Semantic search to LLM context orchestration

#### Phase 1N
- Persistent conversation memory architecture
- Session based chat management
- Historical message storage in PostgreSQL
- Multi turn financial conversations
- Memory aware RAG workflows
- Chat session retrieval and persistence
- Conversational financial intelligence endpoint (`POST /chat/query`)

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