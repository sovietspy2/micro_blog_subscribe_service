from fastapi.testclient import TestClient
import logging


from src.main import app

client = TestClient(app)


def test_read_item():
    response = client.post(
        "/subscription",
        json={
            "name": "General Kenobi",
            "time": 1234,
            "email": "user@medomain.me",
        },
    )
    logging.info(response)
    assert response.status_code == 200