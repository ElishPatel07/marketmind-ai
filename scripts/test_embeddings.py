import asyncio

from apps.vectorstore.embedding_service import (
    EmbeddingService,
)


async def test_embedding():

    service = EmbeddingService()

    await service.generate_embedding(
        article_id=1,
        content=("NVIDIA stock surged after strong AI infrastructure earnings."),
    )

    results = await service.semantic_search("AI chip demand")

    print(results)


asyncio.run(test_embedding())
