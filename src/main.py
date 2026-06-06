from fastapi import FastAPI

from src.modules.users.presentation.routes.user_routes import (
    router as user_router
)

app = FastAPI(
    title="Bale HR Bot",
    version="1.0.0"
)

app.include_router(user_router)


@app.get("/")
async def root():
    return {
        "status": "running"
    }