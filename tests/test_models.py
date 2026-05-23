import pytest
from datetime import datetime
from models import User, Event, RSVP

# ==========================================
# USER MODEL TESTS
# ==========================================

def test_user_password_hashing_behaves_correctly():
    """Unit Test: Verifies that password hashing hashes strings and checks successfully."""
    # Arrange: Create a user and define a password
    # Note: Passwords are now hashed on the frontend before reaching the backend
    user = User()
    user.username = "test_user"
    raw_password = "SecureSecretPass123!"

    # Act: Hash the password using the model's security method
    user.set_password(raw_password)

    # Assert: Verify security requirements are met
    # Confirms the raw password is never stored in plain text for security
    assert user.password_hash != raw_password
    # Confirms the verification logic correctly identifies the original password
    assert user.check_password(raw_password) is True
    # Confirms the system rejects incorrect password attempts
    assert user.check_password("WrongPassword123") is False

def test_user_to_dict_conversion():
    """Unit Test: Validates dictionary output matching the expected layout framework structure."""
    # Arrange: Create a fixed timestamp and a user object
    fixed_time = datetime(2026, 5, 18, 12, 0, 0)
    user = User(
        id=42,
        username="admin_guy",
        is_admin=True,
        created_at=fixed_time
    )

    # Act: Convert the object to a dictionary for API delivery
    user_dict = user.to_dict()

    # Assert: Verify the dictionary format matches the API specification
    assert user_dict["id"] == 42
    assert user_dict["username"] == "admin_guy"
    assert user_dict["is_admin"] is True
    # Confirms date is correctly serialized to an ISO string
    assert user_dict["created_at"] == "2026-05-18T12:00:00"

# ==========================================
# EVENT MODEL TESTS
# ==========================================

def test_event_to_dict_empty_rsvps():
    """Unit Test: Validates event dictionary exports correctly when there are zero attendees."""
    # Arrange: Setup an event with an empty RSVP list
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
        rsvps=[]
    )

    # Act: Extract the dictionary representation
    event_dict = event.to_dict()

    # Assert: Verify the count and list are empty
    assert event_dict["id"] == 101
    assert event_dict["title"] == "Tech Conference"
    # Confirms the rsvp_count logic correctly handles zero entries
    assert event_dict["rsvp_count"] == 0
    assert event_dict["attendees"] == []


def test_event_to_dict_with_mocked_rsvps_calculates_counts():
    """Unit Test: Validates tracking calculations for event RSVPs without interacting with DB engines."""
    # Arrange: Simulate multiple RSVP records with mixed attendance statuses
    fixed_time = datetime(2026, 6, 1, 15, 30, 0)
    rsvp1 = RSVP(user_id=11, attending=True)
    rsvp2 = RSVP(user_id=12, attending=False)
    rsvp3 = RSVP(user_id=13, attending=True)

    event = Event(
        id=202,
        title="Exclusive Workshop",
        date=fixed_time,
        rsvps=[rsvp1, rsvp2, rsvp3]
    )

    # Act: Process the event model logic
    event_dict = event.to_dict()

    # Assert: Verify relationship filtering and counting
    # Confirms total linked RSVP records are counted regardless of status
    assert event_dict["rsvp_count"] == 3
    # Confirms only users who set 'attending=True' are included in the final attendee list
    assert event_dict["attendees"] == [11, 13]

# ==========================================
# RSVP MODEL TESTS
# ==========================================

def test_rsvp_to_dict_conversion():
    """Unit Test: Validates RSVP properties populate dictionary mapping arrays cleanly."""
    # Arrange: Define a specific RSVP record
    fixed_time = datetime(2026, 5, 18, 16, 0, 0)
    rsvp = RSVP(
        id=7,
        event_id=101,
        user_id=11,
        attending=True,
        created_at=fixed_time
    )

    # Act: Convert to dictionary
    rsvp_dict = rsvp.to_dict()

    # Assert: Verify all foreign keys and attributes are preserved
    assert rsvp_dict["id"] == 7
    assert rsvp_dict["event_id"] == 101
    assert rsvp_dict["user_id"] == 11
    assert rsvp_dict["attending"] is True
    assert rsvp_dict["created_at"] == "2026-05-18T16:00:00"