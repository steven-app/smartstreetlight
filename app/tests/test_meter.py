import pytest

def test_read_meter(test_client):
    response = test_client.get("/api/meter/1")
    assert response.status_code == 200
    data = response.get_json()
    assert "meter_value" in data
