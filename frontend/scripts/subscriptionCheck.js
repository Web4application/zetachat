// Function to check subscription status
const checkSubscriptionStatus = async (userId) => {
  try {
    // Make a request to the backend to check subscription status
    const response = await fetch(`/api/check-subscription?userId=${userId}`);
    const data = await response.json();

    if (response.status === 403) {
      // User is unauthorized or trial has expired
      alert(data.message); // Display access denial message
      window.location.href = data.subscribeLink; // Redirect to the subscription page
    } else {
      // User is authorized
      console.log("Welcome to Zetachat! Subscription is active.");
    }
  } catch (error) {
    console.error("Error checking subscription status:", error);
  }
};

// Example usage
const userId = "user123"; // Replace with the logged-in user's ID
checkSubscriptionStatus(userId);
