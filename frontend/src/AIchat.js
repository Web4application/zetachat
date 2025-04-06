import React, { useState } from 'react';
import axios from 'axios';

function AIChat() {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const handleSubmit = async () => {
        const res = await axios.post('http://localhost:5000/ai-response', { message });
        setResponse(res.data.response);
    };

    return (
        <div>
            <textarea
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask the AI anything..."
            />
            <button onClick={handleSubmit}>Send</button>
            <p>{response}</p>
        </div>
    );
}

export default AIChat;
