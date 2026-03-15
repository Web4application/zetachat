import { DiscordSDK } from "@discord/embedded-app-sdk";

const discordSdk = new DiscordSDK(import.meta.env.VITE_DISCORD_CLIENT_ID);

document.querySelector('#app').innerHTML = `
  <div class="glass-container">
    <div class="chat-window" id="chat">
      <div class="message">SYSTEM: Initialization complete. Welcome to Web4Chat.</div>
    </div>
    <div class="input-area">
      <input type="text" id="msgInput" placeholder="Transmit data..." />
      <button id="sendBtn">Send</button>
    </div>
  </div>
`;

// Simple function to add messages with a "glitch" or smooth effect
function addMessage(text, isUser = false) {
  const chat = document.getElementById('chat');
  const msg = document.createElement('div');
  msg.className = `message ${isUser ? 'user' : ''}`;
  msg.innerText = text;
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
}

document.getElementById('sendBtn').onclick = () => {
  const input = document.getElementById('msgInput');
  if (input.value) {
    addMessage(input.value, true);
    input.value = '';
  }
};
