import pytest

def test_create_strategy(test_client):
    strategy_data = {
        "name": "Power Saving",
        "description": "Turn off lights during daylight hours."
    }
    response = test_client.post("/api/strategy", json=strategy_data)
    assert response.status_code == 201
