import { VALIDATION_RULES } from './constants';

export const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

export const validatePassword = (password) => {
  if (password.length < VALIDATION_RULES.PASSWORD_MIN_LENGTH) {
    return false;
  }
  if (!/[A-Z]/.test(password)) return false;
  if (!/[a-z]/.test(password)) return false;
  if (!/[0-9]/.test(password)) return false;
  if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) return false;
  return true;
};

export const validateFullName = (fullName) => {
  const trimmed = fullName.trim();
  return (
    trimmed.length >= VALIDATION_RULES.FULL_NAME_MIN_LENGTH &&
    trimmed.length <= VALIDATION_RULES.FULL_NAME_MAX_LENGTH
  );
};
