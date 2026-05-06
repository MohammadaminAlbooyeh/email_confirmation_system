import './LoadingSpinner.css';

function LoadingSpinner() {
  return (
    <div className="spinner-container" role="status" aria-label="Loading...">
      <div className="spinner-ring">
        <div className="spinner"></div>
      </div>
      <p>Loading...</p>
    </div>
  );
}

export default LoadingSpinner;
