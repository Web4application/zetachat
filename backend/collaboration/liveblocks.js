const liveblocks = require('@liveblocks/server');
const liveblocksClient = new liveblocks.ServerClient({
    secret: 'your-liveblocks-api-key',
});

const room = liveblocksClient.rooms.create('your-room-id', { user: 'User123' });
console.log('Room created:', room);
