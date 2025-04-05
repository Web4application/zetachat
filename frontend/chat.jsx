import React from "react";

function ChatApp() {
  return (
    <div>
      <h1> zetachat </h1>
      <ChatWindow />
    </div>
  );
}

function ChatWindow() {
  return (
    <div>
      <h2>Messages</h2>
      <ul>
        <li>Hello!</li>
        <li>How are you?</li>
      </ul>
      <input type="text" placeholder="Type a message..." />
      <button>Send</button>
    </div>
  );
}

export default ChatApp;
