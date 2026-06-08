"""
Chat service.
"""

from apps.repositories.chat_repository import (
    ChatRepository,
)
from apps.services.rag_service import (
    RAGService,
)


class ChatService:
    def __init__(
        self,
        repository: ChatRepository,
    ):
        self.repository = repository

        self.rag_service = RAGService()

    async def get_or_create_session(
        self,
        session_id: str,
    ):
        """
        Get existing session or create one.
        """

        session = await self.repository.get_session(session_id)

        if session:
            return session

        return await self.repository.create_session(session_id)

    async def save_user_message(
        self,
        session_id: int,
        content: str,
    ):
        """
        Store user message.
        """

        return await self.repository.save_message(
            session_id=session_id,
            role="user",
            content=content,
        )

    async def save_assistant_message(
        self,
        session_id: int,
        content: str,
    ):
        """
        Store assistant message.
        """

        return await self.repository.save_message(
            session_id=session_id,
            role="assistant",
            content=content,
        )

    async def get_conversation_history(
        self,
        session_id: int,
    ):
        """
        Retrieve conversation history.
        """

        return await self.repository.get_recent_messages(session_id)

    def build_history_context(
        self,
        messages,
    ):
        """
        Format chat history.
        """

        history = []

        for message in reversed(messages):
            history.append(f"{message.role}: {message.content}")

        return "\n".join(history)

    async def chat(
        self,
        session_key: str,
        query: str,
    ):
        session = await self.get_or_create_session(session_key)
        messages = await self.get_conversation_history(session.id)

        history = self.build_history_context(messages)

        await self.save_user_message(
            session.id,
            query,
        )

        answer_payload = await self.rag_service.answer_question(
            query=query,
            conversation_history=history,
        )

        await self.save_assistant_message(
            session.id,
            answer_payload["answer"],
        )

        return answer_payload
