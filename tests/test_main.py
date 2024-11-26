# tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    # Verifica que la respuesta del endpoint raíz sea exitosa
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    # Valida encabezados
    assert "content-type" in response.headers
    assert response.headers["content-type"] == "application/json"

def test_non_existent_route():
    # Verifica que una ruta inexistente devuelva 404
    response = client.get("/non-existent-route")
    assert response.status_code == 404
