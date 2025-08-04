from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={
        "session_id": "test-session",
        "query": "Tell me about Goa tourism."
    })
    assert response.status_code == 200
    assert "response" in response.json()
