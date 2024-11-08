import json
import pytest
from faker import Faker

fake = Faker()

def test_user_registration(test_client, init_database):
    user_data = {
        "username": fake.user_name(),
        "password": fake.password()
    }
    response = test_client.post("/api/register", data=json.dumps(user_data), content_type="application/json")
    assert response.status_code == 201

def test_user_login(test_client, init_database):
    login_data = {
        "username": "existing_user",
        "password": "existing_password"
    }
    response = test_client.post("/api/login", data=json.dumps(login_data), content_type="application/json")
    assert response.status_code == 200
    assert b"token" in response.data
