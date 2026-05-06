export const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export const VALIDATION_RULES = {
  PASSWORD_MIN_LENGTH: 8,
  FULL_NAME_MIN_LENGTH: 2,
  FULL_NAME_MAX_LENGTH: 100,
};

export const ERROR_MESSAGES = {
  INVALID_EMAIL: 'Please enter a valid email address',
  WEAK_PASSWORD: 'Password must be at least 8 characters with uppercase, lowercase, number, and special character',
  INVALID_FULL_NAME: 'Full name must be between 2 and 100 characters',
  USER_EXISTS: 'User with this email already exists',
  INVALID_CREDENTIALS: 'Invalid email or password',
  INVALID_TOKEN: 'Invalid or expired confirmation token',
  NETWORK_ERROR: 'Network error. Please try again.',
};

export const SUCCESS_MESSAGES = {
  SIGNUP_SUCCESS: 'Account created successfully! Please confirm your email.',
  LOGIN_SUCCESS: 'Login successful!',
  CONFIRM_SUCCESS: 'Email confirmed successfully!',
  RESEND_SUCCESS: 'Confirmation email sent!',
};
