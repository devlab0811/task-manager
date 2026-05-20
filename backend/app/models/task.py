from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=True)

    completed = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())