"""
Retrieval augmented generation service.
"""

from apps.llm.groq_client import client
from apps.vectorstore.embedding_service import (
    EmbeddingService,
)


class RAGService:
    def __init__(self):

        self.embedding_service = EmbeddingService()

    async def retrieve_context(
        self,
        query: str,
    ):
        """
        Retrieve relevant articles.
        """

        results = await self.embedding_service.semantic_search(
            query=query,
            limit=5,
        )

        documents = results["documents"][0]

        return "\n\n".join(documents)

    async def answer_question(
        self,
        query: str,
        conversation_history: str = "",
    ):
        """
        Generate grounded answer.
        """

        context = await self.retrieve_context(query)

        prompt = f"""
        You are MarketMind AI.

        Use the conversation history and
        retrieved financial context.

        Conversation History:

        {conversation_history}

        Retrieved Financial Context:

        {context}

        Question:

        {query}

        Answer using the retrieved context.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.1,
        )

        answer = response.choices[0].message.content

        return {
            "answer": answer,
            "context": context,
        }
