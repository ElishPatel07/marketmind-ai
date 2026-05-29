import asyncio

from apps.vectorstore.embedding_service import (
    EmbeddingService,
)


async def search():

    service = EmbeddingService()

    results = await service.semantic_search("AI infrastructure demand")

    print(results)


asyncio.run(search())
