from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.middleware.auth import get_current_user
from app.schemas.user import UserResponse, UserUpdate
from app.services import user_service

router = APIRouter()


@router.get("/profile", response_model=UserResponse)
async def get_profile(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get current user profile"""
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user_not_found")
    return user


@router.put("/profile", response_model=UserResponse)
async def update_profile(
    user_update: UserUpdate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update current user profile"""
    user = user_service.update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="user_not_found")
    return user
