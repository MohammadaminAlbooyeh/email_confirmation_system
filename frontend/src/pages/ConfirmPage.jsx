import { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { authService } from '../services/authService';
import { ERROR_MESSAGES, SUCCESS_MESSAGES } from '../utils/constants';
import Alert from '../components/Alert';
import LoadingSpinner from '../components/LoadingSpinner';
import Brand from '../components/Brand';
import './ConfirmPage.css';

function ConfirmPage() {
  const { token } = useParams();
  const [status, setStatus] = useState('loading');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    let isMounted = true;
    let timer;

    const confirmEmail = async () => {
      try {
        await authService.confirmEmail(token);
        if (isMounted) {
          setStatus('success');
          setMessage(SUCCESS_MESSAGES.CONFIRM_SUCCESS);
          timer = setTimeout(() => {
            if (isMounted) navigate('/dashboard');
          }, 3000);
        }
      } catch (err) {
        if (isMounted) {
          setStatus('error');
          setMessage(err.response?.data?.detail || ERROR_MESSAGES.INVALID_TOKEN);
        }
      }
    };

    confirmEmail();
    return () => {
      isMounted = false;
      if (timer) clearTimeout(timer);
    };
  }, [token, navigate]);

  return (
    <div className="confirm-page">
      <div className="floating-shapes">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <div className="shape shape-3"></div>
      </div>
      <div className="confirm-content">
        <Brand />
        <div className="confirm-container slide-up">
        {status === 'loading' && (
          <>
            <div className="confirm-icon confirm-icon--loading">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <path d="M12 6v6l4 2"/>
              </svg>
            </div>
            <h2>Verifying Your Email</h2>
            <p className="confirm-subtitle">Please wait while we confirm your email address...</p>
            <LoadingSpinner />
          </>
        )}
        {status === 'success' && (
          <>
            <div className="confirm-icon confirm-icon--success">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22,4 12,14.01 9,11.01"/>
              </svg>
            </div>
            <h2>Email Verified!</h2>
            <p className="confirm-subtitle">Your email has been successfully confirmed. Redirecting to dashboard...</p>
            <Alert type="success" message={message} />
          </>
        )}
        {status === 'error' && (
          <>
            <div className="confirm-icon confirm-icon--error">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <line x1="15" y1="9" x2="9" y2="15"/>
                <line x1="9" y1="9" x2="15" y2="15"/>
              </svg>
            </div>
            <h2>Verification Failed</h2>
            <p className="confirm-subtitle">We couldn't verify your email. The link may be invalid or expired.</p>
            <Alert type="error" message={message} />
            <div className="confirm-actions">
              <button className="btn-primary" onClick={() => navigate('/login')}>
                Back to Login
              </button>
              <Link to="/resend" className="btn-secondary">
                Resend Confirmation Email
              </Link>
            </div>
          </>
        )}
      </div>
    </div>
    </div>
  );
}

export default ConfirmPage;
