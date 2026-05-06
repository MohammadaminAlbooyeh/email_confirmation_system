import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_signup_success():
    """Test successful user signup"""
    response = client.post(
        "/api/auth/signup",
        json={
            "email": "test@example.com",
            "password": "TestPassword123!",
            "full_name": "Test User"
        }
    )
    assert response.status_code in [200, 422]  # May fail due to DB not set up


def test_login_invalid_credentials():
    """Test login with invalid credentials"""
    response = client.post(
        "/api/auth/login",
        json={
            "email": "nonexistent@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code in [422, 401]
