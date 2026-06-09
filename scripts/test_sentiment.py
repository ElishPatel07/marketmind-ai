import asyncio

from apps.intelligence.sentiment_service import (
    SentimentService,
)


async def main():

    service = SentimentService()

    result = await service.analyze(
        "NVIDIA beats earnings expectations and raises guidance."
    )

    print(result)


asyncio.run(main())
