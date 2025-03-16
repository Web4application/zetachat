const axios = require('axios');

const postToFacebook = async (message, accessToken) => {
    const url = 'https://graph.facebook.com/v12.0/me/feed';
    const response = await axios.post(url, {
        message: message,
        access_token: accessToken,
    });
    console.log('Posted to Facebook:', response.data);
};
postToFacebook('Hello from Zetachat!', 'your-access-token');
