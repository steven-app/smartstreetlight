import pytest

def test_get_map_devices(test_client):
    response = test_client.get("/api/map/devices")
    assert response.status_code == 200
    assert "devices" in response.get_json()
