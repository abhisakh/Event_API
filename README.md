# 🎉 Evently API - Complete Project Documentation

A Flask-based REST API for managing events and RSVPs with role-based access control. This educational project demonstrates REST API design, JWT authentication, database modeling, and comprehensive testing practices.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Tests](https://img.shields.io/badge/Tests-13%20Passing-brightgreen.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Quick Navigation

- [Project Structure](#-project-structure)
- [Docker Files Explanation](#-docker-files-explanation)
- [Getting Started](#-getting-started)
- [Database Models](#-database-models)
- [API Reference](#-api-reference)
- [Test Suite](#-test-suite)
- [Designing New Tests](#-designing-new-tests)

---

## 📁 Project Structure

```
evently-api/
├── README.md                    # Project documentation
├── Dockerfile                   # Docker image configuration (Python 3.9-slim)
├── docker-compose.yml           # Docker Compose configuration (build & run)
├── app.py                       # Flask application factory & initialization
├── config.py                    # Configuration (secrets, database, JWT settings)
├── models.py                    # SQLAlchemy models (User, Event, RSVP)
├── openapi.yaml                 # OpenAPI 3.0 specification
├── requirements.txt             # Python dependencies (Flask, SQLAlchemy, etc.)
│
├── instance/
│   └── events.db                # SQLite database (auto-created on first run)
│
├── routes/                      # API Blueprint modules (organize endpoints)
│   ├── __init__.py              # Package initializer (empty)
│   ├── auth.py                  # Authentication (POST /api/auth/register, /api/auth/login)
│   ├── events.py                # Event management (GET/POST /api/events, GET /api/events/{id})
│   └── rsvps.py                 # RSVP management (POST/GET /api/rsvps/event/{id})
│
└── tests/                       # Automated test suite (13 tests total)
    ├── __init__.py              # Package initializer (empty)
    ├── conftest.py              # Pytest configuration & shared fixtures
    ├── test_models.py           # Unit tests (5 tests) - Pure Python, no I/O
    └── test_api.py              # Integration tests (8 tests) - HTTP E2E
```

### Root Level Files

| File | Purpose | Details |
|------|---------|---------|
| `README.md` | Project documentation | Comprehensive guide for setup, usage, and testing |
| `Dockerfile` | Docker image blueprint | Defines how to build the application container |
| `docker-compose.yml` | Container orchestration | Configures port mapping, volumes, and environment |
| `app.py` | Flask application | Entry point for the API server |
| `config.py` | Configuration settings | Database URI, JWT secrets, token expiration |
| `models.py` | Database models | User, Event, RSVP SQLAlchemy classes |
| `openapi.yaml` | API specification | OpenAPI 3.0 spec for Swagger UI |
| `requirements.txt` | Python dependencies | All pip packages needed to run |

### File Responsibilities

| File | Purpose | Key Components |
|------|---------|-----------------|
| `app.py` | Application factory | `create_app()`, blueprint registration, JWT init |
| `config.py` | Settings & secrets | `SECRET_KEY`, `JWT_SECRET_KEY`, database URI, token expiration |
| `models.py` | Database models | `User`, `Event`, `RSVP` classes with relationships |
| `routes/auth.py` | Authentication | `/register` (POST), `/login` (POST) |
| `routes/events.py` | Event CRUD | `/events` (GET, POST), `/events/{id}` (GET) |
| `routes/rsvps.py` | RSVP system | `/rsvps/event/{id}` (POST, GET) with access control |
| `tests/conftest.py` | Test fixtures | `base_url`, `unique_user_credentials`, `authenticated_headers` |
| `tests/test_models.py` | Unit tests | 5 database model tests (password, serialization, counting) |
| `tests/test_api.py` | Integration tests | 8 HTTP endpoint tests (happy paths + error cases) |

### Docker Files Explanation

#### Dockerfile

The `Dockerfile` at the root directory contains:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python", "app.py"]
```

**Purpose**: Defines the blueprint for building a Docker image that:
- Uses Python 3.9-slim as the lightweight base image
- Installs all Python dependencies from requirements.txt
- Copies the entire application to `/app` directory
- Exposes port 4000 for the Flask API
- Runs the application with `python app.py`

#### docker-compose.yml

The `docker-compose.yml` at the root directory contains:
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "4000:4000"
    environment:
      - FLASK_APP=app.py
      - FLASK_RUN_PORT=4000
    volumes:
      - .:/app
    command: python app.py
```

**Purpose**: Orchestrates the Docker container with:
- Automatic image building from Dockerfile
- Port mapping (container 4000 → local 4000)
- Environment variables for Flask configuration
- Volume mounting for live code reloading during development
- Container startup command

---

### Directory Structure Details

```
instance/
└── events.db                    # SQLite database file
                                 # Auto-created by Flask-SQLAlchemy
                                 # Contains: user, event, rsvp tables
                                 # Remove to reset database

routes/                          # API route blueprints
├── __init__.py                 # Empty - marks as Python package
├── auth.py                     # Handles /api/auth/* endpoints
                                # - User registration
                                # - User login with JWT generation
                                # - Password hashing/verification
│
├── events.py                   # Handles /api/events/* endpoints
                                # - List all events (GET /api/events)
                                # - Create event (POST /api/events) - requires auth
                                # - Get event by ID (GET /api/events/{id})
                                # - Date parsing & validation
│
└── rsvps.py                    # Handles /api/rsvps/* endpoints
                                # - Create/update RSVP (POST /api/rsvps/event/{id})
                                # - Get event RSVPs (GET /api/rsvps/event/{id})
                                # - Access control (public/protected/admin events)
                                # - Capacity checking

tests/                          # Test suite (13 tests)
├── __init__.py                 # Empty - marks as Python package
├── conftest.py                 # Shared pytest configuration
                                # - Fixtures for all tests
                                # - Base URL configuration (http://localhost:4000)
                                # - Unique user generation (timestamp-based)
                                # - JWT token creation
│
├── test_models.py              # Unit tests (5 tests)
                                # - test_user_password_hashing_behaves_correctly
                                # - test_user_to_dict_conversion
                                # - test_event_to_dict_empty_rsvps
                                # - test_event_to_dict_with_mocked_rsvps_calculates_counts
                                # - test_rsvp_to_dict_conversion
│
└── test_api.py                 # Integration tests (8 tests)
                                # Happy Path Tests (6):
                                # - test_health_endpoint_returns_healthy
                                # - test_register_user_creates_new_user
                                # - test_login_returns_jwt_token
                                # - test_create_public_event_requires_auth_and_succeeds_with_token
                                # - test_rsvp_to_public_event_succeeds_without_auth
                                # - test_get_all_events_returns_list
                                #
                                # Error Handling Tests (7):
                                # - test_duplicate_username_registration_returns_400
                                # - test_create_event_without_auth_returns_401
                                # - test_rsvp_to_non_public_event_without_auth_returns_error
                                # - test_get_invalid_event_id_returns_404
                                # - test_create_event_with_missing_required_fields_returns_400
                                # - test_rsvp_to_non_existent_event_returns_404
```

---

## 🐳 Docker Setup & Usage Guide

### 1. Local Setup and Build

Use these commands to build your image and start the container locally using Docker Compose.

**Build and Start:**
```bash
docker compose up -d --build
```

**Check Status:**
```bash
docker ps
```

**Access API:**
Open `http://localhost:4000/events` in your browser.

---

### 2. Pushing to Docker Hub

To share your image, you must tag it and push it to your repository.

**Login:**
```bash
docker login
```

**Tag Version:**
```bash
docker tag abhisakh/events-api:latest abhisakh/events-api:v1.0
```

**Push Image:**
```bash
docker push abhisakh/events-api:v1.0
```

---

### 3. Pulling and Running from Registry

If you are on a new machine, you can pull the image directly without the source code.

**Pull Image:**
```bash
docker pull abhisakh/events-api:latest
```

**Run Container:**
```bash
docker run -d -p 4000:4000 --name events-container abhisakh/events-api:latest
```

---

### 4. Testing the Docker Container

Once the container is running, verify the setup with these tests.

**Health Check:**
```bash
curl http://localhost:4000/api/health
```

**Run Integration Tests:**
```bash
pytest -v
```
*(Ensure the container is "Up" first)*

**View Internal Logs:**
```bash
docker logs -f events-container
```

---

### 5. Management Tips

**Stop Project:**
```bash
docker compose stop
```

**Full Cleanup:**
```bash
docker compose down
```

**Inspect Files:**
Use the Files tab in Docker Desktop to see the `/app` directory.

---

## 🐳 Docker Configuration

### Dockerfile

The `Dockerfile` is the blueprint for your application environment. It ensures that every instance of the app runs with the exact same dependencies and settings.

**Key Features:**
- **Base Image**: Uses `python:3.9-slim` to provide a lightweight and efficient runtime
- **Automation**: Handles the installation of all libraries from `requirements.txt` automatically
- **Portability**: Packages the source code so it can run on any system with Docker installed

**Typical Dockerfile Structure:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python", "app.py"]
```

---

### docker-compose.yml

This file acts as the control panel for your container. It defines how the image interacts with your computer's hardware and network.

**Key Features:**
- **One-Command Setup**: Allows you to build and start the entire project using `docker compose up -d`
- **Port Mapping**: Bridges the container to your local machine (e.g., `4000:4000`) so the API is accessible at `localhost`
- **Environment Control**: Sets critical Flask variables like `FLASK_APP` and `FLASK_RUN_PORT` dynamically

**Typical docker-compose.yml Structure:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "4000:4000"
    environment:
      - FLASK_APP=app.py
      - FLASK_RUN_PORT=4000
    volumes:
      - .:/app
    command: python app.py
```

---

## 🚀 Usage Instructions

### Local Development

To build and run the project locally for the first time:

```bash
docker compose up -d --build
```

**Access the API:**
- Browser: `http://localhost:4000/events`
- Health Check: `http://localhost:4000/api/health`

**Run Tests:**
```bash
# Ensure the container is active, then run
pytest -v
```

---

### Deployment & Distribution

To share your image with others via Docker Hub:

1. **Login to Docker Hub:**
   ```bash
   docker login
   ```

2. **Tag Your Image:**
   ```bash
   docker tag abhisakh/events-api:latest abhisakh/events-api:v1.0
   ```

3. **Push to Registry:**
   ```bash
   docker push abhisakh/events-api:v1.0
   ```

---

### Running from the Cloud

To run the project on a new machine without the source code:

```bash
# Pull the image from Docker Hub
docker pull abhisakh/events-api:latest

# Run the container
docker run -d -p 4000:4000 --name events-container abhisakh/events-api:latest
```

**Verify It's Running:**
```bash
curl http://localhost:4000/api/health
```

---

### 🛠 Troubleshooting & Management

| Task | Command |
|------|---------|
| Stop the App | `docker compose stop` |
| Remove Container | `docker compose down` |
| View Logs | `docker compose logs -f` |
| Inspect Files | Use Files tab in Docker Desktop |
| Rebuild Image | `docker compose up -d --build` |
| Full Reset | `docker compose down -v` (removes volumes) |

**View Container Status:**
```bash
docker ps
```

**Check Container Details:**
```bash
docker inspect events-container
```

---

## 🚀 Getting Started

### Installation

```bash
git clone <repository-url>
cd evently-api

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Run Server

```bash
python app.py
# Server at http://localhost:4000
```

### Run Tests

```bash
# Terminal 1: python app.py (keep running)
# Terminal 2:
pytest -v
```

---

## 📦 conftest.py - Test Configuration & Fixtures

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
    "username": "user_1737283920123",
    "password": "SecurePassword123"
}
```

**Implementation**:
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
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.payload.signature
```
- Prefix: `"Bearer "` (note the space)
- Token: JWT with header, payload, and signature
- Valid until expiration (1 hour, configurable in config.py)

**JWT Claims**:
```python
{
    "sub": user_id,          # Subject (user ID as string)
    "iat": issued_timestamp, # Issued at time
    "exp": expiration_time,  # Expiration time (1 hour later)
    "is_admin": True/False   # Admin flag from user record
}
```

---

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
    
    # Raw password text is never exposed explicitly
    assert user.password_hash != "SecureSecretPass123!"
    
    assert user.check_password("SecureSecretPass123!") is True
    
    # Assert wrong password verification correctly fails
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

**Purpose**: Validates dictionary output matching the expected layout framework structure.

**What It Tests**:
- ✅ `to_dict()` method returns all required fields
- ✅ Timestamps are ISO 8601 formatted strings
- ✅ No sensitive data (password_hash) in output
- ✅ Boolean and integer types preserved

**Test Implementation**:
```python
def test_user_to_dict_conversion():
    """Unit Test: Validates dictionary output matching the expected layout framework structure."""
    fixed_time = datetime(2026, 5, 18, 12, 0, 0)

    user = User(
        id=42,
        username="admin_guy",
        is_admin=True,
        created_at=fixed_time
    )

    user_dict = user.to_dict()

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

**Purpose**: Validates event dictionary exports correctly when there are zero attendees.

**What It Tests**:
- ✅ `to_dict()` handles zero RSVPs gracefully
- ✅ Returns empty list for `attendees` (not null)
- ✅ `rsvp_count` correctly calculates as 0
- ✅ All event metadata fields included

**Test Implementation**:
```python
def test_event_to_dict_empty_rsvps():
    """Unit Test: Validates event dictionary exports correctly when there are zero attendees."""
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)

    event = Event(
        id=101,
        title= "Tech Conference",
        description="A great developer meetup",
        date=fixed_time,
        location="Room A",
        capacity=100,
        is_public=True,
        requires_admin=False,
        created_by=42,
        created_at=fixed_time,
        rsvps=[] # Explicitly pass empty list to mock relationship
    )

    event_dict = event.to_dict()

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

**Purpose**: Validates tracking calculations for event RSVPs without interacting with DB engines.

**What It Tests**:
- ✅ `to_dict()` correctly processes RSVP relationships
- ✅ `rsvp_count` counts **all** RSVPs (total count)
- ✅ `attendees` list only includes `attending=True` user IDs
- ✅ Declined RSVPs excluded from attendees list

**Test Implementation**:
```python
def test_event_to_dict_with_mocked_rsvps_calculates_counts():
    """Unit Test: Validates tracking calculations for event RSVPs without interacting with DB engines."""
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)

    # simulate relationship tables
    rsvp1 = RSVP(user_id=11, attending=True)
    rsvp2 = RSVP(user_id=12, attending=False) # Not attending, shouldn't show in user list
    rsvp3 = RSVP(user_id=13, attending=True)

    event = Event(
        id=202,
        title="Exclusive Workshop",
        date=fixed_time,
        rsvps=[rsvp1, rsvp2, rsvp3]
    )

    event_dict = event.to_dict()

    # Total linked records counted
    assert event_dict["rsvp_count"] == 3

    # Only active, attending user IDs filtered out into final listing array
    assert event_dict["attendees"] == [11, 13]
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

**Purpose**: Validates RSVP properties populate dictionary mapping arrays cleanly.

**What It Tests**:
- ✅ `to_dict()` returns all required RSVP fields
- ✅ Foreign keys (user_id, event_id) preserved
- ✅ Boolean `attending` status correctly included
- ✅ Timestamps properly formatted

**Test Implementation**:
```python
def test_rsvp_to_dict_conversion():
    """Unit Test: Validates RSVP properties populate dictionary mapping arrays cleanly."""
    fixed_time = datetime(2026, 5, 18, 16, 0, 0)

    rsvp = RSVP(
        id=7,
        event_id=101,
        user_id=11,
        attending=True,
        created_at=fixed_time
    )

    rsvp_dict = rsvp.to_dict()

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

**Purpose**: Check server running health status.

**What It Tests**:
- ✅ Server is running and accessible
- ✅ Health endpoint responds with 200 status
- ✅ Response contains "healthy" indicator

**HTTP Request**:
```http
GET http://localhost:4000/api/health
```

**Test Implementation**:
```python
def test_health_endpoint_returns_healthy(base_url):
    """Happy Path 1: Check server running health status."""
    response = requests.get(f"{base_url}/api/health")
    assert response.status_code == 200
    assert "healthy" in response.text.lower() or response.json().get("status") == "healthy"
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

**Purpose**: Register a user with a unique timestamped name.

**What It Tests**:
- ✅ User registration succeeds
- ✅ Returns 201 Created status
- ✅ User object included in response
- ✅ Username matches request payload

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
    """Happy Path 2: Register a user with a unique timestamped name."""
    response = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert response.status_code == 201
    assert response.json()["user"]["username"] == unique_user_credentials["username"]
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

**Purpose**: Log in with known user and retrieve a JWT.

**What It Tests**:
- ✅ Login endpoint works with valid credentials
- ✅ Returns 200 OK status
- ✅ Response contains JWT access_token
- ✅ User object returned with token

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
    """Happy Path 3: Log in with known user and retrieve a JWT."""
    # Register the user first
    requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)

    # Attempt login
    response = requests.post(f"{base_url}/api/auth/login", json=unique_user_credentials)
    assert response.status_code == 200
    assert "access_token" in response.json()
```

**Expected Response** (200 OK):
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzI4MzkyMCwianRpIjoiYWJjMTIzIiwibmJmIjoxNzM3MjgzOTIwLCJzdWIiOjEsInR5cGUiOiJhY2Nlc3MifQ.signature",
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

**Purpose**: Call POST /events with a valid JWT payload.

**What It Tests**:
- ✅ Event creation with JWT authentication works
- ✅ Returns 201 Created status
- ✅ Event data correctly persisted
- ✅ All event fields in response

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

**Purpose**: Create a public event first, then RSVP without any auth token.

**What It Tests**:
- ✅ Public events allow unauthenticated RSVPs
- ✅ Returns 200/201 status
- ✅ RSVP created with correct event_id
- ✅ No authentication required for public events

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

**Purpose**: Verifies that fetching all events returns a 200 OK and a list layout.

**What It Tests**:
- ✅ GET /api/events returns 200 OK status
- ✅ Response is a list (array) type
- ✅ Empty list valid if no events exist

**HTTP Request**:
```http
GET http://localhost:4000/api/events
```

**Test Implementation**:
```python
def test_get_all_events_returns_list(base_url):
    """Happy Path: Verifies that fetching all events returns a 200 OK and a list layout."""
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

**Purpose**: Registering duplicate username returns a bad request error.

**What It Tests**:
- ✅ First registration succeeds
- ✅ Duplicate username properly rejected
- ✅ Returns 400 Bad Request status
- ✅ Database constraint enforced

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
def test_duplicate_username_registration_returns_400(base_url, unique_user_credentials):
    """Edge Case 1: Registering duplicate username returns a bad request error."""
    # First registration succeeds
    res1 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
    assert res1.status_code == 201

    # Second registration with exact same username fails
    res2 = requests.post(f"{base_url}/api/auth/register", json=unique_user_credentials)
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

**Purpose**: Attempting to create an event with no token returns 401 Unauthorized.

**What It Tests**:
- ✅ Event creation requires authentication
- ✅ Missing token returns 401 Unauthorized status
- ✅ Event NOT created without auth

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
    """Edge Case 2: Attempting to create an event with no token returns 401 Unauthorized."""
    event_payload = {"title": "Secret Event", "date": "2026-08-01", "is_public": True}
    response = requests.post(f"{base_url}/api/events", json=event_payload) # No headers sent
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

**Purpose**: RSVPs to private events without a token are blocked.

**What It Tests**:
- ✅ Protected events require authentication
- ✅ Unauthenticated RSVP to private event rejected
- ✅ Returns 401/403/404 status
- ✅ RSVP NOT created

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
def test_rsvp_to_non_public_event_without_auth_returns_error(base_url, authenticated_headers):
    """Edge Case 3: RSVPs to private events without a token are blocked."""
    # Create a private non-public event
    event_payload = {"title": "Private Board Meeting", "date": "2026-09-01", "is_public": False}
    create_res = requests.post(f"{base_url}/api/events", json=event_payload, headers=authenticated_headers)
    event_id = create_res.json().get("id")

    # Attempt RSVP without authorization headers
    rsvp_res = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp_res.status_code in [401, 403, 404] # Depends on security setup
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

**Purpose**: Requesting an event ID that does not exist should yield a 404 Not Found.

**What It Tests**:
- ✅ Non-existent event returns 404 status
- ✅ Proper error handling for missing resources

**HTTP Request**:
```http
GET http://localhost:4000/api/events/999999
```

**Test Implementation**:
```python
def test_get_invalid_event_id_returns_404(base_url):
    """Edge Case: Requesting an event ID that does not exist should yield a 404 Not Found."""
    invalid_id = 999999
    response = requests.get(f"{base_url}/api/events/{invalid_id}")
    assert response.status_code == 404
```

**Expected Response** (404 Not Found):
```json
{
    "error": "Event not found"
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

**Purpose**: Sending an event payload without a 'title' should trigger a 400 Bad Request.

**What It Tests**:
- ✅ Event creation requires all mandatory fields
- ✅ Missing title returns 400 status
- ✅ Input validation enforced
- ✅ Event NOT created with incomplete data

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
def test_create_event_with_missing_required_fields_returns_400(base_url, authenticated_headers):
    """Edge Case: Sending an event payload without a 'title' should trigger a 400 Bad Request."""
    incomplete_payload = {
        "date": "2026-12-01T12:00:00",
        "is_public": True
    }
    response = requests.post(f"{base_url}/api/events", json=incomplete_payload, headers=authenticated_headers)
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

**Purpose**: Attempting to RSVP to an event ID that does not exist should return a 404.

**What It Tests**:
- ✅ Non-existent event returns 404 status
- ✅ RSVP NOT created for invalid event
- ✅ Referential integrity enforced

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
def test_rsvp_to_non_existent_event_returns_404(base_url, authenticated_headers):
    """Edge Case: Attempting to RSVP to an event ID that does not exist should return a 404."""
    invalid_event_id = 888888
    response = requests.post(f"{base_url}/api/rsvps/event/{invalid_event_id}", json={"attending": True}, headers=authenticated_headers)
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

## 💾 Database Models

### Model 1: User

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    rsvps = db.relationship('RSVP', backref='user', lazy=True)
    events = db.relationship('Event', backref='creator', lazy=True)
    
    def set_password(password):
        # Hash plaintext password using werkzeug
        
    def check_password(password) -> bool:
        # Verify password against hash
        
    def to_dict() -> dict:
        # Returns: {id, username, is_admin, created_at}
        # Excludes: password_hash (security)
```

**Key Rules**:
- ✅ Username is unique
- ✅ First user becomes admin
- ✅ Password hashed before storage
- ✅ Password never exposed in responses

---

### Model 2: Event

```python
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    is_public = db.Column(db.Boolean, default=True, nullable=False)
    requires_admin = db.Column(db.Boolean, default=False, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    rsvps = db.relationship('RSVP', backref='event', lazy=True, cascade='all, delete-orphan')
    
    def to_dict() -> dict:
        # Returns: {all fields above, rsvp_count, attendees}
        # rsvp_count = total RSVPs
        # attendees = user_ids where attending=True
```

**Access Control**:
| Type | `is_public` | `requires_admin` | RSVP Auth? |
|------|-------------|------------------|-----------|
| Public | True | False | No |
| Protected | False | False | Yes (any user) |
| Admin | False | True | Yes (admin only) |

---

### Model 3: RSVP

```python
class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    attending = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def to_dict() -> dict:
        # Returns: {id, event_id, user_id, attending, created_at}
```

**Key Points**:
- ✅ `user_id` can be None (anonymous RSVPs)
- ✅ `attending=True` means attending, `False` means declined
- ✅ One RSVP per user per event (POST updates existing)
- ✅ Capacity checks only count attending=True

---

## 🔌 API Reference

**Base URL**: `http://localhost:4000`

### Authentication

#### POST /api/auth/register
```json
{
    "username": "john_doe",
    "password": "SecurePassword123"
}
```
**Response** (201): `{message, user}`

#### POST /api/auth/login
```json
{
    "username": "john_doe",
    "password": "SecurePassword123"
}
```
**Response** (200): `{access_token, user}`

---

### Events

#### GET /api/events
**Response** (200): `[{event}, {event}, ...]`

#### POST /api/events (requires auth)
```json
{
    "title": "Python Meetup",
    "date": "2026-06-01",
    "description": "...",
    "location": "...",
    "capacity": 50,
    "is_public": true,
    "requires_admin": false
}
```
**Response** (201): `{event}`

#### GET /api/events/{event_id}
**Response** (200): `{event}` or (404): error

---

### RSVPs

#### POST /api/rsvps/event/{event_id}
```json
{
    "attending": true
}
```
**Response** (201/200): `{rsvp}`

#### GET /api/rsvps/event/{event_id}
**Response** (200): `{event, rsvps[], stats}`

---

## 🧪 Test Suite (13 Tests Total)

### conftest.py - Test Configuration & Fixtures

**Purpose**: Centralizes pytest configuration, shared fixtures, and utilities used across all test modules.

#### Configuration Constants

```python
BASE_URL = "http://localhost:4000"
```

- Defines the API server endpoint for all integration tests
- Centralized configuration - easy to update if port changes
- Used by all HTTP request operations

---

#### Fixture 1: `base_url` (Session Scope)

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
- ✅ URL doesn't change during test execution
- ✅ Improves performance by creating once
- ✅ Shared across all tests

---

#### Fixture 2: `unique_user_credentials` (Function Scope)

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
@pytest.fixture
def unique_user_credentials():
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

#### Fixture 3: `authenticated_headers` (Function Scope)

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
@pytest.fixture
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

**Fixture Scope Explanation**:
- Function-scoped: Each test gets a fresh, unique authenticated user
- No test can interfere with another's authentication state
- Ensures test isolation and prevents cross-test contamination

---

### Test Execution Commands

```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/test_models.py -v

# Run specific test
pytest tests/test_api.py::test_register_user_creates_new_user -v

# Run tests matching pattern
pytest -k "rsvp" -v

# Run with coverage
pytest --cov=. --cov-report=html

# Run with detailed output
pytest -v -s

# Stop at first failure
pytest -x
```

---

### Unit Tests (test_models.py - 5 Tests)

| # | Test | Purpose |
|---|------|---------|
| 1 | `test_user_password_hashing_behaves_correctly` | Password hashing/verification works |
| 2 | `test_user_to_dict_conversion` | User serializes correctly to dict |
| 3 | `test_event_to_dict_empty_rsvps` | Event handles zero RSVPs |
| 4 | `test_event_to_dict_with_mocked_rsvps_calculates_counts` | RSVP counting and filtering works |
| 5 | `test_rsvp_to_dict_conversion` | RSVP serializes correctly to dict |

---

### Integration Tests (test_api.py - 8 Tests)

#### Happy Path (6 tests)

| # | Test | Validates |
|---|------|-----------|
| 6 | `test_health_endpoint_returns_healthy` | Server running, health check works |
| 7 | `test_register_user_creates_new_user` | User registration succeeds |
| 8 | `test_login_returns_jwt_token` | Login returns valid JWT |
| 9 | `test_create_public_event_requires_auth_and_succeeds_with_token` | Event creation with auth works |
| 10 | `test_rsvp_to_public_event_succeeds_without_auth` | Public event RSVP without auth works |
| 11 | `test_get_all_events_returns_list` | GET /api/events returns list |

#### Error Handling (7 tests)

| # | Test | Validates |
|---|------|-----------|
| 12 | `test_duplicate_username_registration_returns_400` | Duplicate username rejected |
| 13 | `test_create_event_without_auth_returns_401` | Event creation requires auth |
| 14 | `test_rsvp_to_non_public_event_without_auth_returns_error` | Protected event requires auth |
| 15 | `test_get_invalid_event_id_returns_404` | Non-existent event returns 404 |
| 16 | `test_create_event_with_missing_required_fields_returns_400` | Missing fields rejected |
| 17 | `test_rsvp_to_non_existent_event_returns_404` | RSVP to invalid event returns 404 |

---

## 🎓 Designing New Tests

### Template

```python
def test_[feature]_[condition]_[expected_outcome](fixtures):
    """Clear description."""
    
    # SETUP
    data = {...}
    
    # ACTION
    response = requests.post(f"{base_url}/api/endpoint", json=data, headers=headers)
    
    # ASSERTION
    assert response.status_code == expected_code
    assert response.json().get("field") == expected_value
```

### Example: Event Capacity

```python
def test_rsvp_respects_event_capacity(base_url, authenticated_headers):
    """Event capacity prevents overbooking."""
    
    # Create event with capacity=2
    event = {"title": "Small", "date": "2026-06-01", "capacity": 2, "is_public": True}
    event_res = requests.post(f"{base_url}/api/events", json=event, headers=authenticated_headers)
    event_id = event_res.json()["id"]
    
    # RSVP 1 and 2 (succeed)
    for i in range(2):
        rsvp = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
        assert rsvp.status_code in [200, 201]
    
    # RSVP 3 (fails)
    rsvp3 = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={})
    assert rsvp3.status_code == 400
    assert "capacity" in rsvp3.json().get("error", "").lower()
```

### Example: Admin Access Control

```python
def test_admin_event_blocks_non_admin(base_url, authenticated_headers):
    """Only admins can RSVP to admin events."""
    
    # Create admin event
    event = {"title": "Admin", "date": "2026-06-01", "requires_admin": True, "is_public": False}
    event_res = requests.post(f"{base_url}/api/events", json=event, headers=authenticated_headers)
    event_id = event_res.json()["id"]
    
    # Create non-admin user
    non_admin = {"username": f"user_{int(time.time() * 1000) + 1}", "password": "SecurePassword123"}
    requests.post(f"{base_url}/api/auth/register", json=non_admin)
    login = requests.post(f"{base_url}/api/auth/login", json=non_admin)
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Non-admin RSVP fails
    rsvp = requests.post(f"{base_url}/api/rsvps/event/{event_id}", json={"attending": True}, headers=headers)
    assert rsvp.status_code == 403
    assert "admin" in rsvp.json().get("error", "").lower()
```

### Checklist

For each endpoint, test:
- [ ] Valid request succeeds
- [ ] Missing required fields returns 400
- [ ] Invalid data types returns 400
- [ ] Protected endpoints return 401 without auth
- [ ] Non-admin to admin endpoint returns 403
- [ ] Non-existent resources return 404
- [ ] Business logic enforced (capacity, uniqueness)
- [ ] Correct response format
- [ ] Correct HTTP status codes
- [ ] Data persisted to database

---

## 🔐 Security

### Current
- ✅ Password hashing (werkzeug)
- ✅ JWT authentication
- ✅ Role-based access control
- ✅ SQLAlchemy ORM (SQL injection prevention)

### Recommendations
- Upgrade to bcrypt/argon2
- Add JWT refresh tokens
- Input validation (marshmallow/pydantic)
- Rate limiting (Flask-Limiter)
- HTTPS in production
- Better error handling
- Logging & monitoring
- .env file for secrets

---

## 📚 Documentation

- **Swagger UI**: http://localhost:4000/apidocs
- **OpenAPI Spec**: http://localhost:4000/api/openapi.yaml

---

**Made with ❤️ for learning web development**
