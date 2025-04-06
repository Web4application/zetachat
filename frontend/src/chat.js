import React, { useState, useEffect } from 'react';
import { io } from 'socket.io-client';

const socket = io('http://localhost:5000');

function Chat() {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        socket.on('chatMessage', (msg) => {
            setMessages((prev) => [...prev, msg]);
        });
    }, []);

    const sendMessage = () => {
        socket.emit('chatMessage', message);
        setMessage('');
    };

    return (
        <div>
            <ul>
                {messages.map((msg, index) => (
                    <li key={index}>{msg}</li>
                ))}
            </ul>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
}

export default Chat;
