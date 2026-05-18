import pytest
import requests
import time

# Changed port
BASE_URL = "http://localhost:4000"

@pytest.fixture(scope="session")
def base_url():
    """Provides the base URL for the running API server."""
    return BASE_URL

@pytest.fixture
def unique_user_credentials():
    """Generates a guaranteed unique username using a timestamp."""
    timestamp = int(time.time() * 1000)
    return {
        "username": f"user_{timestamp}",
        "password": "SecurePassword123"
    }

@pytest.fixture
def authenticated_headers(base_url, unique_user_credentials):
    """
    Helper fixture that automatically registers a user, logs them in,
    and returns authorization headers containing a valid JWT token.
    """
    # 1. Register
    requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # 2. Login
    login_response = requests.post(f"{base_url}/api/auth/login", json=unique_user_credentials)
    token = login_response.json().get("access_token")

    return {"Authorization": f"Bearer {token}"}
