import React, { useState, useEffect } from "react";
import io from "socket.io-client";
import { Picker } from "emoji-mart"; // Emoji picker
import {
  formatTimestamp,
  generateRandomUsername,
  validateMessage,
  handleReconnection,
  typingIndicator,
  suggestEmoji,
  signupUser,
  loginUser,
} from "./utils/Otherscript"; // Import utility functions

const socket = io("http://web4-86e33.firebaseapp.com"); // Replace with your server URL

function App() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isTyping, setIsTyping] = useState("");
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);

  useEffect(() => {
    // Load messages from server
    socket.emit("join");
    socket.on("load-messages", (savedMessages) => {
      const formattedMessages = savedMessages.map((msg) => ({
        ...msg,
        time: formatTimestamp(msg.time),
      }));
      setMessages(formattedMessages);
    });

    // Listen for new messages
    socket.on("message", (message) => {
      setMessages((prevMessages) => [
        ...prevMessages,
        { ...message, time: formatTimestamp(message.time) },
      ]);
    });

    // Listen for typing indicator
    socket.on("typing", (username) => {
      setIsTyping(typingIndicator(username));
      setTimeout(() => setIsTyping(""), 2000); // Clear typing indicator after 2 seconds
    });

    // Handle reconnections
    handleReconnection(socket);

    return () => {
      socket.off("message");
      socket.off("typing");
      socket.off("load-messages");
    };
  }, []);

  const sendMessage = () => {
    if (validateMessage(inputMessage)) {
      const messageData = {
        user: username || generateRandomUsername(),
        text: inputMessage,
        time: new Date(),
      };
      socket.emit("message", messageData); // Send message to server
      setInputMessage(""); // Clear input field
    } else {
      alert("Please enter a valid message!");
    }
  };

  const handleTyping = () => {
    socket.emit("typing", username);
  };

  const addEmoji = (emoji) => {
    setInputMessage(inputMessage + emoji.native);
    setShowEmojiPicker(false);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1 style={{ textAlign: "center" }}>ZetaChat</h1>

      {/* Authentication Section */}
      {!username ? (
        <div>
          <div style={{ marginBottom: "10px" }}>
            <input
              type="email"
              placeholder="Enter your email"
              onChange={(e) => setEmail(e.target.value)}
              style={{ marginRight: "10px", padding: "5px", width: "70%" }}
            />
            <input
              type="password"
              placeholder="Enter your password"
              onChange={(e) => setPassword(e.target.value)}
              style={{ marginRight: "10px", padding: "5px", width: "70%" }}
            />
            <button
              onClick={() => signupUser(email, password)}
              style={{
                marginRight: "10px",
                padding: "5px 10px",
                background: "green",
                color: "white",
              }}
            >
              Sign Up
            </button>
            <button
              onClick={() => loginUser(email, password)}
              style={{ padding: "5px 10px", background: "blue", color: "white" }}
            >
              Login
            </button>
          </div>
          <input
            type="text"
            placeholder="Enter your username"
            onChange={(e) => setUsername(e.target.value)}
            style={{
              marginBottom: "10px",
              padding: "5px",
              fontSize: "16px",
              width: "70%",
            }}
          />
          <button onClick={() => setUsername(username)} style={{ padding: "5px 10px" }}>
            Join Chat
          </button>
        </div>
      ) : (
        <div>
          {/* Chat Messages */}
          <div
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              height: "300px",
              overflowY: "scroll",
              marginBottom: "10px",
            }}
          >
            {messages.map((msg, index) => (
              <div key={index}>
                <strong>{msg.user}:</strong> {msg.text}{" "}
                <small style={{ color: "#888" }}>({msg.time})</small>
              </div>
            ))}
          </div>

          {/* Typing Indicator */}
          {isTyping && (
            <div style={{ fontStyle: "italic", color: "#666", marginBottom: "10px" }}>
              {isTyping}
            </div>
          )}

          {/* Message Input */}
          <div style={{ marginBottom: "10px" }}>
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyDown={handleTyping}
              placeholder="Type a message..."
              style={{
                padding: "5px",
                fontSize: "16px",
                width: "70%",
                marginRight: "10px",
              }}
            />
            <button onClick={sendMessage} style={{ padding: "5px 10px" }}>
              Send
            </button>
            <button onClick={() => setShowEmojiPicker(!showEmojiPicker)} style={{ marginLeft: "10px" }}>
              😀
            </button>
            {showEmojiPicker && <Picker onSelect={addEmoji} />}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
