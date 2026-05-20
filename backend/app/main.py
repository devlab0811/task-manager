from fastapi import FastAPI
from app.models.base import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}
