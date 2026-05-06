import api from './api';

export const authService = {
  async signup(email, password, fullName) {
    const response = await api.post('/auth/signup', {
      email,
      password,
      full_name: fullName,
    });
    return response.data;
  },

  async login(email, password) {
    const response = await api.post('/auth/login', {
      email,
      password,
    });
    return response.data;
  },

  async confirmEmail(token) {
    const response = await api.get(`/auth/confirm/${token}`);
    return response.data;
  },

  async resendConfirmation(email) {
    const response = await api.post('/auth/resend', {
      email,
    });
    return response.data;
  },

  logout() {
    localStorage.removeItem('access_token');
  },
};
