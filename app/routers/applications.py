from typing import Sequence

from crud import get_all, get_by_id
from db import get_db_session
from fastapi import APIRouter, Depends, HTTPException
from models import Application
from schemas import ApplicationSchema

router = APIRouter(prefix="/applications", tags=["applications"])


@router.get(
    "/",
    response_model=Sequence[ApplicationSchema],
)
async def get_all_apps(db_session=Depends(get_db_session)) -> Sequence[Application]:
    applications = await get_all(db_session)
    return applications


@router.get("/{id}", response_model=ApplicationSchema)
async def get_app(id: str, db_session=Depends(get_db_session)) -> Application:
    application = await get_by_id(id, db_session)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application
