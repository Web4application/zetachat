const { WebClient } = require('@slack/web-api');
const slackClient = new WebClient('your-slack-bot-token');

const sendSlackMessage = async (channel, message) => {
    await slackClient.chat.postMessage({
        channel: channel,
        text: message,
    });
};
sendSlackMessage('#general', 'Hello from Zetachat!');
