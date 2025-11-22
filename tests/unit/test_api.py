import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.get("/") 
    assert r.status_code == 200
    assert r.json() == {"message": "API Artesanos funcionando"}

@pytest.mark.asyncio
async def test_create_artesano():
    transport = ASGITransport(app=app)
    payload = {"nombre": "Ana", "ubicacion": "La Guajira", "tipo": "tejido"}
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        r = await ac.post("/api/artesanos", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["nombre"] == "Ana"
