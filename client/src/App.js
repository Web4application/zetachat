import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');  // Point to your backend server

function App() {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState('');

  // Listen for chat messages from the server
  useEffect(() => {
    socket.on('chat message', (msg) => {
      setMessages((prevMessages) => [...prevMessages, msg]);
    });

    return () => {
      socket.off('chat message');
    };
  }, []);

  const sendMessage = () => {
    if (message.trim()) {
      socket.emit('chat message', message);  // Emit message to backend server
      setMessage('');
    }
  };

  return (
    <Router>
      <div>
        <h1>Welcome to ZetaChat!</h1>
        <div>
          <h2>Chat Room</h2>
          <div>
            {messages.map((msg, index) => (
              <div key={index}>{msg}</div>
            ))}
          </div>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message"
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </Router>
  );
}

export default App;
