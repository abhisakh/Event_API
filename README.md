# 🎉 Evently API

A Flask-based REST API for managing events and RSVPs with role-based access control. This project serves as an educational platform for learning web security best practices through incremental improvements.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Pytest](https://img.shields.io/badge/Tests-13%20Passing-brightgreen.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Comprehensive Test Suite Documentation](#-comprehensive-test-suite-documentation)
- [API Reference](#-api-reference)
- [Security Considerations](#-security-considerations)

## ✨ Features

- **🌐 Public Events**: Open RSVP system without authentication requirements
- **🔒 Protected Events**: User authentication required for RSVP
- **👑 Admin Events**: Admin role required for RSVP access
- **🔐 JWT Authentication**: Secure token-based authentication system
- **📚 Swagger UI**: Interactive API documentation
- **✅ Comprehensive Testing**: 13 tests covering unit and integration scenarios
- **💾 SQLite Database**: Lightweight, file-based database solution

## 🛠 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | Flask | 3.0.0 |
| **Database ORM** | Flask-SQLAlchemy | Latest |
| **Database** | SQLite | Built-in |
| **Authentication** | Flask-JWT-Extended | Latest |
| **CORS** | Flask-CORS | Latest |
| **API Documentation** | Flasgger | Latest |
| **Testing Framework** | Pytest | Latest |
| **HTTP Client** | Requests | Latest |

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd evently-api
   ```

2. **Create and activate a virtual environment**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Server

Start the Flask development server:

```bash
python app.py
```

**The API will be available at:** `http://localhost:4000`

**Important Notes:**
- The database file (`events.db`) will be created automatically on first run
- The first registered user automatically receives admin privileges for demo purposes
- The server runs on **port 4000** by default

### API Documentation

Once the server is running, access the interactive Swagger UI documentation:

**🔗 Swagger UI**: `http://localhost:4000/apidocs`

**🔗 OpenAPI Spec**: `http://localhost:4000/apispec_1.json`

---

# 🧪 Comprehensive Test Suite Documentation

The Evently API includes a **production-grade automated testing suite** built with `pytest`. The test architecture validates both **isolated unit logic** and **end-to-end integration workflows**, ensuring comprehensive coverage of functionality, security boundaries, and error handling.

## 📁 Test Architecture

```text
tests/
├── __init__.py              # Python package initializer
├── conftest.py              # Pytest fixtures and configuration
├── test_models.py           # Unit tests (5 tests) - Pure Python, no I/O
└── test_api.py              # Integration tests (8 tests) - HTTP E2E workflows
```

**Total Test Count: 13 tests**
- ✅ **5 Unit Tests**: Database model logic validation
- ✅ **6 Happy Path Tests**: Successful workflow validation
- ✅ **7 Error/Edge Case Tests**: Error handling and validation

---

## 📦 File 1: `conftest.py` - Test Configuration & Fixtures

**Purpose**: Centralizes pytest configuration, shared fixtures, and utilities used across all test modules.

### Configuration Constants

```python
BASE_URL = "http://localhost:4000"
```
- Defines the API server endpoint for all integration tests
- Centralized configuration - easy to update if port changes
- Used by all HTTP request operations

---

### Fixture 1: `base_url` (Session Scope)

**Signature**: `@pytest.fixture(scope="session")`

**Purpose**: Provides the base URL for the running API server.

**Returns**: `"http://localhost:4000"`

**Scope**: Session-level (created once per test session)

**Usage Example**:
```python
def test_health_endpoint(base_url):
    response = requests.get(f"{base_url}/api/health")
```

**Why Session Scope?**:
- URL doesn't change during test execution
- Improves performance by creating once
- Shared across all tests

---

### Fixture 2: `unique_user_credentials` (Function Scope)

**Signature**: `@pytest.fixture`

**Purpose**: Generates guaranteed unique username credentials using millisecond-precision timestamps.

**Returns**:
```python
{
    "username": "user_1737283920123",  # timestamp in milliseconds
    "password": "SecurePassword123"
}
```

**Implementation Details**:
```python
timestamp = int(time.time() * 1000)  # Milliseconds since epoch
return {
    "username": f"user_{timestamp}",
    "password": "SecurePassword123"
}
```

**Key Features**:
- ✅ Timestamp in **milliseconds** ensures uniqueness
- ✅ Function-scoped: New credentials for each test
- ✅ Prevents database conflicts from duplicate usernames
- ✅ Allows tests to run repeatedly without cleanup

**Why Milliseconds?**:
- Multiple tests can run in the same second
- Millisecond precision prevents collisions
- Example: `user_1737283920123` vs `user_1737283920456`

**Usage Example**:
```python
def test_register_user(base_url, unique_user_credentials):
    response = requests.post(
        f"{base_url}/api/auth/register", 
        json=unique_user_credentials
    )
    # username is unique every time this test runs
```

---

### Fixture 3: `authenticated_headers` (Function Scope)

**Signature**: `@pytest.fixture`

**Purpose**: Automatically registers a user, logs them in, and returns authorization headers containing a valid JWT token.

**Dependencies**: 
- `base_url` fixture
- `unique_user_credentials` fixture

**Returns**:
```python
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Implementation Flow**:
```python
def authenticated_headers(base_url, unique_user_credentials):
    # Step 1: Register a new user
    requests.post(
        f"{base_url}/api/auth/register", 
        json=unique_user_credentials
    )
    
    # Step 2: Login with registered credentials
    login_response = requests.post(
        f"{base_url}/api/auth/login", 
        json=unique_user_credentials
    )
    
    # Step 3: Extract JWT token
    token = login_response.json().get("access_token")
    
    # Step 4: Return formatted authorization header
    return {"Authorization": f"Bearer {token}"}
```

**Why This Fixture Is Powerful**:
- ✅ Eliminates boilerplate: Tests don't repeat registration/login
- ✅ Automatic setup: Fresh authenticated user for each test
- ✅ Clean syntax: Tests simply request `authenticated_headers`
- ✅ Realistic: Mimics actual user authentication flow

**Usage Example**:
```python
def test_create_event(base_url, authenticated_headers):
    # Headers already contain valid JWT token
    response = requests.post(
        f"{base_url}/api/events",
        json={"title": "My Event", "date": "2026-06-01"},
        headers=authenticated_headers  # Authentication handled!
    )
```

**Token Format**:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzI4MzkyMCwianRpIjoiYWJjMTIzIiwibmJmIjoxNzM3MjgzOTIwLCJzdWIiOjEsInR5cGUiOiJhY2Nlc3MifQ.signature
```
- Prefix: `"Bearer "`
- Token: JWT with header, payload, and signature
- Valid until expiration (configurable in Flask app)

---

## 📦 File 2: `test_models.py` - Unit Tests (5 Tests)

**Philosophy**: Pure unit tests validating database model logic in complete isolation. Execute entirely in Python memory with **no database persistence, no HTTP requests, no external dependencies**.

---

### ✅ Test 1: `test_user_password_hashing_behaves_correctly`

**Function Name**: `test_user_password_hashing_behaves_correctly()`

**Category**: User Model - Security

**Purpose**: Verifies that password hashing and verification mechanism works correctly using werkzeug security.

**What It Tests**:
- ✅ `set_password()` method hashes plaintext passwords
- ✅ Passwords are **never stored in plaintext**
- ✅ `check_password()` correctly verifies valid passwords
- ✅ `check_password()` correctly rejects invalid passwords

**Test Implementation**:
```python
def test_user_password_hashing_behaves_correctly():
    # Create User instance in memory
    user = User()
    user.username = "test_user"
    user.set_password("SecureSecretPass123!")
    
    # Assertion 1: Hash is NOT equal to plaintext
    assert user.password_hash != "SecureSecretPass123!"
    
    # Assertion 2: Correct password validates as True
    assert user.check_password("SecureSecretPass123!") is True
    
    # Assertion 3: Wrong password validates as False
    assert user.check_password("WrongPassword123") is False
```

**Security Mechanisms**:
- Uses werkzeug's `generate_password_hash()` and `check_password_hash()`
- One-way cryptographic hashing (cannot reverse)
- Automatic salting prevents rainbow table attacks
- Each hash is unique even for identical passwords

**Assertions Breakdown**:

| Assertion | What It Validates | Why It Matters |
|-----------|-------------------|----------------|
| `password_hash != plaintext` | Hash is created, not plaintext stored | Prevents credential exposure |
| `check_password(correct) == True` | Valid credentials are accepted | Users can log in |
| `check_password(wrong) == False` | Invalid credentials are rejected | Prevents unauthorized access |

**Why This Test Matters**:
- Password security is foundational to authentication
- Prevents database compromise from exposing passwords
- Validates the security layer works before deployment

---

### ✅ Test 2: `test_user_to_dict_conversion`

**Function Name**: `test_user_to_dict_conversion()`

**Category**: User Model - Serialization

**Purpose**: Validates the User model correctly serializes to dictionary format suitable for JSON API responses.

**What It Tests**:
- ✅ `to_dict()` method returns all required fields
- ✅ Timestamps are ISO 8601 formatted strings
- ✅ No sensitive data (password_hash) in output
- ✅ Boolean and integer types preserved

**Test Implementation**:
```python
def test_user_to_dict_conversion():
    # Create User with known test data
    fixed_time = datetime(2026, 5, 18, 12, 0, 0)
    
    user = User(
        id=42,
        username="admin_guy",
        is_admin=True,
        created_at=fixed_time
    )
    
    # Convert to dictionary
    user_dict = user.to_dict()
    
    # Assert all fields are correct
    assert user_dict["id"] == 42
    assert user_dict["username"] == "admin_guy"
    assert user_dict["is_admin"] is True
    assert user_dict["created_at"] == "2026-05-18T12:00:00"
```

**Expected Dictionary Output**:
```python
{
    "id": 42,
    "username": "admin_guy",
    "is_admin": True,
    "created_at": "2026-05-18T12:00:00"
}
```

**Field Specifications**:

| Field | Type | Format | Notes |
|-------|------|--------|-------|
| `id` | int | Integer | Primary key |
| `username` | str | String | Unique identifier |
| `is_admin` | bool | Boolean | Role flag |
| `created_at` | str | ISO 8601 | "YYYY-MM-DDTHH:MM:SS" |

**What's Excluded** (Security):
- ❌ `password_hash` - Never exposed in API responses
- ❌ Internal database fields

**Why This Test Matters**:
- API responses must return consistent, well-formatted data
- Prevents accidental exposure of sensitive fields
- Ensures frontend clients receive expected data structure
- Validates datetime serialization works correctly

---

### ✅ Test 3: `test_event_to_dict_empty_rsvps`

**Function Name**: `test_event_to_dict_empty_rsvps()`

**Category**: Event Model - Serialization (Empty State)

**Purpose**: Validates Event model serialization when no attendees have RSVPed (boundary condition).

**What It Tests**:
- ✅ `to_dict()` handles zero RSVPs gracefully
- ✅ Returns empty list for `attendees` (not null)
- ✅ `rsvp_count` correctly calculates as 0
- ✅ All event metadata fields included

**Test Implementation**:
```python
def test_event_to_dict_empty_rsvps():
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)
    
    # Create Event with empty RSVPs list
    event = Event(
        id=101,
        title="Tech Conference",
        description="A great developer meetup",
        date=fixed_time,
        location="Room A",
        capacity=100,
        is_public=True,
        requires_admin=False,
        created_by=42,
        created_at=fixed_time,
        rsvps=[]  # Explicitly empty
    )
    
    event_dict = event.to_dict()
    
    # Validate structure
    assert event_dict["id"] == 101
    assert event_dict["title"] == "Tech Conference"
    assert event_dict["rsvp_count"] == 0
    assert event_dict["attendees"] == []
```

**Expected Dictionary Output**:
```python
{
    "id": 101,
    "title": "Tech Conference",
    "description": "A great developer meetup",
    "date": "2026-06-01T15:30:00",
    "location": "Room A",
    "capacity": 100,
    "is_public": True,
    "requires_admin": False,
    "created_by": 42,
    "created_at": "2026-06-01T15:30:00",
    "rsvp_count": 0,
    "attendees": []
}
```

**Key Validations**:

| Field | Expected Value | Why It Matters |
|-------|---------------|----------------|
| `rsvp_count` | `0` | Count of RSVPs (total) |
| `attendees` | `[]` | Empty list, not null | Prevents frontend errors |

**Edge Case Handling**:
- Empty list `[]` vs `null` - JavaScript/JSON safety
- Zero count clearly indicates no RSVPs
- Consistent structure regardless of data presence

**Why This Test Matters**:
- Most common initial state for new events
- Prevents null pointer exceptions in frontend
- Validates boundary condition handling
- Ensures API doesn't break on empty relationships

---

### ✅ Test 4: `test_event_to_dict_with_mocked_rsvps_calculates_counts`

**Function Name**: `test_event_to_dict_with_mocked_rsvps_calculates_counts()`

**Category**: Event Model - Serialization (With Data)

**Purpose**: Validates Event model serialization with RSVPs and ensures accurate attendee filtering.

**What It Tests**:
- ✅ `to_dict()` correctly processes RSVP relationships
- ✅ `rsvp_count` counts **all** RSVPs (total count)
- ✅ `attendees` list only includes `attending=True` user IDs
- ✅ Declined RSVPs excluded from attendees list

**Test Implementation**:
```python
def test_event_to_dict_with_mocked_rsvps_calculates_counts():
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)
    
    # Create mock RSVP objects
    rsvp1 = RSVP(user_id=11, attending=True)   # Attending
    rsvp2 = RSVP(user_id=12, attending=False)  # Not attending
    rsvp3 = RSVP(user_id=13, attending=True)   # Attending
    
    # Create Event with RSVPs
    event = Event(
        id=202,
        title="Exclusive Workshop",
        date=fixed_time,
        rsvps=[rsvp1, rsvp2, rsvp3]
    )
    
    event_dict = event.to_dict()
    
    # Validate counts and filtering
    assert event_dict["rsvp_count"] == 3        # Total RSVPs
    assert event_dict["attendees"] == [11, 13]  # Only attending users
```

**Business Logic Validation**:

```python
# Total RSVP Count (all responses)
rsvp_count = len(event.rsvps)  # 3 (includes True and False)

# Attendees List (only attending=True)
attendees = [rsvp.user_id for rsvp in event.rsvps if rsvp.attending]
# Result: [11, 13]
```

**RSVP Filtering Logic**:

| User ID | Attending Status | Included in `rsvp_count`? | Included in `attendees`? |
|---------|-----------------|--------------------------|-------------------------|
| 11 | `True` | ✅ Yes | ✅ Yes |
| 12 | `False` | ✅ Yes | ❌ No |
| 13 | `True` | ✅ Yes | ✅ Yes |

**Expected Output**:
```python
{
    "id": 202,
    "title": "Exclusive Workshop",
    "date": "2026-06-01T15:30:00",
    "rsvp_count": 3,         # Total responses
    "attendees": [11, 13]    # Only user IDs with attending=True
}
```

**Why This Test Matters**:
- Accurate attendance counting is critical for capacity management
- Prevents overbooking events
- Tests core business logic for event management
- Validates filtering of declined RSVPs
- Ensures attendee list accuracy for event organizers

---

### ✅ Test 5: `test_rsvp_to_dict_conversion`

**Function Name**: `test_rsvp_to_dict_conversion()`

**Category**: RSVP Model - Serialization

**Purpose**: Validates RSVP model serialization ensures proper data mapping.

**What It Tests**:
- ✅ `to_dict()` returns all required RSVP fields
- ✅ Foreign keys (user_id, event_id) preserved
- ✅ Boolean `attending` status correctly included
- ✅ Timestamps properly formatted

**Test Implementation**:
```python
def test_rsvp_to_dict_conversion():
    fixed_time = datetime(2026, 5, 18, 16, 0, 0)
    
    # Create RSVP instance
    rsvp = RSVP(
        id=7,
        event_id=101,
        user_id=11,
        attending=True,
        created_at=fixed_time
    )
    
    rsvp_dict = rsvp.to_dict()
    
    # Validate all fields
    assert rsvp_dict["id"] == 7
    assert rsvp_dict["event_id"] == 101
    assert rsvp_dict["user_id"] == 11
    assert rsvp_dict["attending"] is True
    assert rsvp_dict["created_at"] == "2026-05-18T16:00:00"
```

**Expected Dictionary Output**:
```python
{
    "id": 7,
    "event_id": 101,
    "user_id": 11,
    "attending": True,
    "created_at": "2026-05-18T16:00:00"
}
```

**Field Specifications**:

| Field | Type | Purpose | Notes |
|-------|------|---------|-------|
| `id` | int | Primary key | Auto-generated |
| `event_id` | int | Foreign key | Links to Event |
| `user_id` | int | Foreign key | Links to User |
| `attending` | bool | Status flag | True = attending, False = declined |
| `created_at` | str | Timestamp | ISO 8601 format |

**Relational Integrity**:
- `event_id` → References `Event.id`
- `user_id` → References `User.id`
- Links users to events with attendance status

**Why This Test Matters**:
- RSVPs are the bridge between users and events
- Validates relational data is preserved
- Ensures API responses have consistent RSVP structure
- Critical for displaying attendee lists

---

## 📦 File 3: `test_api.py` - Integration Tests (8 Tests)

**Philosophy**: End-to-end integration tests that validate complete HTTP request/response cycles. Send real HTTP requests to a **running Flask server** on `http://localhost:4000`.

**Prerequisites**: 
- ⚠️ **CRITICAL**: Flask server MUST be running on `localhost:4000`
- Tests will fail if server is not accessible

---

## 🟢 Happy Path Tests (6 Tests)

### ✅ Test 6: `test_health_endpoint_returns_healthy`

**Function Name**: `test_health_endpoint_returns_healthy(base_url)`

**Category**: Integration - Health Check

**Purpose**: Validates basic server connectivity and health status.

**HTTP Request**:
```http
GET http://localhost:4000/api/health
```

**Test Implementation**:
```python
def test_health_endpoint_returns_healthy(base_url):
    response = requests.get(f"{base_url}/api/health")
    assert response.status_code == 200
    assert "healthy" in response.text.lower() or \
           response.json().get("status") == "healthy"
```

**Expected Response** (200 OK):
```json
{
    "status": "healthy"
}
```

**Assertions**:
- ✅ Status code = `200`
- ✅ Response contains "healthy" (case-insensitive) OR
- ✅ Response JSON has `status: "healthy"`

**Why This Test Matters**:
- First test to run - validates server is running
- Confirms basic HTTP infrastructure works
- Used for monitoring and health checks

**Common Failures**:
- ❌ `ConnectionError` - Server not running
- ❌ Wrong port - Server on 5000 instead of 4000

---

### ✅ Test 7: `test_register_user_creates_new_user`

**Function Name**: `test_register_user_creates_new_user(base_url, unique_user_credentials)`

**Category**: Integration - Authentication

**Purpose**: Validates complete user registration workflow.

**Fixtures Used**:
- `base_url` - API endpoint
- `unique_user_credentials` - Generated username with timestamp

**HTTP Request**:
```http
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920123",
    "password": "SecurePassword123"
}
```

**Test Implementation**:
```python
def test_register_user_creates_new_user(base_url, unique_user_credentials):
    response = requests.post(
        f"{base_url}/api/auth/register", 
        json=unique_user_credentials
    )
    assert response.status_code == 201
    assert response.json()["user"]["username"] == \
           unique_user_credentials["username"]
```

**Expected Response** (201 Created):
```json
{
    "message": "User created successfully",
    "user": {
        "id": 1,
        "username": "user_1737283920123",
        "is_admin": false,
        "created_at": "2026-05-19T10:30:00"
    }
}
```

**Assertions**:
- ✅ Status code = `201 Created`
- ✅ Response contains `user` object
- ✅ Username matches the request payload

**Validation Points**:
- User successfully created in database
- Username uniqueness enforced (tested separately)
- Password hashed before storage (unit test validates)
- Response excludes password_hash

**Why This Test Matters**:
- Registration is user entry point
- Validates database write operations
- Tests first step of authentication flow

---

### ✅ Test 8: `test_login_returns_jwt_token`

**Function Name**: `test_login_returns_jwt_token(base_url, unique_user_credentials)`

**Category**: Integration - Authentication

**Purpose**: Validates authentication workflow and JWT token generation.

**Fixtures Used**:
- `base_url` - API endpoint
- `unique_user_credentials` - Fresh user credentials

**Test Flow**:
1. Register a new user (setup)
2. Login with registered credentials
3. Validate JWT token received

**HTTP Requests**:
```http
# Step 1: Register
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920456",
    "password": "SecurePassword123"
}

# Step 2: Login
POST http://localhost:4000/api/auth/login
Content-Type: application/json

{
    "username": "user_1737283920456",
    "password": "SecurePassword123"
}
```

**Test Implementation**:
```python
def test_login_returns_jwt_token(base_url, unique_user_credentials):
    # Register user first
    requests.post(
        f"{base_url}/api/auth/register", 
        json=unique_user_credentials
    )
    
    # Attempt login
    response = requests.post(
        f"{base_url}/api/auth/login", 
        json=unique_user_credentials
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
```

**Expected Response** (200 OK):
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
        "id": 1,
        "username": "user_1737283920456",
        "is_admin": false
    }
}
```

**JWT Token Structure**:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImlhdCI6MTczNzI4MzkyMH0.signature
```
- Part 1: Header (algorithm, token type)
- Part 2: Payload (user ID, issued at, expiration)
- Part 3: Signature (cryptographic verification)

**Assertions**:
- ✅ Status code = `200 OK`
- ✅ Response contains `access_token` field
- ✅ Token is a non-empty string

**Why This Test Matters**:
- JWT tokens enable stateless authentication
- Tests second step of authentication flow
- Validates token generation works correctly

---

### ✅ Test 9: `test_create_public_event_requires_auth_and_succeeds_with_token`

**Function Name**: `test_create_public_event_requires_auth_and_succeeds_with_token(base_url, authenticated_headers)`

**Category**: Integration - Event Management

**Purpose**: Validates authenticated event creation workflow.

**Fixtures Used**:
- `base_url` - API endpoint
- `authenticated_headers` - JWT token headers (auto-setup)

**HTTP Request**:
```http
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Public Networking Event",
    "date": "2026-06-01",
    "is_public": true
}
```

**Test Implementation**:
```python
def test_create_public_event_requires_auth_and_succeeds_with_token(
    base_url, authenticated_headers
):
    event_payload = {
        "title": "Public Networking Event",
        "date": "2026-06-01",
        "is_public": True
    }
    response = requests.post(
        f"{base_url}/api/events", 
        json=event_payload, 
        headers=authenticated_headers
    )
    assert response.status_code == 201
    assert response.json().get("title") == "Public Networking Event"
```

**Expected Response** (201 Created):
```json
{
    "id": 1,
    "title": "Public Networking Event",
    "date": "2026-06-01T00:00:00",
    "is_public": true,
    "requires_admin": false,
    "capacity": null,
    "location": null,
    "description": null,
    "rsvps": [],
    "rsvp_count": 0,
    "attendees": [],
    "created_at": "2026-05-19T10:30:00"
}
```

**Assertions**:
- ✅ Status code = `201 Created`
- ✅ Response title matches request payload

**Authentication Validation**:
- Requires valid JWT token in Authorization header
- Token automatically provided by `authenticated_headers` fixture
- User must be authenticated to create events

**Why This Test Matters**:
- Event creation is core platform feature
- Validates JWT authentication for protected endpoints
- Ensures only authenticated users can create events

---

### ✅ Test 10: `test_rsvp_to_public_event_succeeds_without_auth`

**Function Name**: `test_rsvp_to_public_event_succeeds_without_auth(base_url, authenticated_headers)`

**Category**: Integration - RSVP System

**Purpose**: Validates public events allow RSVPs without authentication.

**Fixtures Used**:
- `base_url` - API endpoint
- `authenticated_headers` - Used only for event creation

**Test Flow**:
1. Create a public event (with auth)
2. RSVP to event (without auth)
3. Validate RSVP succeeds

**HTTP Requests**:
```http
# Step 1: Create Public Event (authenticated)
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Open House",
    "date": "2026-07-01",
    "is_public": true
}

# Step 2: RSVP (NO authentication header)
POST http://localhost:4000/api/rsvps/event/1
Content-Type: application/json

{}
```

**Test Implementation**:
```python
def test_rsvp_to_public_event_succeeds_without_auth(
    base_url, authenticated_headers
):
    # Create public event
    event_payload = {
        "title": "Open House", 
        "date": "2026-07-01", 
        "is_public": True
    }
    create_res = requests.post(
        f"{base_url}/api/events", 
        json=event_payload, 
        headers=authenticated_headers
    )
    event_id = create_res.json().get("id")
    
    # RSVP without authentication
    rsvp_res = requests.post(
        f"{base_url}/api/rsvps/event/{event_id}", 
        json={}
    )
    assert rsvp_res.status_code in [200, 201]
    assert rsvp_res.json().get("event_id") == event_id
```

**Expected Response** (200 OK or 201 Created):
```json
{
    "id": 1,
    "event_id": 1,
    "user_id": null,
    "attending": true,
    "created_at": "2026-05-19T10:30:00"
}
```

**Assertions**:
- ✅ Status code = `200` or `201`
- ✅ Response `event_id` matches created event

**Access Control Validation**:
- Public events (`is_public: true`) allow unauthenticated RSVPs
- No Authorization header required
- Anonymous users can RSVP

**Why This Test Matters**:
- Validates access control differentiates event types
- Ensures public events are truly accessible
- Tests unauthenticated API access paths

---

### ✅ Test 11: `test_get_all_events_returns_list`

**Function Name**: `test_get_all_events_returns_list(base_url)`

**Category**: Integration - Event Retrieval

**Purpose**: Verifies fetching all events returns a properly formatted list.

**HTTP Request**:
```http
GET http://localhost:4000/api/events
```

**Test Implementation**:
```python
def test_get_all_events_returns_list(base_url):
    response = requests.get(f"{base_url}/api/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

**Expected Response** (200 OK):
```json
[
    {
        "id": 1,
        "title": "Tech Conference",
        "date": "2026-06-01T15:30:00",
        "is_public": true,
        ...
    },
    {
        "id": 2,
        "title": "Workshop",
        "date": "2026-06-15T10:00:00",
        "is_public": false,
        ...
    }
]
```

**Assertions**:
- ✅ Status code = `200 OK`
- ✅ Response is a list (array) type
- ✅ Empty list `[]` is valid if no events exist

**Why This Test Matters**:
- Validates list endpoint structure
- Ensures proper JSON array response
- Tests read operations work correctly

---

## 🔴 Error Handling & Edge Case Tests (7 Tests)

### ✅ Test 12: `test_duplicate_username_registration_returns_400`

**Function Name**: `test_duplicate_username_registration_returns_400(base_url, unique_user_credentials)`

**Category**: Integration - Error Handling

**Purpose**: Validates duplicate usernames are properly rejected.

**Test Flow**:
1. Register user (succeeds)
2. Register same username again (fails)

**HTTP Requests**:
```http
# First Registration (succeeds)
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920789",
    "password": "SecurePassword123"
}

# Second Registration (fails)
POST http://localhost:4000/api/auth/register
Content-Type: application/json

{
    "username": "user_1737283920789",
    "password": "SecurePassword123"
}
```

**Test Implementation**:
```python
def test_duplicate_username_registration_returns_400(
    base_url, unique_user_credentials
):
    # First registration succeeds
    res1 = requests.post(
        f"{base_url}/api/auth/register", 
        json=unique_user_credentials
    )
    assert res1.status_code == 201
    
    # Second registration fails
    res2 = requests.post(
        f"{base_url}/api/auth/register", 
        json=unique_user_credentials
    )
    assert res2.status_code == 400
```

**Expected Error Response** (400 Bad Request):
```json
{
    "error": "Username already exists",
    "message": "A user with this username is already registered"
}
```

**Assertions**:
- ✅ First registration: Status = `201 Created`
- ✅ Second registration: Status = `400 Bad Request`

**Why This Test Matters**:
- Validates username uniqueness constraint
- Tests error handling for constraint violations
- Prevents account conflicts

---

### ✅ Test 13: `test_create_event_without_auth_returns_401`

**Function Name**: `test_create_event_without_auth_returns_401(base_url)`

**Category**: Integration - Security

**Purpose**: Validates event creation requires authentication.

**HTTP Request**:
```http
POST http://localhost:4000/api/events
Content-Type: application/json
# NOTE: No Authorization header

{
    "title": "Secret Event",
    "date": "2026-08-01",
    "is_public": true
}
```

**Test Implementation**:
```python
def test_create_event_without_auth_returns_401(base_url):
    event_payload = {
        "title": "Secret Event", 
        "date": "2026-08-01", 
        "is_public": True
    }
    response = requests.post(
        f"{base_url}/api/events", 
        json=event_payload
    )  # No headers sent
    assert response.status_code == 401
```

**Expected Error Response** (401 Unauthorized):
```json
{
    "msg": "Missing Authorization Header"
}
```

**Assertions**:
- ✅ Status code = `401 Unauthorized`
- ✅ Event NOT created

**Why This Test Matters**:
- Validates authentication is enforced
- Prevents unauthorized event creation
- Tests security boundary enforcement

---

### ✅ Test 14: `test_rsvp_to_non_public_event_without_auth_returns_error`

**Function Name**: `test_rsvp_to_non_public_event_without_auth_returns_error(base_url, authenticated_headers)`

**Category**: Integration - Access Control

**Purpose**: Validates protected events reject unauthenticated RSVPs.

**Test Flow**:
1. Create private event (with auth)
2. RSVP to private event (without auth)
3. Validate rejection

**HTTP Requests**:
```http
# Step 1: Create Private Event
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "title": "Private Board Meeting",
    "date": "2026-09-01",
    "is_public": false
}

# Step 2: RSVP without auth (should fail)
POST http://localhost:4000/api/rsvps/event/1
Content-Type: application/json

{}
```

**Test Implementation**:
```python
def test_rsvp_to_non_public_event_without_auth_returns_error(
    base_url, authenticated_headers
):
    # Create private event
    event_payload = {
        "title": "Private Board Meeting", 
        "date": "2026-09-01", 
        "is_public": False
    }
    create_res = requests.post(
        f"{base_url}/api/events", 
        json=event_payload, 
        headers=authenticated_headers
    )
    event_id = create_res.json().get("id")
    
    # Attempt RSVP without auth
    rsvp_res = requests.post(
        f"{base_url}/api/rsvps/event/{event_id}", 
        json={}
    )
    assert rsvp_res.status_code in [401, 403, 404]
```

**Possible Error Responses**:
```json
// 401 Unauthorized
{
    "msg": "Missing Authorization Header"
}

// 403 Forbidden
{
    "error": "Access denied",
    "message": "This event requires authentication"
}

// 404 Not Found (if event hidden from unauthenticated users)
{
    "error": "Event not found"
}
```

**Assertions**:
- ✅ Status code = `401`, `403`, or `404`
- ✅ RSVP NOT created

**Access Control Matrix**:

| Event Type | `is_public` | RSVP Auth Required? |
|------------|-------------|---------------------|
| Public | `true` | No |
| Protected | `false` | Yes |

**Why This Test Matters**:
- Validates role-based access control
- Ensures private events remain private
- Tests multi-level authorization logic

---

### ✅ Test 15: `test_get_invalid_event_id_returns_404`

**Function Name**: `test_get_invalid_event_id_returns_404(base_url)`

**Category**: Integration - Error Handling

**Purpose**: Validates requesting non-existent events returns 404.

**HTTP Request**:
```http
GET http://localhost:4000/api/events/999999
```

**Test Implementation**:
```python
def test_get_invalid_event_id_returns_404(base_url):
    invalid_id = 999999
    response = requests.get(f"{base_url}/api/events/{invalid_id}")
    assert response.status_code == 404
```

**Expected Response** (404 Not Found):
```json
{
    "error": "Event not found",
    "message": "No event exists with ID 999999"
}
```

**Assertions**:
- ✅ Status code = `404 Not Found`

**Why This Test Matters**:
- Validates proper HTTP status for missing resources
- Tests error handling for invalid IDs

---

### ✅ Test 16: `test_create_event_with_missing_required_fields_returns_400`

**Function Name**: `test_create_event_with_missing_required_fields_returns_400(base_url, authenticated_headers)`

**Category**: Integration - Input Validation

**Purpose**: Validates event creation requires all mandatory fields.

**HTTP Request**:
```http
POST http://localhost:4000/api/events
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "date": "2026-12-01T12:00:00",
    "is_public": true
    // Missing "title" field
}
```

**Test Implementation**:
```python
def test_create_event_with_missing_required_fields_returns_400(
    base_url, authenticated_headers
):
    incomplete_payload = {
        "date": "2026-12-01T12:00:00",
        "is_public": True
        # Missing "title"
    }
    response = requests.post(
        f"{base_url}/api/events", 
        json=incomplete_payload, 
        headers=authenticated_headers
    )
    assert response.status_code == 400
```

**Expected Response** (400 Bad Request):
```json
{
    "error": "Validation error",
    "message": "Missing required field: title"
}
```

**Assertions**:
- ✅ Status code = `400 Bad Request`
- ✅ Event NOT created

**Why This Test Matters**:
- Validates input validation works
- Ensures data integrity
- Tests required field enforcement

---

### ✅ Test 17: `test_rsvp_to_non_existent_event_returns_404`

**Function Name**: `test_rsvp_to_non_existent_event_returns_404(base_url, authenticated_headers)`

**Category**: Integration - Error Handling

**Purpose**: Validates RSVPing to non-existent events returns 404.

**HTTP Request**:
```http
POST http://localhost:4000/api/rsvps/event/888888
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
    "attending": true
}
```

**Test Implementation**:
```python
def test_rsvp_to_non_existent_event_returns_404(
    base_url, authenticated_headers
):
    invalid_event_id = 888888
    response = requests.post(
        f"{base_url}/api/rsvps/event/{invalid_event_id}", 
        json={"attending": True}, 
        headers=authenticated_headers
    )
    assert response.status_code == 404
```

**Expected Response** (404 Not Found):
```json
{
    "error": "Event not found",
    "message": "Cannot RSVP to non-existent event"
}
```

**Assertions**:
- ✅ Status code = `404 Not Found`
- ✅ RSVP NOT created

**Why This Test Matters**:
- Validates referential integrity
- Tests error handling for invalid foreign keys

---

## 🚀 Running the Complete Test Suite

### Prerequisites

1. **Server MUST be running** on port 4000
2. Virtual environment activated
3. Dependencies installed

### Step-by-Step Guide

#### Step 1: Start the Flask Server

**Terminal 1:**
```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Start server
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:4000
```

⚠️ **Wait for this output before proceeding**

#### Step 2: Run Tests

**Terminal 2:**
```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Run all tests
pytest
```

### Test Execution Commands

| Command | Purpose |
|---------|---------|
| `pytest` | Run all tests (minimal output) |
| `pytest -v` | Verbose output with test names |
| `pytest -v -s` | Verbose + show print statements |
| `pytest tests/test_models.py` | Run only unit tests |
| `pytest tests/test_api.py` | Run only integration tests |
| `pytest tests/test_api.py::test_health_endpoint_returns_healthy -v` | Run specific test |
| `pytest --cov=. --cov-report=html` | Generate coverage report |
| `pytest -x` | Stop at first failure |
| `pytest -k "auth"` | Run tests matching "auth" |

### Expected Output

**Successful Run:**
```
========================= test session starts ==========================
platform win32 -- Python 3.11.0, pytest-7.4.0, pluggy-1.0.0
rootdir: C:\projects\evently-api
collected 13 items

tests/test_models.py .....                                      [ 38%]
tests/test_api.py ........                                      [100%]

========================= 13 passed in 5.23s ===========================
```

**Test Breakdown:**
- ✅ 5 Unit Tests (test_models.py)
- ✅ 8 Integration Tests (test_api.py)
- ✅ **Total: 13 tests**

### Troubleshooting

#### ❌ Connection Refused
```
requests.exceptions.ConnectionError
```
**Solution**: Start Flask server first

#### ❌ Wrong Port
```
Connection refused at localhost:5000
```
**Solution**: Verify server runs on port 4000

#### ❌ Import Errors
```
ModuleNotFoundError: No module named 'pytest'
```
**Solution**: 
```bash
pip install -r requirements.txt
```

---

## 📊 Test Coverage Summary

| Category | Count | Percentage |
|----------|-------|------------|
| **Unit Tests** | 5 | 38% |
| **Integration (Happy)** | 6 | 46% |
| **Integration (Error)** | 7 | 54% |
| **Total Tests** | **13** | **100%** |

### Coverage by Feature

| Feature | Tests | Coverage |
|---------|-------|----------|
| **Authentication** | 4 | Registration, Login, JWT, Duplicates |
| **Event Management** | 5 | Create, List, Get, Validation |
| **RSVP System** | 3 | Public RSVP, Private RSVP, Validation |
| **Access Control** | 2 | Auth Required, Public Access |
| **Error Handling** | 4 | 404s, 400s, 401s |

---

## 📖 API Reference

### Base URL
```
http://localhost:4000
```

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
    "username": "newuser",
    "password": "SecurePass123"
}
```

**Response (201):**
```json
{
    "message": "User created successfully",
    "user": {
        "id": 1,
        "username": "newuser",
        "is_admin": false
    }
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
    "username": "newuser",
    "password": "SecurePass123"
}
```

**Response (200):**
```json
{
    "access_token": "eyJhbGc...",
    "user": { ... }
}
```

### Event Endpoints

#### Get All Events
```http
GET /api/events
```

#### Get Event by ID
```http
GET /api/events/{event_id}
```

#### Create Event (Protected)
```http
POST /api/events
Authorization: Bearer {token}
Content-Type: application/json

{
    "title": "My Event",
    "date": "2026-06-01",
    "is_public": true
}
```

### RSVP Endpoints

#### RSVP to Event
```http
POST /api/rsvps/event/{event_id}
Content-Type: application/json

{
    "attending": true
}
```

---

## 🔐 Security Considerations

### Current Features
- ✅ Password hashing (werkzeug)
- ✅ JWT authentication
- ✅ Role-based access control
- ✅ SQLAlchemy ORM

### Recommended Improvements
- 🔄 Bcrypt/Argon2 password hashing
- 🔄 JWT refresh tokens
- 🔄 Rate limiting
- 🔄 Input validation
- 🔄 HTTPS enforcement
- 🔄 Logging & monitoring

⚠️ **Educational project - not production-ready**

---

## 📄 License

MIT License

---

**Made with ❤️ for learning web development and security**


# Evently API

A Flask-based REST API for managing events and RSVPs with different access levels. This API is designed to teach web security best practices through incremental improvements.

## Features

- **Public Events**: Anyone can RSVP without authentication
- **Protected Events**: Requires user authentication to RSVP
- **Admin Events**: Requires admin role to RSVP

## Tech Stack

- Flask 3.0.0
- Flask-SQLAlchemy (SQLite database)
- Flask-CORS
- Flask-JWT-Extended (JWT authentication)
- Pytest & Requests (Testing Suite)

## Setup

1. Create and activate a virtual environment:

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Automated Testing Suite

The project includes a robust automated test architecture structured using `pytest`. The test environment contains pure unit tests for database models and end-to-end integration tests targeting a running server.

### Full Project Layout
```
.
├── README.md
├── app.py
├── config.py
├── instance
│   └── events.db
├── models.py
├── openapi.yaml
├── requirements.txt
├── routes
│   ├── __init__.py
│   ├── auth.py
│   ├── events.py
│   └── rsvps.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_api.py
    └── test_models.py
```

### Test Directory Layout
```text
tests/
├── __init__.py
├── conftest.py          # Global configurations, fixtures, and automatic auth tokens
├── test_models.py       # Isolated Unit Tests (pure Python execution logic, no DB, no HTTP)
└── test_api.py          # Server Integration Tests (E2E flows targeting live endpoints)
```

### Detailed Test Specifications

#### 1. Unit Tests (`tests/test_models.py`)
These tests process pure database model logic inside transient memory. They do not run a server or persist data to a database file.
*   `test_user_password_hashing_behaves_correctly`: Verifies that `set_password` securely hashes string text and `check_password` validates credentials accurately using `werkzeug`.
*   `test_user_to_dict_conversion`: Ensures user model components serialize correctly to dictionaries with properly formatted ISO timestamps.
*   `test_event_to_dict_empty_rsvps`: Confirms that events without attendees gracefully export an empty attendee tracking list.
*   `test_event_to_dict_with_mocked_rsvps_calculates_counts`: Mocks relational `RSVP` memory entities to verify that `rsvp_count` filters active attendees accurately.
*   `test_rsvp_to_dict_conversion`: Assures properties map seamlessly inside the RSVP data schema framework.

#### 2. Integration Tests: Happy Paths (`tests/test_api.py`)
These tests send HTTP requests to the running backend to assert valid actions.
*   `test_health_endpoint_returns_healthy`: Contacts the root health node to ensure server responsiveness.
*   `test_register_user_creates_new_user`: Sends data to `/api/auth/register` with dynamic, timestamped usernames to ensure clean account instantiation.
*   `test_login_returns_jwt_token`: Contacts `/api/auth/login` with newly registered records to extract valid JWT tokens.
*   `test_create_public_event_requires_auth_and_succeeds_with_token`: Asserts authorized payloads successfully build new entries at `POST /api/events`.
*   `test_rsvp_to_public_event_succeeds_without_auth`: Tracks open public gatherings to ensure anyone can seamlessly opt-in without an explicit token.
*   `test_get_all_events_returns_list`: Hits the core event retrieval node to verify data is successfully delivered inside a valid JSON list array.

#### 3. Integration Tests: Edge Cases & Error Conditions (`tests/test_api.py`)
These tests check robustness by intentionally feeding bad data or bypassing rules.
*   `test_duplicate_username_registration_returns_400`: Asserts that trying to use an identical username twice halts duplication workflows with an explicit HTTP 400 response.
*   `test_create_event_without_auth_returns_401`: Guarantees unauthenticated requests attempting to write an event to `POST /api/events` are rejected with a 401 status code.
*   `test_create_event_with_missing_required_fields_returns_400`: Intentionally leaves out vital structural parameters (like `title`) to force structural validation failures.
*   `test_rsvp_to_non_public_event_without_auth_returns_error`: Protects private gatherings from unverified users, checking for error handling defaults.
*   `test_rsvp_to_non_existent_event_returns_404`: Attaches attendance records to invalid event ID paths to check for database resource handling responses.
*   `test_get_invalid_event_id_returns_404`: Requests missing records from the backend to ensure route lookups fail gracefully with an HTTP 404 status.


### Running the Test Runner Suite
Your local development server must be running to process the integration tests.

1. **Fire up the backend server** in your first terminal workspace:
   ```bash
   python app.py
   ```
2. **Execute the test collection utility** inside a separate, active terminal tab:
   ```bash
   pytest
   ```

## Swagger UI Documentation

The API includes interactive Swagger UI documentation. After starting the server:

1. Open your browser and navigate to: `http://localhost:5000/apidocs`

2. You'll see an interactive API documentation interface where you can:
   - Browse all available endpoints
   - See request/response schemas
   - Test endpoints directly from the browser
   - Authenticate using the "Authorize" button (enter your JWT token)

3. To use the "Authorize" button:
   - First, login via `/api/auth/login` to get your JWT token
   - Click the "Authorize" button at the top of the Swagger UI
   - Enter: `Bearer <your_jwt_token>` (replace `<your_jwt_token>` with your actual token)
   - Now you can test protected endpoints directly from Swagger UI

**Alternative**: You can also view the OpenAPI specification directly at `http://localhost:5000/apispec_1.json`

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register a new user
  ```json
  {
    "username": "user123",
    "password": "password123"
  }
  ```

- `POST /api/auth/login` - Login and get JWT token
  ```json
  {
    "username": "user123",
    "password": "password123"
  }
  ```

### Events

- `GET /api/events` - Get all events
- `GET /api/events/<id>` - Get a specific event
- `POST /api/events` - Create a new event (requires authentication)
  ```json
  {
    "title": "Python Meetup",
    "description": "Monthly Python developer meetup",
    "date": "2026-01-15T18:00:00",
    "location": "Tech Hub, Room 101",
    "capacity": 50,
    "is_public": true,
    "requires_admin": false
  }
  ```

### RSVPs

- `POST /api/rsvps/event/<event_id>` - RSVP to an event
  ```json
  {
    "attending": true
  }
  ```

- `GET /api/rsvps/event/<event_id>` - Get all RSVPs for an event

## Authentication

For protected endpoints, include the JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Security Notes

This is a basic implementation designed for educational purposes. The following security considerations are intentionally simplified and can be improved in subsequent lessons:

- Password storage (currently using werkzeug, but can be improved)
- JWT token handling
- Input validation
- SQL injection prevention (SQLAlchemy helps, but can be improved)
- Rate limiting
- CORS configuration
- Error handling and information disclosure

## Database

The application uses SQLite by default. The database file (`events.db`) will be created automatically on first run.

**Note**: The first user registered automatically becomes an admin for demo purposes.

