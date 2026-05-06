import api from './api';

export const userService = {
  async getProfile() {
    const response = await api.get('/user/profile');
    return response.data;
  },

  async updateProfile(data) {
    const response = await api.put('/user/profile', data);
    return response.data;
  },
};
