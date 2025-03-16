const axios = require('axios');

const postToInstagram = async (imageUrl, caption, accessToken) => {
    const url = 'https://graph.facebook.com/v12.0/{instagram_account_id}/media';
    const response = await axios.post(url, {
        image_url: imageUrl,
        caption: caption,
        access_token: accessToken,
    });
    console.log('Posted to Instagram:', response.data);
};
postToInstagram('https://example.com/image.jpg', 'Hello from Zetachat!', 'your-access-token');
