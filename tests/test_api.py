import pytest
import requests
import time

# ==========================================
# 3. CORE INTEGRATION TESTS (HAPPY PATHS)
# ==========================================

def test_health_endpoint_returns_healthy(base_url):
    """Happy Path 1: Check server running health status."""
    response = requests.get(f"{base_url}/api/health")
    assert response.status_code == 200
    assert "healthy" in response.text.lower() or response.json().get("status") == "healthy"

def test_register_user_creates_new_user(base_url, unique_user_credentials):
    """Happy Path 2: Register a user with a unique timestamped name."""
    response = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert response.status_code == 201
    assert response.json()["user"]["username"] == unique_user_credentials["username"]

def test_login_returns_jwt_token(base_url, unique_user_credentials):
    """Happy Path 3: Log in with known user and retrieve a JWT."""
    # Register the user first
    requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # Attempt login
    response = requests.post(f"{base_url}/api/auth/login", json=unique_user_credentials)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_public_event_requires_auth_and_succeeds_with_token(base_url, authenticated_headers):
    """Happy Path 4: Call POST /events with a valid JWT payload."""
    event_payload = {
        "title": "Public Networking Event",
        "date": "2026-06-01",
        "is_public": True
    }
    response = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    assert response.status_code == 201
    assert response.json().get("title") == "Public Networking Event"

def test_rsvp_to_public_event_succeeds_without_auth(base_url, authenticated_headers):
    """Happy Path 5: Create a public event first, then RSVP without any auth token."""
    # Create the public event with credentials
    event_payload = {"title": "Open House", "date": "2026-07-01", "is_public": True}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # RSVP without using authenticated headers
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp_res.status_code in [200, 201]
    assert rsvp_res.json().get("event_id") == event_id


# ==========================================
# 4. ERROR / EDGE-CASE TESTS
# ==========================================

def test_duplicate_username_registration_returns_400(base_url, unique_user_credentials):
    """Edge Case 1: Registering duplicate username returns a bad request error."""
    # First registration succeeds
    res1 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert res1.status_code == 201

    # Second registration with exact same username fails
    res2 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert res2.status_code == 400

def test_create_event_without_auth_returns_401(base_url):
    """Edge Case 2: Attempting to create an event with no token returns 401 Unauthorized."""
    event_payload = {"title": "Secret Event", "date": "2026-08-01", "is_public": True}
    response = requests.post(f"{base_url}/api/events", json=event_payload) # No headers sent
    assert response.status_code == 401

def test_rsvp_to_non_public_event_without_auth_returns_error(base_url, authenticated_headers):
    """Edge Case 3: RSVPs to private events without a token are blocked."""
    # Create a private non-public event
    event_payload = {"title": "Private Board Meeting", "date": "2026-09-01", "is_public": False}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # Attempt RSVP without authorization headers
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp_res.status_code in [401, 403, 404] # Depends on security setup

#==============================================================================
#========================== MY OWN TESTING BLOCK ==============================
#==============================================================================
if __name__ == '__main__':
    import time
    base_url = "http://localhost:4000"
    timestamp = int(time.time() * 1000)

    unique_user_credentials =         {
        "username": f"user_{timestamp}",
        "password": "SecurePassword123"
    }
    requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    response = requests.post(f"{base_url}/api/auth/login", json=unique_user_credentials)
    token = response.json()["access_token"]
    authenticated_headers = {"Authorization": f"Bearer {token}"}

    event_payload = {"title": "Open House", "date": "2026-07-01", "is_public": True}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")
    print(create_res.text)
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    print(rsvp_res.text)
