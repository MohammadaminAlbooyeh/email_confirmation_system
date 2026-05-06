from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt

from app.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None


def create_confirmation_token(email: str, expires_delta: Optional[timedelta] = None) -> str:
    data = {"sub": email, "type": "email_confirmation"}
    if expires_delta is None:
        expires_delta = timedelta(hours=24)
    return create_access_token(data, expires_delta)


def verify_confirmation_token(token: str) -> Optional[str]:
    payload = verify_token(token)
    if payload and payload.get("type") == "email_confirmation":
        return payload.get("sub")
    return None
