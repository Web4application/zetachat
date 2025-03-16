const express = require('express');
const app = express();

app.get('/api/feed', (req, res) => {
  const feedData = [
    { id: 1, content: "Welcome to Zetachat!" },
    { id: 2, content: "Your personalized updates are here." },
    { id: 3, content: "Check out the latest from your contacts." }
  ];
  res.json(feedData);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
