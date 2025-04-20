const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const app = express();
const users = [];  // This should be replaced with a database in production

app.use(express.json());

// Register User
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    users.push({ username, password: hashedPassword });
    res.send('User registered');
});

// Login User
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = users.find((user) => user.username === username);

    if (!user) return res.status(400).send('User not found');

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) return res.status(400).send('Invalid credentials');

    const token = jwt.sign({ username: user.username }, 'your-secret-key', { expiresIn: '1h' });
    res.json({ token });
});

// Protected Route
app.get('/dashboard', (req, res) => {
    const token = req.headers['authorization'];
    if (!token) return res.status(403).send('Token is required');

    jwt.verify(token, 'your-secret-key', (err, decoded) => {
        if (err) return res.status(403).send('Invalid token');
        res.send(`Hello ${decoded.username}, welcome to your dashboard!`);
    });
});

app.listen(5000, () => {
    console.log('Server running on port 5000');
});
