import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension';
import chatReducer from './reducers/chatReducer'; // Custom chat reducer
import authReducer from './reducers/authReducer'; // Custom auth reducer

// Combine all reducers
const rootReducer = combineReducers({
    chat: chatReducer,
    auth: authReducer,
});

// Create Redux store with middleware (Thunk)
const store = createStore(
    rootReducer,
    composeWithDevTools(applyMiddleware(thunk))
);

export default store;
