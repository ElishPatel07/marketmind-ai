"""
Market sentiment analysis.
"""

from apps.llm.groq_client import client


class SentimentService:
    async def analyze(
        self,
        text: str,
    ):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""
        Classify sentiment.

        Return ONLY one value:

        BULLISH
        BEARISH
        NEUTRAL

        Text:

        {text}
        """,
                }
            ],
            temperature=0,
        )

        return response.choices[0].message.content.strip()
