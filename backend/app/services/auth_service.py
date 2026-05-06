from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, SignupRequest, TokenResponse, ConfirmationResponse
from app.schemas.response import ErrorResponse
from app.services import email_service, token_service, user_service
from app.utils.jwt_handler import create_access_token, verify_confirmation_token
from app.utils.password import verify_password, DUMMY_HASH
from app.utils.validators import (
    validate_email_format,
    validate_password_strength,
    validate_full_name,
)
from app.utils.logger import logger


async def signup(db: Session, request: SignupRequest) -> TokenResponse | ErrorResponse:
    existing_user = user_service.get_user_by_email(db, request.email)
    if existing_user:
        return ErrorResponse(error="user_exists", detail="User with this email already exists")

    user = user_service.create_user(db, request)
    token = token_service.create_confirmation_token_db(db, user.id, user.email)
    await email_service.send_confirmation_email(user.email, token, user.full_name)

    access_token = create_access_token({"sub": user.email, "user_id": user.id})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id,
        email=user.email,
    )


async def login(db: Session, request: LoginRequest) -> TokenResponse | ErrorResponse:
    user = user_service.get_user_by_email(db, request.email)
    password_hash = user.password_hash if user else DUMMY_HASH

    if not verify_password(request.password, password_hash):
        return ErrorResponse(error="invalid_credentials", detail="Invalid email or password")

    if not user:
        return ErrorResponse(error="invalid_credentials", detail="Invalid email or password")

    if not user.confirmed_at:
        return ErrorResponse(error="email_not_confirmed", detail="Please confirm your email before logging in")

    access_token = create_access_token({"sub": user.email, "user_id": user.id})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id,
        email=user.email,
    )


async def confirm_email(db: Session, token: str) -> ConfirmationResponse | ErrorResponse:
    email = verify_confirmation_token(token)
    if not email:
        return ErrorResponse(error="invalid_token", detail="Invalid or expired token")

    db_token = token_service.get_token_by_token_string(db, token)
    if not db_token or not token_service.is_token_valid(db_token):
        return ErrorResponse(error="invalid_token", detail="Invalid or expired token")

    user = user_service.get_user_by_id(db, db_token.user_id)
    if not user:
        return ErrorResponse(error="user_not_found", detail="User not found")

    user.confirmed_at = datetime.now(timezone.utc)
    db.commit()

    token_service.mark_token_as_used(db, db_token)
    await email_service.send_welcome_email(user.email, user.full_name)
    logger.info(f"Email confirmed for user {user.id}")

    return ConfirmationResponse(message="Email confirmed successfully", user_id=user.id)


async def resend_confirmation(db: Session, email: str) -> dict:
    user = user_service.get_user_by_email(db, email)
    if user and not user.confirmed_at:
        token = token_service.create_confirmation_token_db(db, user.id, user.email)
        await email_service.send_confirmation_email(user.email, token, user.full_name)

    return {"message": "If this email is registered and unconfirmed, a confirmation email has been sent"}
