const Twitter = require('twitter');

const twitterClient = new Twitter({
    consumer_key: 'your-consumer-key',
    consumer_secret: 'your-consumer-secret',
    access_token_key: 'your-access-token',
    access_token_secret: 'your-access-token-secret',
});

const postTweet = async (status) => {
    const response = await twitterClient.post('statuses/update', { status });
    console.log('Tweet posted:', response);
};
postTweet('Hello from Zetachat!');
