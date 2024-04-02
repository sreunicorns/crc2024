from db import sessionmgr
from fastapi import APIRouter
from schemas import HealthCheck

router = APIRouter(tags=["health"])


@router.get("/healthz", response_model=HealthCheck)
async def check_health() -> dict[str, str]:
    if await sessionmgr.check_db_health():
        status = "Healthy"
    else:
        status = "Unhealthy"

    return {"status": status}
