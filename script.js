// Establish WebSocket Connection
const socket = io('http://localhost:5000');

// DOM Elements
const chatForm = document.getElementById('chat-form');
const chatMessages = document.getElementById('chat-messages');
const aiForm = document.getElementById('ai-form');
const aiResponse = document.getElementById('ai-response');

// Handle Real-Time Chat
socket.on('chatMessage', (message) => {
    const div = document.createElement('div');
    div.classList.add('message');
    div.innerHTML = `<p>${message}</p>`;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll
});

// Send Chat Message
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const messageInput = document.getElementById('chat-input');
    const message = messageInput.value;

    if (message) {
        socket.emit('chatMessage', message);
        messageInput.value = ''; // Clear input
    }
});

// AI-Powered Chat Response
aiForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const aiInput = document.getElementById('ai-input').value;

    if (aiInput) {
        const res = await fetch('http://localhost:5000/ai-response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: aiInput }),
        });

        const data = await res.json();
        aiResponse.innerHTML = `<p>${data.response}</p>`;
    }
});

// Utility: Display Notifications
function notifyUser(message) {
    const notification = document.createElement('div');
    notification.classList.add('notification');
    notification.innerText = message;
    document.body.appendChild(notification);
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Push Notifications Handling (Optional)
async function subscribeToNotifications() {
    if ('serviceWorker' in navigator) {
        const registration = await navigator.serviceWorker.register('/sw.js');
        const subscription = await registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: 'YOUR_PUBLIC_VAPID_KEY',
        });

        await fetch('http://localhost:5000/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(subscription),
        });
        notifyUser('Subscribed to notifications!');
    }
}

// Call subscription function if needed
subscribeToNotifications();
