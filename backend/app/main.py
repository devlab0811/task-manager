from fastapi import FastAPI

from app.database import engine
from app.models.base import Base
from app.routes.tasks import router as tasks_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    tasks_router,
    prefix="/tasks",
    tags=["tasks"]
    )

@app.get("/health")
async def health_check():
    return {"status": "ok"}
