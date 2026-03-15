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
const mCanvas = document.getElementById('matrix-canvas');
const sCanvas = document.getElementById('stars-canvas');
const mCtx = mCanvas.getContext('2d');
const sCtx = sCanvas.getContext('2d');

let w, h;
const resize = () => {
  w = mCanvas.width = sCanvas.width = window.innerWidth;
  h = mCanvas.height = sCanvas.height = window.innerHeight;
};
window.onresize = resize;
resize();

// Matrix Data Settings
const chars = "0101ΣΔΩΨ";
const drops = Array(Math.floor(w / 20)).fill(1);

// Star Particle Settings
const stars = Array.from({ length: 100 }, () => ({
  x: Math.random() * w, y: Math.random() * h, s: Math.random() * 2
}));

function animate() {
  // Matrix Rain
  mCtx.fillStyle = "rgba(0, 0, 0, 0.05)";
  mCtx.fillRect(0, 0, w, h);
  mCtx.fillStyle = "#00f2ff";
  drops.forEach((y, i) => {
    mCtx.fillText(chars[Math.floor(Math.random() * chars.length)], i * 20, y * 20);
    if (y * 20 > h && Math.random() > 0.975) drops[i] = 0;
    drops[i]++;
  });

  // Floating Stars
  sCtx.clearRect(0, 0, w, h);
  sCtx.fillStyle = "#fff";
  stars.forEach(star => {
    sCtx.beginPath();
    sCtx.arc(star.x, star.y, star.s, 0, Math.PI * 2);
    sCtx.fill();
    star.y -= 0.5; // Stars float upward
    if (star.y < 0) star.y = h;
  });

  requestAnimationFrame(animate);
}
animate();

