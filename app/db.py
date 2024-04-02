from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, AsyncIterator

from settings import settings
from sqlalchemy.exc import InterfaceError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.sql import expression as sql


class DbMgmt:
    def __init__(self, host: str) -> None:
        self._engine = create_async_engine(host, echo=settings.ECHO_SQL)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self) -> None:
        if self._engine is None:
            raise Exception("DbMgmt is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DbMgmt is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def check_db_health(self) -> bool:
        is_healthy = False
        async with self.session() as session:
            try:
                await session.execute(sql.select(1))
                is_healthy = True
            except (InterfaceError, ConnectionRefusedError):
                pass
        return is_healthy


sessionmgr = DbMgmt(settings.DB_CONFIG)


async def get_db_session() -> AsyncGenerator[AsyncSession, Any]:
    async with sessionmgr.session() as session:
        yield session
