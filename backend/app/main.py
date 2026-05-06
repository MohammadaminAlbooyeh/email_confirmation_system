from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.error_handler import setup_error_handlers
from app.routes import auth, user

app = FastAPI(title="Email Confirmation System")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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
