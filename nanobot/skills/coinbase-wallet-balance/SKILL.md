```skill
---
name: coinbase-wallet-balance
description: Retrieves the current balance of a specified Coinbase wallet.
metadata:
  nanobot:
    emoji: 💰
    category: finance
    tags: [coinbase, wallet, balance, cryptocurrency]
---

## Coinbase Wallet Balance Skill

This skill allows the nanobot to query the current balance of a Coinbase wallet.

**Instructions:**

1.  **Authentication:** This skill requires authentication with the Coinbase API.  Assume the nanobot has access to a secure key store containing a Coinbase API key and secret.  Retrieve these credentials.
2.  **Wallet Identification:** The user will provide a wallet ID or email address associated with the Coinbase account.  Validate the input to ensure it's a valid format (either a Coinbase Wallet ID or a valid email address).
3.  **API Request:** Construct a GET request to the Coinbase API endpoint for retrieving account balances. The endpoint is typically `/accounts`.  Include the API key and secret in the request headers for authentication.
4.  **Data Parsing:** Parse the JSON response from the Coinbase API.  Locate the account associated with the provided wallet ID or email address.
5.  **Balance Extraction:** Extract the current balance of the specified account from the JSON response.  The balance will be represented in the account's base currency (e.g., USD).
6.  **Response Formatting:** Format the balance into a human-readable string, including the currency symbol. For example: "Your Coinbase wallet balance is $1234.56".
7.  **Error Handling:** Implement robust error handling.  If the API request fails, or if the account is not found, return an appropriate error message to the user.  Common errors include invalid API keys, rate limiting, and account not found.
8.  **Security:**  Never store the API key and secret in plain text. Utilize the secure key store for retrieval and management.

**Example Interaction:**

*   **User:** "What's my Coinbase balance?"
*   **Nanobot:** "Please provide your Coinbase wallet ID or email address."
*   **User:** "myemail@example.com"
*   **Nanobot:** "Your Coinbase wallet balance is $1234.56."

*   **User:** "What's my Coinbase balance?"
*   **Nanobot:** "Please provide your Coinbase wallet ID or email address."
*   **User:** "invalid-wallet-id"
*   **Nanobot:** "Error: Could not find account associated with the provided identifier."
```