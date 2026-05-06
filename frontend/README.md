# Email Confirmation System - Frontend

React-based frontend for the Email Confirmation System.

## Requirements

- Node.js 14+
- npm or yarn

## Installation

1. Install dependencies:
```bash
npm install
```

2. Set up environment variables:
Create a `.env` file in the frontend directory:
```
REACT_APP_API_URL=http://localhost:8000/api
```

3. Start the development server:
```bash
npm start
```

The application will open at `http://localhost:3000`

## Available Scripts

- `npm start` - Start development server
- `npm build` - Create production build
- `npm test` - Run tests
- `npm format` - Format code with Prettier
- `npm format:check` - Check code formatting
- `npm lint` - Lint code with ESLint

## Project Structure

```
frontend/
├── src/
│   ├── components/      # Reusable React components
│   ├── pages/           # Page components
│   ├── hooks/           # Custom React hooks
│   ├── services/        # API service layer
│   ├── context/         # React Context providers
│   ├── utils/           # Utility functions
│   ├── styles/          # Global styles
│   ├── App.jsx          # Root component
│   └── index.js         # Application entry point
├── public/              # Static files
├── package.json         # Dependencies
└── README.md
```

## Key Features

### Components
- **Navbar** - Navigation bar with user info
- **ProtectedRoute** - Route guard for authenticated pages
- **Alert** - Notification component
- **LoadingSpinner** - Loading indicator

### Pages
- **SignupPage** - User registration
- **LoginPage** - User login
- **ConfirmPage** - Email confirmation
- **DashboardPage** - User dashboard
- **ResendPage** - Resend confirmation email

### Hooks
- **useAuth** - Authentication context hook
- **useFetch** - HTTP request hook

### Services
- **authService** - Authentication API calls
- **userService** - User management API calls
- **api** - Axios instance with interceptors

### Utilities
- **validators** - Input validation functions
- **constants** - Application constants
- **localStorage** - Local storage helpers

## API Integration

The frontend communicates with the backend API through the `api` service, which is an Axios instance configured with:
- Base URL from environment variable
- Authorization header with JWT token
- Request/response interceptors

## Authentication Flow

1. User registers with email and password
2. Confirmation email is sent
3. User clicks confirmation link
4. Email is confirmed and user can login
5. JWT token is stored in localStorage
6. Token is sent with all authenticated requests
7. Protected routes check token before rendering

## Styling

The application uses:
- CSS modules for component styles
- Tailwind CSS for utility classes
- CSS variables for theming

## Environment Variables

Create a `.env` file:

```
REACT_APP_API_URL=http://localhost:8000/api
```

## Development

### Code Quality

ESLint configuration:
- React recommended rules
- Prettier integration

### Building for Production

```bash
npm run build
```

Creates an optimized production build in the `build` folder.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance

- Code splitting with React Router
- Lazy loading of routes
- Optimized re-renders with React.memo
- Efficient state management with Context API
