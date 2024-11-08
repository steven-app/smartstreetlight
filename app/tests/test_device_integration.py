import json
import pytest
from faker import Faker

fake = Faker()

def test_device_creation(test_client, init_database):
    device_data = {
        "name": fake.name(),
        "location": fake.address(),
        "ip_address": fake.ipv4(),
        "status": "active"
    }
    response = test_client.post("/api/device", data=json.dumps(device_data), content_type="application/json")
    assert response.status_code == 201

def test_get_device(test_client, init_database):
    response = test_client.get("/api/device/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "name" in data
    assert "location" in data
    assert "ip_address" in data
