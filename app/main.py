from fastapi import FastAPI
from contextlib import asynccontextmanager

from api import router as api_router
from core.auth import main_router as auth_router

from core import settings
from core.models import db_helper


import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)

main_app.include_router(
    router=api_router,
)

main_app.include_router(
    router=auth_router,
)


@main_app.get("/")
async def root_def():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run(app="main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)