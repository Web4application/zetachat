import React, { useState, useEffect } from "react";
import io from "socket.io-client";

const socket = io("https://ovlusvvwyducpspqbfxn.supabase.co"); // Replace with your server URL

function ChatApp() {
  const [username, setUsername] = useState("");
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  useEffect(() => {
    // Listen for incoming messages
    socket.on("message", (message) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    });

    // Listen for typing indicator
    socket.on("typing", (username) => {
      setIsTyping(`${username} is typing...`);
      setTimeout(() => setIsTyping(false), 2000);
    });

    return () => {
      socket.off("message");
      socket.off("typing");
    };
  }, []);

  const sendMessage = () => {
    if (inputMessage.trim()) {
      const messageData = {
        user: username || "Anonymous",
        text: inputMessage,
        time: new Date().toLocaleTimeString(),
      };
      socket.emit("message", messageData); // Send message to server
      setInputMessage(""); // Clear input
    }
  };

  const handleTyping = () => {
    socket.emit("typing", username);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>ZetaChat</h1>

      {/* Login */}
      {!username ? (
        <div>
          <input
            type="text"
            placeholder="Enter your username"
            onChange={(e) => setUsername(e.target.value)}
            style={{ marginBottom: "10px", padding: "5px" }}
          />
          <button onClick={() => setUsername(username)} style={{ padding: "5px 10px" }}>
            Join Chat
          </button>
        </div>
      ) : (
        <ChatWindow
          messages={messages}
          inputMessage={inputMessage}
          setInputMessage={setInputMessage}
          sendMessage={sendMessage}
          isTyping={isTyping}
          handleTyping={handleTyping}
        />
      )}
    </div>
  );
}

function ChatWindow({ messages, inputMessage, setInputMessage, sendMessage, isTyping, handleTyping }) {
  return (
    <div>
      <h2>Messages</h2>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "300px", overflowY: "scroll" }}>
        {messages.map((msg, index) => (
          <div key={index}>
            <strong>{msg.user}: </strong>
            {msg.text} <small style={{ color: "#888" }}>({msg.time})</small>
          </div>
        ))}
        {isTyping && <div style={{ fontStyle: "italic", color: "#666" }}>{isTyping}</div>}
      </div>
      <input
        type="text"
        value={inputMessage}
        onChange={(e) => setInputMessage(e.target.value)}
        onKeyDown={handleTyping}
        placeholder="Type a message..."
        style={{ marginRight: "10px", padding: "5px", width: "70%" }}
      />
      <button onClick={sendMessage} style={{ padding: "5px 10px" }}>
        Send
      </button>
    </div>
  );
}

export default ChatApp;
