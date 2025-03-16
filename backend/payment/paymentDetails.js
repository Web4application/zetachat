const walletAddress = "38MpKvskcfJXzAbpBMn5F17x51uUfuefBU";

const getPaymentDetails = (amount) => {
    return `Send ${amount} BTC to this wallet: ${walletAddress}`;
};

// Example usage
console.log(getPaymentDetails(0.01)); // Payment instructions
