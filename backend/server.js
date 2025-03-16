// Load environment variables from .env file
require('dotenv').config();

// Import necessary libraries
const express = require('express');
const { Configuration, OpenAIApi } = require('openai');

// Initialize OpenAI API configuration
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY, // Securely access API key
});
const openai = new OpenAIApi(configuration);

// Create an Express app
const app = express();
app.use(express.json());

// Endpoint to handle chat messages
app.post('/chat', async (req, res) => {
  const userMessage = req.body.message;

  // Check if the user sent a message
  if (!userMessage) {
    return res.status(400).json({ error: 'Message is required' });
  }

  try {
    // Send user message to OpenAI GPT-4 and get AI response
    const response = await openai.createChatCompletion({
      model: 'gpt-4',
      messages: [
        { role: 'system', content: 'You are a helpful and intelligent chatbot for Zetachat.' },
        { role: 'user', content: userMessage },
      ],
    });

    // Extract the AI's response from the API
    const aiResponse = response.data.choices[0].message.content.trim();

    // Send the AI's response back to the client
    res.json({ response: aiResponse });
  } catch (error) {
    console.error('Error with OpenAI API:', error);
    res.status(500).json({ error: 'An error occurred while processing your request' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000; // Use PORT from .env or default to 3000
app.listen(PORT, () => {
  console.log(`Zetachat AI server is running on port ${PORT}`);
});
