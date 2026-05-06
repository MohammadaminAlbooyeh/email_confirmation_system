# Email Confirmation System - Backend

FastAPI-based backend for the Email Confirmation System.

## Requirements

- Python 3.8+
- PostgreSQL 12+

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```

4. Run the application:
```bash
python run.py
```

The API will be available at `http://localhost:8000`

## Project Structure

```
backend/
├── app/
│   ├── models/          # SQLAlchemy ORM models
│   ├── schemas/         # Pydantic request/response schemas
│   ├── routes/          # API endpoint routers
│   ├── services/        # Business logic layer
│   ├── middleware/      # Custom middleware
│   ├── utils/           # Utility functions
│   ├── config.py        # Configuration management
│   ├── database.py      # Database initialization
│   └── main.py          # FastAPI application
├── migrations/          # Alembic database migrations
├── tests/               # Unit tests
├── run.py               # Application entry point
├── pyproject.toml       # Code quality configuration
└── requirements.txt     # Python dependencies
```

## Key Components

### Models
- `User` - User account information
- `ConfirmationToken` - Email confirmation tokens

### Services
- `auth_service` - Authentication and registration logic
- `user_service` - User management
- `email_service` - Email sending
- `token_service` - Token generation and validation

### Utilities
- `jwt_handler` - JWT token creation and verification
- `password` - Password hashing and verification
- `validators` - Input validation functions
- `logger` - Application logging

## API Routes

All routes are prefixed with `/api`

### Authentication Routes (`/auth`)
- `POST /signup` - User registration
- `POST /login` - User login
- `GET /confirm/{token}` - Email confirmation
- `POST /resend` - Resend confirmation email

### User Routes (`/user`)
- `GET /profile` - Get user profile (requires authentication)
- `PUT /profile` - Update user profile (requires authentication)

## Configuration

Configuration is managed through environment variables in the `app/config.py` file using Pydantic Settings.

Required environment variables:
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - JWT secret key
- `SMTP_SERVER` - SMTP server address
- `SMTP_PORT` - SMTP port
- `SMTP_USER` - SMTP username
- `SMTP_PASSWORD` - SMTP password
- `SENDER_EMAIL` - Email address to send from

## Database

The application uses PostgreSQL with SQLAlchemy ORM. Database migrations are managed with Alembic.

To run migrations:
```bash
cd backend
alembic upgrade head
```

## Testing

Run tests with pytest:
```bash
pytest
```

## Code Quality

The project uses:
- **Black** - Code formatting
- **isort** - Import sorting
- **Pylint** - Code linting

Configuration is in `pyproject.toml`

## Security

- Passwords are hashed using bcrypt
- JWT tokens are used for authentication
- Email confirmation tokens expire after 24 hours
- CORS is configured for the frontend domain
- Input validation using Pydantic schemas
