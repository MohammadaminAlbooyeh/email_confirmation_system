import { useState } from 'react';
import { Link } from 'react-router-dom';
import { authService } from '../services/authService';
import { validateEmail } from '../utils/validators';
import { ERROR_MESSAGES, SUCCESS_MESSAGES } from '../utils/constants';
import Alert from '../components/Alert';
import './ResendPage.css';

function ResendPage() {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');

    if (!validateEmail(email)) {
      setError(ERROR_MESSAGES.INVALID_EMAIL);
      return;
    }

    setLoading(true);
    try {
      await authService.resendConfirmation(email);
      setMessage(SUCCESS_MESSAGES.RESEND_SUCCESS);
      setEmail('');
    } catch (err) {
      setError(err.response?.data?.detail || ERROR_MESSAGES.NETWORK_ERROR);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="resend-page">
      <div className="resend-container">
        <h2>Resend Confirmation Email</h2>
        {error && <Alert type="error" message={error} onClose={() => setError('')} />}
        {message && <Alert type="success" message={message} />}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              autoComplete="email"
              required
            />
          </div>
          <button type="submit" disabled={loading}>
            {loading ? 'Sending...' : 'Resend'}
          </button>
        </form>
        <div className="footer-links">
          <p>
            Remember your password? <Link to="/login">Log in</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

export default ResendPage;
