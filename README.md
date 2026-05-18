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

#### 3. Integration Tests: Edge Cases & Error Conditions (`tests/test_api.py`)
These tests check robustness by intentionally feeding bad data or bypassing rules.
*   `test_duplicate_username_registration_returns_400`: Asserts that trying to use an identical username twice halts duplication workflows with an explicit HTTP 400 response.
*   `test_create_event_without_auth_returns_401`: Guarantees unauthenticated requests attempting to write an event to `POST /api/events` are rejected with a 401 status code.
*   `test_rsvp_to_non_public_event_without_auth_returns_error`: Protects private gatherings from unverified users, checking for error handling defaults.

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

