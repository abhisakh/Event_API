import pytest
import requests
import time

# ==========================================
# 3. CORE INTEGRATION TESTS (HAPPY PATHS)
# ==========================================

def test_health_endpoint_returns_healthy(base_url):
    """Happy Path 1: Check server running health status."""
    # Act: Request the health check endpoint
    response = requests.get(f"{base_url}/api/health")

    # Assert: Verify the server is alive and responding correctly
    assert response.status_code == 200  # Confirms the endpoint exists and is reachable
    # Checks for "healthy" string or JSON key to ensure the internal logic is working
    assert "healthy" in response.text.lower() or response.json().get("status") == "healthy"

def test_register_user_creates_new_user(base_url, unique_user_credentials):
    """Happy Path 2: Register a user with a unique timestamped name."""
    # Act: Send user details to the registration endpoint
    response = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # Assert: Verify the user was created successfully
    assert response.status_code == 201  # Confirms successful resource creation
    # Confirms the returned username matches the one we sent
    assert response.json()["user"]["username"] == unique_user_credentials["username"]

def test_login_returns_jwt_token(base_url, unique_user_credentials):
    """Happy Path 3: Log in with known user and retrieve a JWT."""
    # Arrange: Ensure the user exists by registering them first
    requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # Act: Attempt to login with those credentials
    response = requests.post(f"{base_url}/api/auth/login", json=unique_user_credentials)

    # Assert: Verify the login granted access
    assert response.status_code == 200  # Confirms valid credentials were accepted
    assert "access_token" in response.json()  # Ensures a security token was returned

def test_create_public_event_requires_auth_and_succeeds_with_token(base_url, authenticated_headers):
    """Happy Path 4: Call POST /events with a valid JWT payload."""
    # Arrange: Prepare the event details
    event_payload = {
        "title": "Public Networking Event",
        "date": "2026-06-01",
        "is_public": True
    }

    # Act: Send the creation request with the JWT in headers
    response = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)

    # Assert: Verify the event is now in the database
    assert response.status_code == 201  # Confirms the event was created
    assert response.json().get("title") == "Public Networking Event"  # Verifies data integrity

def test_rsvp_to_public_event_succeeds_without_auth(base_url, authenticated_headers):
    """Happy Path 5: Create a public event first, then RSVP without any auth token."""
    # Arrange: Create a public event using credentials
    event_payload = {"title": "Open House", "date": "2026-07-01", "is_public": True}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # Act: RSVP to the event without using the authentication headers
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})

    # Assert: Verify public RSVP is allowed
    assert rsvp_res.status_code in [200, 201]  # Confirms successful RSVP
    assert rsvp_res.json().get("event_id") == event_id  # Confirms RSVP is linked to correct event

def test_get_all_events_returns_list(base_url):
    """Happy Path: Verifies that fetching all events returns a 200 OK and a list layout."""
    # Act: Fetch the list of events
    response = requests.get(f"{base_url}/api/events")

    # Assert: Verify response format
    assert response.status_code == 200  # Confirms endpoint is functional
    assert isinstance(response.json(), list)  # Ensures the API returns an array/list of data


# ==========================================
# 4. ERROR / EDGE-CASE TESTS
# ==========================================

def test_duplicate_username_registration_returns_400(base_url, unique_user_credentials):
    """Edge Case 1: Registering duplicate username returns a bad request error."""
    # Arrange: Register the user once
    res1 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert res1.status_code == 201

    # Act: Attempt to register the exact same username again
    res2 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # Assert: Verify the system blocks duplicates
    assert res2.status_code == 400  # Confirms the API handles duplicate constraints

def test_create_event_without_auth_returns_401(base_url):
    """Edge Case 2: Attempting to create an event with no token returns 401 Unauthorized."""
    # Arrange: Prepare payload but ignore headers
    event_payload = {"title": "Secret Event", "date": "2026-08-01", "is_public": True}

    # Act: Request creation without any JWT headers
    response = requests.post(f"{base_url}/api/events", json=event_payload)

    # Assert: Verify unauthorized access is blocked
    assert response.status_code == 401  # Confirms security is active for this route

def test_rsvp_to_non_public_event_without_auth_returns_error(base_url, authenticated_headers):
    """Edge Case 3: RSVPs to private events without a token are blocked."""
    # Arrange: Create a private (is_public=False) event
    event_payload = {"title": "Private Board Meeting", "date": "2026-09-01", "is_public": False}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # Act: Attempt to RSVP to this private event anonymously
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})

    # Assert: Verify the API protects private data
    # Confirms that without a token, the user cannot interact with private events
    assert rsvp_res.status_code in [401, 403, 404]

def test_get_invalid_event_id_returns_404(base_url):
    """Edge Case: Requesting an event ID that does not exist should yield a 404 Not Found."""
    # Arrange: Define an ID that is statistically unlikely to exist
    invalid_id = 999999

    # Act: Try to fetch the non-existent event
    response = requests.get(f"{base_url}/api/events/{invalid_id}")

    # Assert: Verify the 404 error handling
    assert response.status_code == 404  # Confirms the API correctly identifies missing resources

def test_create_event_with_missing_required_fields_returns_400(base_url, authenticated_headers):
    """Edge Case: Sending an event payload without a 'title' should trigger a 400 Bad Request."""
    # Arrange: Provide a payload missing the required 'title' field
    incomplete_payload = {
        "date": "2026-12-01T12:00:00",
        "is_public": True
    }

    # Act: Submit the invalid data
    response = requests.post(f"{base_url}/api/events", json=incomplete_payload, headers=authenticated_headers)

    # Assert: Verify validation logic
    assert response.status_code == 400  # Confirms the server validates required input fields

def test_rsvp_to_non_existent_event_returns_404(base_url, authenticated_headers):
    """Edge Case: Attempting to RSVP to an event ID that does not exist should return a 404."""
    # Arrange: Use an invalid ID
    invalid_event_id = 888888

    # Act: Attempt to RSVP
    response = requests.post(f"{base_url}/api/rsvps/event/{invalid_event_id}", json={"attending": True}, headers=authenticated_headers)

    # Assert: Verify the error response
    assert response.status_code == 404  # Confirms RSVP logic also validates event existence

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
