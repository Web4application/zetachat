async function sendMessageToAI(userMessage) {
  try {
    const response = await fetch('http://localhost:3000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userMessage }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    return data.response; // AI response
  } catch (error) {
    console.error('Error communicating with AI:', error);
    return 'Sorry, I encountered an issue. Please try again later.';
  }
}

export default sendMessageToAI;
