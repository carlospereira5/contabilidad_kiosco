# app/models.py

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
