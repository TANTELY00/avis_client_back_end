import pytest

#  Test : création d'un avis valide
@pytest.mark.asyncio
async def test_create_review(client):
    # Payload JSON pour POST
    payload = {
        "client_name": "Test User",
        "client_email": "test@example.com",
        "text": "I love this product, it's excellent!"
    }

    response = await client.post("/reviews/", json=payload)
    assert response.status_code == 200
    data = response.json()
    #  Vérifie que le backend renvoie bien les champs attendus
    assert "sentiment" in data
    assert "theme" in data
    assert "suggestion" in data

#  Test : payload incomplet → erreur 422
@pytest.mark.asyncio
async def test_create_review_invalid_payload(client):
    payload = {
        "client_name": "User",
        "text": "Bad experience"
    }

    response = await client.post("/reviews/", json=payload)
    #  Erreur Pydantic : Unprocessable Entity
    assert response.status_code == 422

#  Test CORS : requête préflight OPTIONS
@pytest.mark.asyncio
async def test_cors_preflight(client):
    headers = {
        "Origin": "http://localhost:5173",
        "Access-Control-Request-Method": "POST"
    }
    response = await client.options("/reviews/", headers=headers)
    #  Doit répondre sans bloquer la requête CORS
    assert response.status_code in [200, 204]
