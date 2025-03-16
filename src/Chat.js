import React, { useState } from 'react';
import sendMessageToAI from '../utils/api'; // Adjust the path as needed

const ChatComponent = () => {
  const [userMessage, setUserMessage] = useState('');
  const [aiResponse, setAIResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSendMessage = async () => {
    if (!userMessage.trim()) return;

    setLoading(true);
    const response = await sendMessageToAI(userMessage);
    setAIResponse(response);
    setLoading(false);
    setUserMessage(''); // Clear the input
  };

  return (
    <div>
      <input
        type="text"
        value={userMessage}
        onChange={(e) => setUserMessage(e.target.value)}
        placeholder="Type a message..."
      />
      <button onClick={handleSendMessage} disabled={loading}>
        {loading ? 'Sending...' : 'Send'}
      </button>
      <div>AI Response: {aiResponse}</div>
    </div>
  );
};

export default ChatComponent;
