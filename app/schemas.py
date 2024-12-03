# app/schemas.py

from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: str = "user"

class UsuarioCreate(UsuarioBase):
    password: str  # Contraseña para creación

class UsuarioOut(UsuarioBase):
    id: int
    creado_en: datetime

    class Config:
        orm_mode = True
