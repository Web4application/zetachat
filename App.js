// Import required modules
import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

// Connect to the chat server
const socket = io('https://ovlusvvwyducpspqbfxn.supabase.co'); // Replace with your server URL

const App = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [username, setUsername] = useState('');

  useEffect(() => {
    // Listen for incoming messages
    socket.on('message', (message) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    return () => {
      socket.off('message');
    };
  }, []);

  const sendMessage = () => {
    if (inputMessage.trim() !== '') {
      const messageData = {
        user: username || 'Anonymous',
        text: inputMessage,
        time: new Date().toLocaleTimeString(),
      };
      socket.emit('message', messageData); // Send message to server
      setInputMessage(''); // Clear input field
    }
  };

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
          <div style={{ border: '1px solid #ccc', padding: '10px', height: '300px', overflowY: 'scroll' }}>
            {messages.map((msg, index) => (
              <div key={index}>
                <strong>{msg.user}: </strong>
                {msg.text} <small style={{ color: '#888' }}>({msg.time})</small>
              </div>
            ))}
          </div>
          <div style={{ marginTop: '10px' }}>
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              placeholder="Type a message"
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
