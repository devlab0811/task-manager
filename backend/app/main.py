from fastapi import FastAPI
from app.models.base import Base
from app.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
