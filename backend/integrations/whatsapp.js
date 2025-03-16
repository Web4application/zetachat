const axios = require('axios');

const sendMessage = async (phoneNumber, message) => {
    const response = await axios.post(
        'https://graph.facebook.com/v12.0/{your-phone-id}/messages',
        {
            messaging_product: 'whatsapp',
            to: phoneNumber,
            text: { body: message },
        },
        {
            headers: {
                Authorization: `Bearer your-access-token`,
                'Content-Type': 'application/json',
            },
        }
    );
    console.log('Message sent:', response.data);
};

sendMessage('2341234567890', 'Hello from Zetachat!');
