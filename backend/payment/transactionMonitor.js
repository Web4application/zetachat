const axios = require('axios');

const monitorWalletTransactions = async () => {
    const walletAddress = "your-bitcoin-wallet-address";
    const response = await axios.get(`https://blockchain.info/rawaddr/${walletAddress}`);
    console.log("Transactions:", response.data.txs); // List of transactions
};

// Call the function to check transactions
monitorWalletTransactions();
