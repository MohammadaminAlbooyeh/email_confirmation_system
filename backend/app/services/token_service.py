from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.token import ConfirmationToken
from app.models.user import User
from app.utils.jwt_handler import create_confirmation_token
from app.utils.logger import logger


def create_confirmation_token_db(db: Session, user_id: int, email: str) -> str:
    token = create_confirmation_token(email)
    expires_at = datetime.now(timezone.utc) + timedelta(hours=24)

    db_token = ConfirmationToken(
        user_id=user_id,
        token=token,
        expires_at=expires_at,
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    logger.info(f"Confirmation token created for user {user_id}")
    return token


def get_token_by_token_string(db: Session, token: str) -> ConfirmationToken | None:
    return db.query(ConfirmationToken).filter(
        ConfirmationToken.token == token
    ).first()


def mark_token_as_used(db: Session, db_token: ConfirmationToken) -> bool:
    if not db_token:
        return False
    db_token.used_at = datetime.now(timezone.utc)
    db.commit()
    logger.info(f"Token marked as used: {db_token.id}")
    return True


def is_token_valid(db_token: ConfirmationToken) -> bool:
    if not db_token:
        return False
    if db_token.used_at is not None:
        return False
    if db_token.expires_at < datetime.now(timezone.utc):
        return False
    return True
