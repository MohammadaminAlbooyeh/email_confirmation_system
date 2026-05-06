from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    email: str


class ConfirmationResponse(BaseModel):
    message: str
    user_id: int


class ResendRequest(BaseModel):
    email: EmailStr
