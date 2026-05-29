from fastapi import APIRouter

from apps.schemas.rag import (
    RAGQueryRequest,
)
from apps.services.rag_service import (
    RAGService,
)

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

rag_service = RAGService()


@router.post("/query")
async def query_rag(
    payload: RAGQueryRequest,
):

    return await rag_service.answer_question(payload.query)
