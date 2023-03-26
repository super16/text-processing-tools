from typing import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from text_processing_tools.config import Settings, get_settings


class DatabaseConnection:

    """Connection class to database with SQLAlchemy."""

    def __init__(self, settings: Settings) -> None:
        self._url: URL = URL.create(
            settings.db_engine,
            username=settings.db_user,
            password=settings.db_password,
            host=settings.db_host,
            port=settings.db_port,
            database=settings.db_name,
        )
        self._connection: AsyncEngine = create_async_engine(self._url)
        self._session_factory: async_sessionmaker[AsyncSession] = \
            async_sessionmaker(
                self._connection, expire_on_commit=False,
            )

    async def create_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_factory() as session:
            yield session


database_conn = DatabaseConnection(get_settings())
