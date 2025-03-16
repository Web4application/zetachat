// Middleware to check subscription status
const checkSubscription = async (req, res, next) => {
  const { userId } = req; // Assume userId is available from authentication token

  try {
    // Fetch user from database
    const user = await User.findByPk(userId);

    // Check if the user exists and is subscribed
    if (!user) {
      return res.status(404).json({ message: "User not found!" });
    }

    if (!user.isSubscribed) {
      // If the user's subscription is inactive, deny access
      return res.status(403).json({
        message: "Access denied. Please subscribe to continue.",
        subscribeLink: "your-subscription-page-link", // Optional: Link to subscription page
      });
    }

    // Allow access if subscribed
    next();
  } catch (error) {
    console.error("Error checking subscription:", error);
    res.status(500).json({ message: "Internal server error." });
  }
};

// Example usage in a route
app.use("/zetachat", checkSubscription, (req, res) => {
  res.json({ message: "Welcome to Zetachat!" });
});
