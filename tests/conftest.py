import pytest
from httpx import AsyncClient
from app.main import app

# Fixture pour créer un client de test HTTP (Async)
@pytest.fixture
async def client():
    # AsyncClient = client HTTP pour FastAPI en mode asynchrone
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
