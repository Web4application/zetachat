// Import required modules
import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import { Picker } from 'emoji-mart'; // Emoji picker
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth';

// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Connect to the chat server
const socket = io('https://your-server-url'); // Replace with your backend server URL

const App = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [userTyping, setUserTyping] = useState('');
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);

  // Load saved messages from the backend
  useEffect(() => {
    socket.emit('join');
    socket.on('load-messages', (savedMessages) => {
      setMessages(savedMessages);
    });

    // Listen for new messages
    socket.on('message', (message) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    // Listen for typing events
    socket.on('typing', (username) => {
      setUserTyping(`${username} is typing...`);
      setTimeout(() => setUserTyping(''), 2000); // Clear typing indicator after 2 seconds
    });

    return () => {
      socket.off('message');
      socket.off('typing');
      socket.off('load-messages');
    };
  }, []);

  // Emit message to server
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

  // Handle typing event
  const handleTyping = () => {
    socket.emit('typing', username);
  };

  // Add emoji to the input field
  const addEmoji = (emoji) => {
    setInputMessage(inputMessage + emoji.native);
    setShowEmojiPicker(false);
  };

  // Handle user signup
  const handleSignup = async () => {
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      alert("Signup successful!");
    } catch (error) {
      console.error(error.message);
      alert("Signup failed!");
    }
  };

  // Handle user login
  const handleLogin = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      alert("Login successful!");
    } catch (error) {
      console.error(error.message);
      alert("Login failed!");
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1 style={{ textAlign: 'center' }}>ZetaChat</h1>

      {/* Authentication Section */}
      {!username ? (
        <div>
          <div style={{ marginBottom: '10px' }}>
            <input
              type="email"
              placeholder="Enter your email"
              onChange={(e) => setEmail(e.target.value)}
              style={{ marginRight: '10px', padding: '5px', width: '70%' }}
            />
            <input
              type="password"
              placeholder="Enter your password"
              onChange={(e) => setPassword(e.target.value)}
              style={{ marginRight: '10px', padding: '5px', width: '70%' }}
            />
            <button onClick={handleSignup} style={{ marginRight: '10px', padding: '5px 10px', background: 'green', color: 'white' }}>
              Sign Up
            </button>
            <button onClick={handleLogin} style={{ padding: '5px 10px', background: 'blue', color: 'white' }}>
              Login
            </button>
          </div>
          <input
            type="text"
            placeholder="Enter your username"
            onChange={(e) => setUsername(e.target.value)}
            style={{ marginBottom: '10px', padding: '5px', fontSize: '16px', width: '70%' }}
          />
          <button onClick={() => setUsername(username)} style={{ padding: '5px 10px' }}>
            Join Chat
          </button>
        </div>
      ) : (
        <div>
          {/* Chat Messages */}
          <div style={{ border: '1px solid #ccc', padding: '10px', height: '300px', overflowY: 'scroll', marginBottom: '10px' }}>
            {messages.map((msg, index) => (
              <div key={index}>
                <strong>{msg.user}: </strong>
                {msg.text} <small style={{ color: '#888' }}>({msg.time})</small>
              </div>
            ))}
          </div>

          {/* Typing Indicator */}
          {userTyping && <div style={{ fontStyle: 'italic', color: '#666', marginBottom: '10px' }}>{userTyping}</div>}

          {/* Message Input */}
          <div style={{ marginBottom: '10px' }}>
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyDown={handleTyping}
              placeholder="Type a message"
              style={{ padding: '5px', fontSize: '16px', width: '70%' }}
            />
            <button onClick={sendMessage} style={{ padding: '5px 10px', marginLeft: '10px', background: 'blue', color: 'white' }}>
              Send
            </button>
            <button onClick={() => setShowEmojiPicker(!showEmojiPicker)} style={{ marginLeft: '10px' }}>😀</button>
            {showEmojiPicker && <Picker onSelect={addEmoji} />}
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
