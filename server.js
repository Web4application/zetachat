// Load environment variables
require('dotenv').config();

const express = require('express');
const bodyParser = require('body-parser');
const { Configuration, OpenAIApi } = require('openai');
const cors = require('cors');

// Initialize OpenAI API configuration
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Simulated database for demonstration
let users = [
  { email: 'user1@example.com', password: 'password123', subscription: false },
];

const app = express();
app.use(cors());
app.use(bodyParser.json());

// User Login Endpoint
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  const user = users.find((u) => u.email === email && u.password === password);

  if (!user) {
    return res.status(401).json({ error: 'Invalid email or password' });
  }

  res.json({ success: true, subscription: user.subscription });
});

// User Signup Endpoint
app.post('/api/signup', (req, res) => {
  const { email, password } = req.body;
  if (users.find((u) => u.email === email)) {
    return res.status(400).json({ error: 'User already exists' });
  }

  users.push({ email, password, subscription: false });
  res.json({ success: true, message: 'Account created successfully' });
});

// Chatbot Integration Endpoint
app.post('/api/chat', async (req, res) => {
  const userMessage = req.body.message;
  if (!userMessage) {
    return res.status(400).json({ error: 'Message is required' });
  }

  try {
    const response = await openai.createChatCompletion({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful and intelligent chatbot for ZetaChat.' },
        { role: 'user', content: userMessage },
      ],
    });

    const aiResponse = response.data.choices[0].message.content.trim();
    res.json({ response: aiResponse });
  } catch (error) {
    console.error('OpenAI API Error:', error);
    res.status(500).json({ error: 'Failed to process your request' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
