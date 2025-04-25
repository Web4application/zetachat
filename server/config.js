const { Configuration, OpenAIApi } = require('openai');

const configuration = new Configuration({
    apiKey: process.env.AIzaSyAvrxOyAVzPVcnzxuD0mjKVDyS2bNWfC10, // Store this securely
});
const openai = new OpenAIApi(configuration);

app.post('/ai-response', async (req, res) => {
    const userMessage = req.body.message;

    try {
        const response = await openai.createChatCompletion({
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: userMessage }],
        });

        res.json({ response: response.data.choices[0].message.content });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});
