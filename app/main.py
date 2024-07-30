from fastapi import FastAPI, APIRouter

import uvicorn


main_app = FastAPI()


@main_app.get("/")
async def root_def():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run(app="main:main_app",
                host="0.0.0.0",
                port="9998",
                reload=True)