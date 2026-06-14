"""
Research agent.
"""

import json
import re

from apps.llm.groq_client import client
from apps.services.rag_service import RAGService


class ResearchAgent:
    def __init__(
        self,
    ):
        self.rag_service = RAGService()

    async def analyze(
        self,
        query: str,
    ):
        """
        Generate research report.
        """

        context = await self.rag_service.retrieve_context(query)

        prompt = f"""
        You are a senior financial analyst.

        Using only the supplied context,
        generate a market research report.

        Return valid JSON.

        Format:

        {{
            "themes": [],
            "risks": [],
            "opportunities": [],
            "outlook": "",
            "report": ""
        }}

        Rules:

        - themes must contain 3 items
        - risks must contain 3 items
        - opportunities must contain 3 items
        - outlook must be:
        BULLISH
        BEARISH
        or
        NEUTRAL

        Context:

        {context}
        """
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
        )

        content = (response.choices[0].message.content).strip()

        match = re.search(
            r"\{.*\}",
            content,
            re.DOTALL,
        )

        if not match:
            raise ValueError("No JSON found in LLM response")

        data = json.loads(match.group())

        return {
            "query": query,
            "themes": data["themes"],
            "risks": data["risks"],
            "opportunities": data["opportunities"],
            "outlook": data["outlook"],
            "report": data["report"],
        }
