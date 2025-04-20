import React, { useState } from 'react';

const InputField = ({ username, socket }) => {
  const [inputMessage, setInputMessage] = useState('');

  const sendMessage = () => {
    if (inputMessage.trim() !== '') {
      const messageData = {
        user: username || 'Anonymous',
        text: inputMessage,
        time: new Date().toLocaleTimeString(),
      };
      socket.emit('message', messageData); // Send message to server
      setInputMessage('');
    }
  };

  return (
    <div style={{ marginTop: '10px' }}>
      <input
        type="text"
        value={inputMessage}
        onChange={(e) => setInputMessage(e.target.value)}
        placeholder="Type a message"
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default InputField;
