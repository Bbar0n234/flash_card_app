from fastapi import FastAPI, APIRouter

from api import router as api_router

from core import settings

import uvicorn


main_app = FastAPI()

main_app.include_router(
    router=api_router,
)


@main_app.get("/")
async def root_def():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run(app="main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)