// src/components/Chat.js
import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

// Connect to the chat server (adjust the URL if needed)
const socket = io('web4app.com');

function Chat() {
  const [userMessage, setUserMessage] = useState('');
  const [chat, setChat] = useState([]);

  // Listen for chat messages from the server
  useEffect(() => {
    socket.on('chat message', (msg) => {
      // Use the functional update to ensure correct state when appending messages
      setChat((prevChat) => [...prevChat, msg]);
    });

    // Clean up event listener on component unmount
    return () => {
      socket.off('chat message');
    };
  }, []);

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (userMessage.trim()) {
      // Emit the message to the server
      socket.emit('chat message', userMessage);
      setUserMessage('');
    }
  };

  return (
    <div>
      <h1>Real Time Chat</h1>
      <form onSubmit={handleSendMessage}>
        <input
          type="text"
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
      <div>
        <h2>Chat Log:</h2>
        {chat.map((msg, index) => (
          <div key={index}>{msg}</div>
        ))}
      </div>
    </div>
  );
}

export default Chat;
