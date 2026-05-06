from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.password import hash_password
from app.utils.validators import normalize_email
from app.utils.logger import logger


def create_user(db: Session, user_create: UserCreate) -> User:
    hashed_password = hash_password(user_create.password)
    normalized_email = normalize_email(user_create.email) or user_create.email
    db_user = User(
        email=normalized_email,
        password_hash=hashed_password,
        full_name=user_create.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"User created: {db_user.email}")
    return db_user


def get_user_by_email(db: Session, email: str) -> User | None:
    normalized_email = normalize_email(email) or email
    return db.query(User).filter(User.email == normalized_email).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User | None:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None
    if user_update.full_name:
        db_user.full_name = user_update.full_name
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    logger.info(f"User deleted: {db_user.email}")
    return True
