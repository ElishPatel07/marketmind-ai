# MarketMind AI

AI powered financial intelligence platform built with FastAPI, PostgreSQL, ChromaDB, and Groq LLMs.

MarketMind automatically ingests financial news, performs sentiment analysis, generates semantic embeddings, stores market intelligence, and provides Retrieval Augmented Generation (RAG) powered insights through a production style backend architecture.

## Features

- Automated financial news ingestion
- Market sentiment analysis
- Semantic search using vector embeddings
- Retrieval Augmented Generation (RAG)
- Multi turn conversational memory
- AI research agent
- Structured research reports
- Portfolio management
- Portfolio intelligence reports
- Portfolio risk analysis
- Portfolio opportunity analysis
- Automated market alerts
- Event driven intelligence workflows
- Background scheduling and automation
- Health monitoring and metrics

## Architecture

```text
Financial News Sources
          │
          ▼
   Ingestion Layer
          │
          ▼
     PostgreSQL
          │
 ┌────────┼──────────┬──────────┬─────────────┐
 ▼        ▼          ▼          ▼             ▼
ChromaDB  Sentiment  Research   Portfolio     Alerts
 ▼                   Agent      Intelligence
Semantic
Search
          │
          ▼
      FastAPI
```

## Tech Stack

| Category        | Technology            |
| --------------- | --------------------- |
| Backend         | FastAPI               |
| Database        | PostgreSQL            |
| ORM             | SQLAlchemy            |
| Migrations      | Alembic               |
| Vector Database | ChromaDB              |
| LLM             | Groq Llama 3.3        |
| NLP             | Sentence Transformers |
| Scheduling      | APScheduler           |
| Infrastructure  | Docker                |
| Testing         | Pytest                |
| Linting         | Ruff                  |

## API Endpoints

### Chat

```http
POST /chat/query
```

Conversational financial intelligence with memory.

### RAG

```http
POST /rag/query
```

Retrieve and answer using financial news context.

### Intelligence

```http
GET /intelligence/summary
```

Market sentiment distribution and AI generated summaries.

### System

```http
GET /system/health
GET /system/status
GET /system/metrics
```

Application monitoring endpoints.

### Research

POST /research/analyze

Generate AI powered market research reports with:

- Key themes
- Risks
- Opportunities
- Market outlook

### Portfolio

POST /portfolio

Create investment portfolios.

GET /portfolio/{portfolio_id}/report

Generate portfolio intelligence reports including:

- Portfolio outlook
- Portfolio risks
- Portfolio opportunities
- AI generated portfolio research

### Alerts

GET /alerts

Retrieve generated market alerts.

Alert Types:

- Bearish sentiment alerts
- Portfolio related market events
- Intelligence driven market signals

## Local Setup

```bash
git clone <repo>

cp .env.example .env

docker compose up -d

alembic upgrade head

make run
```

Swagger UI:

```text
http://localhost:8000/docs
```

## Testing

```bash
pytest
make check
```

## Roadmap

## Completed

- News ingestion
- Semantic search
- Retrieval augmented generation
- Conversation memory
- Market sentiment analysis
- Research agent
- Portfolio intelligence
- Automated market alerts

## Planned

- Daily market reports
- Company intelligence
- Multi-agent orchestration
- Portfolio monitoring rules
- Sector intelligence

## License

MIT