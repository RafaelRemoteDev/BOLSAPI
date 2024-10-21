from fastapi.testclient import TestClient
from app.main import app
import httpx


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to BOLSAPI: the crypto and commodities alert bot API!"}
