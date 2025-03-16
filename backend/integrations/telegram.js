const TelegramBot = require('node-telegram-bot-api');
const bot = new TelegramBot('your-telegram-bot-token', { polling: true });

bot.on('message', (msg) => {
    bot.sendMessage(msg.chat.id, `Hello from Zetachat!`);
});
