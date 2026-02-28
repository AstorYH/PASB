```skill
---
name: plaid-transaction-fetch
description: Retrieves recent transaction history from a Plaid-linked financial account.
metadata:
  nanobot:
    emoji: 🏦
    category: finance
    tags: [finance, plaid, transactions, data]
  dependencies: []
---

## Skill Instructions

This skill allows you to fetch transaction data from a Plaid-linked financial account.  It assumes a pre-existing Plaid integration and access token.

**Input:**

*   `account_id`: (string, required) The ID of the Plaid account to fetch transactions from. This is the identifier provided by Plaid.
*   `date_range`: (string, optional, default: "30d") The date range to fetch transactions for, specified in Plaid's format (e.g., "30d", "90d", "1y", "2y", "all").
*   `limit`: (integer, optional, default: 25) The maximum number of transactions to retrieve.

**Process:**

1.  **Authenticate:** Use the existing Plaid integration to authenticate with the Plaid API.  This step is assumed to be handled by the underlying Plaid integration and is not part of this skill's direct responsibility.
2.  **Construct API Request:** Build a request to the Plaid Transactions endpoint.  The request should include:
    *   `account_id`: The provided `account_id`.
    *   `date_range`: The provided `date_range` (or the default "30d" if not provided).
    *   `limit`: The provided `limit` (or the default 25 if not provided).
3.  **Execute API Request:** Send the request to the Plaid API.
4.  **Parse Response:** Parse the JSON response from the Plaid API.  Extract the `transactions` array.
5.  **Format Output:**  Format the transaction data into a structured format (e.g., a list of dictionaries, where each dictionary represents a transaction).  Each transaction should include at least the following fields:
    *   `date`: The transaction date (in a human-readable format).
    *   `amount`: The transaction amount.
    *   `description`: A description of the transaction.
    *   `category`: The transaction category (if available).
    *   `transaction_id`: The unique transaction ID from Plaid.

**Output:**

*   A list of transaction dictionaries, formatted as described above.  If no transactions are found, return an empty list.  If an error occurs during the API call, return an error message indicating the failure and the reason (e.g., "Error fetching transactions: Invalid account ID").

**Error Handling:**

*   Handle potential errors from the Plaid API (e.g., invalid account ID, authentication errors, rate limiting).
*   Return informative error messages to the user.
*   Log any errors for debugging purposes.

**Example:**

**Input:**

```json
{
  "account_id": "1234567890",
  "date_range": "90d",
  "limit": 50
}
```

**Output:**

```json
[
  {
    "date": "2024-01-26",
    "amount": -25.00,
    "description": "Starbucks",
    "category": "Food & Drink",
    "transaction_id": "txn_abcdefg"
  },
  {
    "date": "2024-01-25",
    "amount": -100.00,
    "description": "Rent Payment",
    "category": "Housing",
    "transaction_id": "txn_hijklmn"
  },
  // ... more transactions
]
```
```