const twilio = require('twilio');
const client = new twilio('account_sid', 'auth_token');

client.messages
    .create({
        body: 'Hello from Zetachat!',
        from: 'whatsapp:+14155238886', // Twilio WhatsApp number
        to: 'whatsapp:+2341234567890', // Recipient's number
    })
    .then((message) => console.log(message.sid));
