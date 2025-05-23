import { io } from 'socket.io-client';

const socket = io('http://localhost:5000'); // WebSocket server URL
export default socket;
