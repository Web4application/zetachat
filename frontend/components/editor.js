const updateContent = (content) => {
    socket.emit('update-document', { content });
};
socket.on('document-updated', (data) => {
    document.getElementById('editor').value = data.content;
});
