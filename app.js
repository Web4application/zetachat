const express = require('express');
const app = express();

// Zetachat Routes
const zetachatRoutes = require('./routes/zetachat');
app.use('/zetachat', zetachatRoutes);

// Start server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${8080}`);
});
