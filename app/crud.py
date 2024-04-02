from typing import Sequence

from models import Application
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import expression as sql


async def get_all(db_session: AsyncSession) -> Sequence[Application]:
    query = sql.select(Application)
    all_apps = await db_session.execute(query)
    all_apps = all_apps.scalars().all()
    return all_apps


async def get_by_id(id: str, db_session: AsyncSession) -> Application | None:
    query = sql.select(Application).where(Application.id == id)
    application = await db_session.execute(query)
    try:
        (application,) = application.one()
    except NoResultFound:
        application = None
    return application
