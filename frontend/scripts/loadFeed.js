document.addEventListener("DOMContentLoaded", async () => {
  const feedContainer = document.querySelector('.feed');

  try {
    // Fetch feed data from the backend
    const response = await fetch('/api/feed');
    const feedData = await response.json();

    // Clear the placeholder text
    feedContainer.innerHTML = '';

    // Populate the feed dynamically
    feedData.forEach(item => {
      const feedItem = document.createElement('div');
      feedItem.textContent = item.content;
      feedContainer.appendChild(feedItem);
    });
  } catch (error) {
    console.error("Error loading feed:", error);
    feedContainer.textContent = "Failed to load feed. Please try again later.";
  }
});
