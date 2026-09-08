import os

import pytest


os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["BEARER_TOKEN"] = "test-token"


@pytest.fixture
def valid_payload():
    return {
        "email": "user@example.com",
        "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
        "blocked_reason": "Spam activity detected",
        }