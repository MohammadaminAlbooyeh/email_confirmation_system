from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import (
    LoginRequest,
    SignupRequest,
    ResendRequest,
)
from app.services import auth_service

router = APIRouter()


@router.post("/signup")
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    """User registration endpoint"""
    return await auth_service.signup(db, request)


@router.get("/confirm/{token}")
async def confirm_email(token: str, db: Session = Depends(get_db)):
    """Email confirmation endpoint"""
    return await auth_service.confirm_email(db, token)


@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """User login endpoint"""
    return await auth_service.login(db, request)


@router.post("/resend")
async def resend_confirmation(
    request: ResendRequest, db: Session = Depends(get_db)
):
    """Resend confirmation email"""
    return await auth_service.resend_confirmation(db, request.email)
