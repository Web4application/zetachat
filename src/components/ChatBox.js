import React from 'react';

const ChatBox = ({ messages }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', height: '300px', overflowY: 'scroll' }}>
      {messages.map((msg, index) => (
        <div key={index}>
          <strong>{msg.user}: </strong>
          {msg.text} <small style={{ color: '#888' }}>({msg.time})</small>
        </div>
      ))}
    </div>
  );
};

export default ChatBox;
