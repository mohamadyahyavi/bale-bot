from fastapi import FastAPI

from src.modules.users.presentation.routes.user_routes import (
    router as user_router
)
from src.modules.departments.presentation.routes.department_routes import (
    router as department_router
)

app = FastAPI(
    title="Bale HR Bot",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(department_router)


@app.get("/")
async def root():
    return {
        "status": "running"
    }