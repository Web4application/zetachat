import React, { useState, useEffect } from 'react';
import socket from './services/socket';
import ChatBox from './components/ChatBox';
import InputField from './components/InputField';

const App = () => {
  const [messages, setMessages] = useState([]);
  const [username, setUsername] = useState('');

  useEffect(() => {
    socket.on('message', (message) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    return () => {
      socket.off('message');
    };
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Zetachat</h1>

      {!username ? (
        <div>
          <input
            type="text"
            placeholder="Enter your username"
            onChange={(e) => setUsername(e.target.value)}
          />
          <button onClick={() => setUsername(username)}>Join Chat</button>
        </div>
      ) : (
        <div>
          <ChatBox messages={messages} />
          <InputField username={username} socket={socket} />
        </div>
      )}
    </div>
  );
};

export default App;
