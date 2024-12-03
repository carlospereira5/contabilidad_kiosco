# tests/test_models.py

import pytest
from app.models import Base, Usuario
from app.database import SessionLocal, engine

# Configurar la base de datos para pruebas
@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)  # Crear tablas
    db_session = SessionLocal()
    yield db_session
    db_session.close()
    Base.metadata.drop_all(bind=engine)  # Eliminar tablas después de las pruebas

def test_crear_usuario(db):
    nuevo_usuario = Usuario(
        nombre="Carlos Pereira",
        email="carlos@example.com",
        hashed_password="hashed_password_example",
        rol="admin",
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    assert nuevo_usuario.id is not None
    assert nuevo_usuario.nombre == "Carlos Pereira"
    assert nuevo_usuario.email == "carlos@example.com"
    assert nuevo_usuario.rol == "admin"
