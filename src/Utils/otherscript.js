// Utility functions for ZetaChat

// Format timestamps for messages
export const formatTimestamp = (date) => {
  const options = { hour: '2-digit', minute: '2-digit', second: '2-digit' };
  return new Date(date).toLocaleTimeString(undefined, options);
};

// Generate a random username (if none is provided)
export const generateRandomUsername = () => {
  const adjectives = ['Cool', 'Fast', 'Smart', 'Happy', 'Bright'];
  const nouns = ['Tiger', 'Eagle', 'Shark', 'Lion', 'Wolf'];
  const randomAdjective = adjectives[Math.floor(Math.random() * adjectives.length)];
  const randomNoun = nouns[Math.floor(Math.random() * nouns.length)];
  return `${randomAdjective}${randomNoun}${Math.floor(Math.random() * 100)}`;
};

// Validate message input
export const validateMessage = (message) => {
  if (!message || message.trim() === '') {
    return false;
  }
  return true;
};

// Configuration for server connection
export const serverConfig = {
  url: 'https://your-server-url', // Replace with your server URL
  reconnectInterval: 5000, // Time in ms to attempt reconnection
};

// Function to handle reconnection logic
export const handleReconnection = (socket) => {
  socket.on('disconnect', () => {
    console.log('Disconnected from server. Attempting to reconnect...');
    setTimeout(() => {
      socket.connect();
    }, serverConfig.reconnectInterval);
  });
};

// Emoji utilities
export const emojis = ['😀', '😂', '😍', '👍', '🤔', '😎', '😢', '🔥'];
export const suggestEmoji = (keyword) => {
  const emojiMap = {
    happy: '😀',
    funny: '😂',
    love: '😍',
    cool: '😎',
    sad: '😢',
  };
  return emojiMap[keyword.toLowerCase()] || '🤔';
};

// Typing indicator
export const typingIndicator = (username) => `${username} is typing...`;

// Firebase Authentication utilities
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth';

export const firebaseAuth = getAuth();
export const signupUser = async (email, password) => {
  try {
    await createUserWithEmailAndPassword(firebaseAuth, email, password);
    alert('Signup successful!');
  } catch (error) {
    console.error(error.message);
    alert('Signup failed!');
  }
};

export const loginUser = async (email, password) => {
  try {
    await signInWithEmailAndPassword(firebaseAuth, email, password);
    alert('Login successful!');
  } catch (error) {
    console.error(error.message);
    alert('Login failed!');
  }
};
