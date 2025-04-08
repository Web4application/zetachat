import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Import global styles
import App from './App';
import { Provider } from 'react-redux'; // For state management
import store from './store'; // Redux store
import reportWebVitals from './reportWebVitals'; // Optional performance measurement

// Render the App component and wrap it with Redux Provider for global state management
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <Provider store={store}>
            <App />
        </Provider>
    </React.StrictMode>
);

// Measure app performance (optional)
reportWebVitals(console.log);
