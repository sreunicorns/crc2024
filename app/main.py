from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

import uvicorn
from db import sessionmgr
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from routers import applications, healthz
from settings import settings

# Disabled for systemd
# with open("logging.yml") as f:
#     config = yaml.load(f, Loader=yaml.FullLoader)
#     logging.config.dictConfig(config)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, None]:
    yield
    if sessionmgr._engine is not None:
        await sessionmgr.close()


def init_api() -> FastAPI:
    app = FastAPI(lifespan=lifespan, title=settings.APP_NAME)
    app.include_router(applications.router, prefix="/api/v1")
    app.include_router(healthz.router)
    return app


app = init_api()
Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
