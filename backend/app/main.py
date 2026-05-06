from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.middleware.error_handler import setup_error_handlers
from app.routes import auth, user

app = FastAPI(title="Email Confirmation System")

# CORS middleware - allow origins from environment variable
allowed_origins = [settings.FRONTEND_URL]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup error handlers
setup_error_handlers(app)

# Include routes
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(user.router, prefix="/api/user", tags=["user"])


@app.get("/")
async def root():
    return {"message": "Email Confirmation System API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
