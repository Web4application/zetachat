const sendFileMessage = async (fileUrl) => {
    // Logic to send the file's URL as a message in the chat
    await addChatMessage({
        type: "file",
        content: fileUrl,
        sender: "User123",
        timestamp: Date.now(),
    });
};
