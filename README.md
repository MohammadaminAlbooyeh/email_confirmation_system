# Email Confirmation System

A full-stack web application for user authentication with email confirmation. Built with FastAPI (backend) and React (frontend).

## Features

- User registration with email validation
- Email-based confirmation system
- Secure password hashing and JWT authentication
- User profile management
- Protected routes and dashboard
- Responsive UI with modern design

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **Email**: SMTP with aiosmtplib
- **Validation**: Pydantic

### Frontend
- **Framework**: React 18
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Styling**: CSS with Tailwind CSS
- **State Management**: React Context API

## Project Structure

```
email_confirmation_system/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── middleware/      # Custom middleware
│   │   ├── utils/           # Utility functions
│   │   ├── config.py        # Configuration
│   │   ├── database.py      # Database setup
│   │   └── main.py          # FastAPI app
│   ├── migrations/          # Alembic migrations
│   ├── tests/               # Unit tests
│   └── run.py               # Entry point
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # API services
│   │   ├── utils/           # Utilities
│   │   ├── context/         # Context providers
│   │   ├── styles/          # Global styles
│   │   ├── App.jsx
│   │   └── index.js
│   ├── public/
│   └── package.json
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- PostgreSQL 12+ (or use Docker)
- SMTP server for email sending

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd email_confirmation_system
```

2. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Backend setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

4. Frontend setup
```bash
cd frontend
npm install
npm start
```

### Using Docker Compose

```bash
docker-compose up -d
```

Access the application at `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Register a new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/confirm/{token}` - Confirm email with token
- `POST /api/auth/resend` - Resend confirmation email

### User
- `GET /api/user/profile` - Get user profile (protected)
- `PUT /api/user/profile` - Update user profile (protected)

## Environment Variables

Create a `.env` file in the root directory:

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/email_confirmation
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=email_confirmation

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# SMTP
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SENDER_EMAIL=noreply@example.com

# Frontend
FRONTEND_URL=http://localhost:3000
REACT_APP_API_URL=http://localhost:8000/api
```

## Development

### Running Tests

Backend:
```bash
cd backend
pytest
```

### Code Quality

Backend code follows PEP 8 with the configuration in `pyproject.toml`:
- Black for formatting
- isort for import sorting
- Pylint for linting

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
