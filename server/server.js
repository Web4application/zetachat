// server.js
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
require('dotenv').config();

const app = express();
const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: '*', // Adjust to restrict origins in production
    methods: ['GET', 'POST']
  }
});

// Basic route just to confirm the server is running
app.get('/', (req, res) => {
  res.send('Real-time chat server is running.');
});

// Listen for new connections
io.on('connection', (socket) => {
  console.log('New user connected:', socket.id);

  // Listen for incoming chat messages
  socket.on('chat message', (msg) => {
    console.log(`Message from ${socket.id}:`, msg);
    // Broadcast the received message to all connected clients
    io.emit('chat message', msg);
  });

  // Handle disconnections
  socket.on('disconnect', () => {
    console.log('User disconnected:', socket.id);
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
