from fastapi import APIRouter

from app.schemas.auth import LoginRequest, SignupRequest
from app.services import auth_service

router = APIRouter()


@router.post("/signup")
async def signup(request: SignupRequest):
    """User registration endpoint"""
    return await auth_service.signup(request)


@router.get("/confirm/{token}")
async def confirm_email(token: str):
    """Email confirmation endpoint"""
    return await auth_service.confirm_email(token)


@router.post("/login")
async def login(request: LoginRequest):
    """User login endpoint"""
    return await auth_service.login(request)


@router.post("/resend")
async def resend_confirmation(email: str):
    """Resend confirmation email"""
    return await auth_service.resend_confirmation(email)
