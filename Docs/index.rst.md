<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="ZetaChat - Connect seamlessly with friends and social media">
  <title>ZetaChat</title>
  <link rel="stylesheet" href="styles.css">
  <script src="scripts/zetachat.js" defer></script> <!-- Add your JavaScript file -->
</head>
<body>
  <!-- Main Container -->
  <div id="main-container">
    
    <!-- Sign-Up Page -->
    <section id="signup-page">
      <h1>ZetaChat Sign-Up</h1>
      <form id="signup-form">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" placeholder="Enter your password" required>
        <button type="submit">Sign Up</button>
      </form>
    </section>

    <!-- Profile Setup Page -->
    <section id="profile-page" style="display: none;">
      <h1>Profile Setup</h1>
      <form id="profile-form">
        <label for="fullname">Full Name:</label>
        <input type="text" id="fullname" name="fullname" placeholder="Enter your full name" required>

        <label for="age">Age:</label>
        <input type="number" id="age" name="age" placeholder="Enter your age" required>

        <label for="gender">Gender:</label>
        <select id="gender" name="gender" required>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" placeholder="Enter your address" required>

        <label for="country">Country:</label>
        <input type="text" id="country" name="country" placeholder="Enter your country" required>

        <label for="occupation">Occupation:</label>
        <input type="text" id="occupation" name="occupation" placeholder="Enter your occupation" required>

        <label for="status">Public Status:</label>
        <select id="status" name="status" required>
          <option value="">Select Status</option>
          <option value="artist">Artist</option>
          <option value="musician">Musician</option>
          <option value="manager">Manager</option>
          <option value="comedian">Comedian</option>
          <option value="other">Other</option>
        </select>

        <button type="submit">Save Profile</button>
      </form>
    </section>

    <!-- Social Media Integration Page -->
    <section id="social-media-page" style="display: none;">
      <h1>Social Media Integration</h1>
      <p>Choose the platforms you want to sync with ZetaChat:</p>
      <form id="social-media-form">
        <div>
          <input type="checkbox" id="whatsapp" name="social-media" value="whatsapp">
          <label for="whatsapp">WhatsApp</label>
        </div>
        <div>
          <input type="checkbox" id="twitter" name="social-media" value="twitter">
          <label for="twitter">Twitter</label>
        </div>
        <div>
          <input type="checkbox" id="instagram" name="social-media" value="instagram">
          <label for="instagram">Instagram</label>
        </div>
        <div>
          <input type="checkbox" id="facebook" name="social-media" value="facebook">
          <label for="facebook">Facebook</label>
        </div>
        <div>
          <input type="checkbox" id="discord" name="social-media" value="discord">
          <label for="discord">Discord</label>
        </div>
        <div>
          <input type="checkbox" id="telegram" name="social-media" value="telegram">
          <label for="telegram">Telegram</label>
        </div>
        <button type="submit">Sync Platforms</button>
      </form>
    </section>

  </div>

  <!-- JavaScript Logic -->
  <script>
    // Handle Sign-Up Form Submission
    document.getElementById('signup-form').addEventListener('submit', (e) => {
      e.preventDefault();
      // Simulate account creation and move to profile setup
      document.getElementById('signup-page').style.display = 'none';
      document.getElementById('profile-page').style.display = 'block';
    });

    // Handle Profile Setup Form Submission
    document.getElementById('profile-form').addEventListener('submit', (e) => {
      e.preventDefault();
      // Simulate saving profile and move to social media integration
      document.getElementById('profile-page').style.display = 'none';
      document.getElementById('social-media-page').style.display = 'block';
    });

    // Handle Social Media Integration Form Submission
    document.getElementById('social-media-form').addEventListener('submit', (e) => {
      e.preventDefault();
      const selectedPlatforms = [];
      document.querySelectorAll('input[name="social-media"]:checked').forEach((checkbox) => {
        selectedPlatforms.push(checkbox.value);
      });
      console.log('Selected Platforms:', selectedPlatforms);
      alert('Social media platforms synced successfully!');
    });
  </script>
</body>
</html>


NEXT_PUBLIC_SUPABASE_URL=https://ovlusvvwyducpspqbfxn.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im92bHVzdnZ3eWR1Y3BzcHFiZnhuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzYxOTY5MjMsImV4cCI6MjA1MTc3MjkyM30.Rsmd3VxO4DPf-xkVVekRwHptO0Ey8n-XVVGvX0zVYVI
OPENAI_API_KEY=qusDmXVuflS2UgVbtNoxT3BlbkFJdB1IU0OFhSmKkTfBQpAo

https://gkkxjkbsqluqosrapiru.supabase.co

API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imdra3hqa2JzcWx1cW9zcmFwaXJ1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA5OTIwMDEsImV4cCI6MjA3NjU2ODAwMX0.fg1xwVS90kDQCx7MC53mltooPBrnVexRZkRM26kgW-U

xXj0y119zVg3M2Tg

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
