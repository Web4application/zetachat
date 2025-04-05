import React from 'react';

const ChatBox = ({ messages, userTyping }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', height: '300px', overflowY: 'scroll', marginBottom: '10px' }}>
      {/* Display messages */}
      {messages.map((msg, index) => (
        <div key={index} style={{ marginBottom: '10px' }}>
          <strong>{msg.user}: </strong>
          {msg.text} <small style={{ color: '#888' }}>({msg.time})</small>
        </div>
      ))}

      {/* Display typing indicator */}
      {userTyping && <div style={{ fontStyle: 'italic', color: '#666' }}>{userTyping}</div>}
    </div>
  );
};

export default ChatBox;
