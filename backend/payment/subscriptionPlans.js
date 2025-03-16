// Define subscription plans in USD
const subscriptionPlans = {
  monthly: {
    amountUSD: 30, // Monthly price in USD
    description: "Access for one month",
  },
  yearly: {
    amountUSD: 300, // Yearly price in USD (discounted)
    description: "Access for one year (Save $60)",
  },
};

// Define Bitcoin wallet address
const bitcoinWalletAddress = "38MpKvskcfJXzAbpBMn5F17x51uUfuefBU"; // Replace with your wallet address

// Track user trial status
const users = {}; // Simulating a database of users with trial status

// Function to check trial status or show subscription details
const getAccessDetails = (userID, plan) => {
  if (!users[userID]) {
    // Start a 7-day trial for the user
    users[userID] = { trialEnd: Date.now() + 7 * 24 * 60 * 60 * 1000 }; // 7 days in milliseconds
    return `Welcome to your 7-day trial! Enjoy full access until ${new Date(
      users[userID].trialEnd
    ).toLocaleString()}. After the trial, you can subscribe as follows:\n\nPlan: ${plan.toUpperCase()}\nAmount: $${subscriptionPlans[plan].amountUSD} USD\nDescription: ${subscriptionPlans[plan].description}\n\nTo subscribe:\n1. Copy this Bitcoin address: ${bitcoinWalletAddress}\n2. Send the equivalent BTC to this address.\n3. Once payment is confirmed, your subscription will be activated.`;
  } else if (Date.now() > users[userID].trialEnd) {
    // Trial has ended
    return `Your 7-day trial has ended. To continue using the service, please subscribe:\n\nPlan: ${plan.toUpperCase()}\nAmount: $${subscriptionPlans[plan].amountUSD} USD\nDescription: ${subscriptionPlans[plan].description}\n\nTo subscribe:\n1. Copy this Bitcoin address: ${bitcoinWalletAddress}\n2. Send the equivalent BTC to this address.\n3. Once payment is confirmed, your subscription will be activated.`;
  } else {
    // Trial is still active
    return `Your trial is still active! Enjoy full access until ${new Date(
      users[userID].trialEnd
    ).toLocaleString()}.`;
  }
};

// Example usage
const userID = "user123"; // Example user ID
console.log(getAccessDetails(userID, "monthly"));
