from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.models.chat_message import (
    ChatMessage,
)
from apps.db.models.chat_session import (
    ChatSession,
)


class ChatRepository:
    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def get_session(
        self,
        session_id: str,
    ):
        """
        Find chat session.
        """

        result = await self.db.execute(
            select(ChatSession).where(ChatSession.session_id == session_id)
        )

        return result.scalar_one_or_none()

    async def create_session(
        self,
        session_id: str,
    ):
        """
        Create chat session.
        """

        session = ChatSession(session_id=session_id)

        self.db.add(session)

        await self.db.commit()

        await self.db.refresh(session)

        return session

    async def save_message(
        self,
        session_id: int,
        role: str,
        content: str,
    ):
        """
        Save chat message.
        """

        message = ChatMessage(
            session_id=session_id,
            role=role,
            content=content,
        )

        self.db.add(message)

        await self.db.commit()

        await self.db.refresh(message)

        return message

    async def get_recent_messages(
        self,
        session_id: int,
        limit: int = 10,
    ):
        """
        Get recent chat history.
        """

        result = await self.db.execute(
            select(ChatMessage)
            .where(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.id.desc())
            .limit(limit)
        )

        return result.scalars().all()
