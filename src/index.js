import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Optional for styling
import App from './App'; // Import the App component

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root') // Matches the "root" div in public/index.html
);
