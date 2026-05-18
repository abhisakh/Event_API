import pytest
from datetime import datetime
from models import User, Event, RSVP

# ==========================================
# USER MODEL TESTS
# ==========================================

def test_user_password_hashing_behaves_correctly():
    """Unit Test: Verifies that password hashing hashes strings and checks successfully."""
    user = User()
    user.username = "test_user"
    user.set_password("SecureSecretPass123!")

    # Raw password text is never exposed explicitly
    assert user.password_hash != "SecureSecretPass123!"

    assert user.check_password("SecureSecretPass123!") is True

    # Assert wrong password verification correctly fails
    assert user.check_password("WrongPassword123") is False

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

# ==========================================
# EVENT MODEL TESTS
# ==========================================

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

# ==========================================
# RSVP MODEL TESTS
# ==========================================

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