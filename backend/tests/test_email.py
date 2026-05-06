import pytest
from app.services import email_service


def test_send_confirmation_email():
    """Test sending confirmation email"""
    result = email_service.send_confirmation_email(
        "test@example.com",
        "test_token_123"
    )
    assert isinstance(result, bool)


def test_send_welcome_email():
    """Test sending welcome email"""
    result = email_service.send_welcome_email(
        "test@example.com",
        "Test User"
    )
    assert isinstance(result, bool)
