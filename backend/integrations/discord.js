const discordClient = require('discord.js');
const client = new discordClient.Client();

client.on('message', (message) => {
    if (message.content === 'Hello Zetachat') {
        message.reply('Hello from Zetachat!');
    }
});

client.login('qzKvJpweA4');
