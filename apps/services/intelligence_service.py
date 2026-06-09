from apps.intelligence.sentiment_service import (
    SentimentService,
)


class IntelligenceService:
    def __init__(self):

        self.sentiment_service = SentimentService()

    async def analyze_article(
        self,
        content: str,
    ):
        """
        Analyze article sentiment.
        """

        sentiment = await self.sentiment_service.analyze(content)

        return {
            "sentiment": sentiment,
        }
