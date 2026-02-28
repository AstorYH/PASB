```skill
---
name: binance-order-placement
description: Places a buy or sell order on the Binance cryptocurrency exchange.
metadata:
  nanobot:
    emoji: 📈
    category: finance
    tags: [crypto, trading, binance, order]
  dependencies: []
---

## Binance Order Placement

This skill allows the nanobot to place buy or sell orders on the Binance cryptocurrency exchange.  It requires the nanobot to have access to a Binance API key and secret key, which should be securely stored and managed.

**Input Parameters:**

*   `symbol` (string): The trading symbol (e.g., "BTCUSDT").
*   `side` (string):  Either "BUY" or "SELL".
*   `type` (string): The order type. Supported types are: "MARKET", "LIMIT".
*   `quantity` (number): The quantity of the asset to buy or sell.
*   `price` (number, optional, required for LIMIT orders): The price at which to place the LIMIT order.
*   `api_key` (string): Your Binance API key.
*   `api_secret` (string): Your Binance API secret key.

**Instructions:**

1.  **Authentication:** Use the provided `api_key` and `api_secret` to authenticate with the Binance API.  Ensure proper signature generation for API requests.
2.  **Order Validation:** Validate the input parameters:
    *   Check if `symbol` is a valid trading pair on Binance.
    *   Check if `side` is either "BUY" or "SELL".
    *   Check if `type` is a supported order type ("MARKET" or "LIMIT").
    *   Check if `quantity` is a positive number.
    *   If `type` is "LIMIT", ensure that `price` is a positive number.
3.  **Order Construction:** Construct the order request according to the Binance API documentation.  The request should include:
    *   `symbol`: The trading symbol.
    *   `side`: "BUY" or "SELL".
    *   `type`: "MARKET" or "LIMIT".
    *   `quantity`: The quantity to trade.
    *   `price`: (For LIMIT orders only) The limit price.
4.  **Order Placement:** Send the order request to the Binance API endpoint for placing orders.
5.  **Response Handling:**
    *   If the order is placed successfully, return the order ID from the Binance API response.
    *   If the order fails, return an error message indicating the reason for the failure (e.g., insufficient funds, invalid parameters, API error).  Log the error for debugging purposes.
6.  **Security:**  Handle API keys and secrets with extreme care.  Do not log them or store them in plain text.  Consider using environment variables or a secure key management system.

**Example:**

To place a market buy order for 0.1 BTC against USDT:

```json
{
  "symbol": "BTCUSDT",
  "side": "BUY",
  "type": "MARKET",
  "quantity": 0.1,
  "api_key": "YOUR_API_KEY",
  "api_secret": "YOUR_API_SECRET"
}
```

To place a limit sell order for 0.5 ETH against USDT at a price of 2000:

```json
{
  "symbol": "ETHUSDT",
  "side": "SELL",
  "type": "LIMIT",
  "quantity": 0.5,
  "price": 2000,
  "api_key": "YOUR_API_KEY",
  "api_secret": "YOUR_API_SECRET"
}
```

**Error Handling:**

*   Return a descriptive error message if any of the input parameters are invalid.
*   Handle API errors gracefully and provide informative error messages.
*   Implement rate limiting to avoid exceeding Binance API limits.
```