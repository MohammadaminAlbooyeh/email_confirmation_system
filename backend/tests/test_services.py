import pytest
from app.utils.password import hash_password, verify_password
from app.utils.validators import (
    validate_email_format,
    validate_password_strength,
    validate_full_name
)


def test_password_hashing():
    """Test password hashing and verification"""
    password = "TestPassword123!"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed)


def test_invalid_password_verification():
    """Test invalid password verification"""
    password = "TestPassword123!"
    hashed = hash_password(password)
    assert not verify_password("WrongPassword", hashed)


def test_email_validation():
    """Test email format validation"""
    assert validate_email_format("test@example.com")
    assert not validate_email_format("invalid-email")


def test_password_strength_validation():
    """Test password strength validation"""
    valid, message = validate_password_strength("TestPassword123!")
    assert valid

    invalid, message = validate_password_strength("weak")
    assert not invalid


def test_full_name_validation():
    """Test full name validation"""
    assert validate_full_name("John Doe")
    assert not validate_full_name("J")
    assert not validate_full_name("A" * 101)
