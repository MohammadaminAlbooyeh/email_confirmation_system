import re
from email_validator import EmailNotValidError, validate_email


def validate_email_format(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def normalize_email(email: str) -> str | None:
    try:
        validated = validate_email(email)
        return validated.normalized
    except EmailNotValidError:
        return None


def validate_password_strength(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, "Password is strong"


def validate_full_name(full_name: str) -> bool:
    return len(full_name.strip()) >= 2 and len(full_name.strip()) <= 100
