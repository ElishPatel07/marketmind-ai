from apps.intelligence.sentiment_service import (
    SentimentService,
)
from apps.llm.groq_client import client


class IntelligenceService:
    def __init__(
        self,
        repository=None,
    ):

        self.sentiment_service = SentimentService()

        self.repository = repository

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

    async def get_summary(
        self,
    ):
        """
        Market sentiment summary.
        """

        rows = await self.repository.get_sentiment_counts()

        summary = {
            "bullish": 0,
            "bearish": 0,
            "neutral": 0,
            "total_articles": 0,
        }

        market_summary = await self.generate_market_summary()

        for sentiment, count in rows:
            if sentiment == "BULLISH":
                summary["bullish"] = count

            elif sentiment == "BEARISH":
                summary["bearish"] = count

            elif sentiment == "NEUTRAL":
                summary["neutral"] = count

            summary["total_articles"] += count

        summary["market_summary"] = market_summary

        return summary

    async def generate_market_summary(
        self,
    ):
        """
        Generate market overview.
        """

        articles = await self.repository.get_recent_articles()

        content = "\n\n".join(article.content for article in articles)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
    Summarize the current market.

    Provide:

    1. Key themes
    2. Major risks
    3. Major opportunities

    Articles:

    {content}
    """,
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content
