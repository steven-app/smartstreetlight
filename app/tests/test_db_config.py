import pytest

def test_mysql_config(test_client):
    response = test_client.get("/api/db-config/mysql")
    assert response.status_code == 200
    assert "MySQL" in response.get_json()

def test_postgresql_config(test_client):
    response = test_client.get("/api/db-config/postgresql")
    assert response.status_code == 200
    assert "PostgreSQL" in response.get_json()

def test_mongodb_config(test_client):
    response = test_client.get("/api/db-config/mongodb")
    assert response.status_code == 200
    assert "MongoDB" in response.get_json()
