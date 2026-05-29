"""
Semantic search API routes.
"""

from fastapi import APIRouter

from apps.vectorstore.embedding_service import (
    EmbeddingService,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)

embedding_service = EmbeddingService()


@router.get("/semantic")
async def semantic_search(
    query: str,
    limit: int = 5,
):
    """
    Semantic financial article search.
    """

    results = await embedding_service.semantic_search(
        query=query,
        limit=limit,
    )

    return results
