```skill
---
name: wise-transfer
description: Facilitates secure and optimized multi-currency transfers, leveraging real-time exchange rates and minimizing fees.
metadata:
  nanobot:
    emoji: 💰
    category: financial
    tags: [currency, transfer, optimization, fee, exchange]
---

## Instructions

This skill allows you to initiate a currency transfer, optimizing for cost and speed.  Follow these steps carefully.

**1. Gather Information:**

*   **Source Currency (sc):**  The currency you are transferring *from*.  Example: "USD"
*   **Destination Currency (dc):** The currency you are transferring *to*. Example: "EUR"
*   **Amount (amt):** The amount of the source currency you wish to transfer. Example: "1000"
*   **Recipient Account Details (rec_details):**  This is a structured data object containing the necessary information to send the funds.  The exact format will depend on the recipient's preferred method (bank transfer, digital wallet, etc.).  Example:
    ```json
    {
      "method": "bank_transfer",
      "account_number": "DE12345678901234567890",
      "bank_code": "DEUTIFXXXX",
      "recipient_name": "John Doe"
    }
    ```
    Or, for a digital wallet:
    ```json
    {
      "method": "paypal",
      "email": "john.doe@example.com"
    }
    ```
*   **Transfer Priority (priority):**  Indicate the desired transfer speed. Options: "low", "medium", "high".  Higher priority may incur higher fees. Default is "medium".

**2. Execute the Transfer:**

The nanobot will:

*   **Determine Optimal Exchange Rate:** Query real-time exchange rates for the `sc` to `dc` conversion.
*   **Calculate Fees:** Estimate transfer fees based on the `priority` and the transfer amount.
*   **Present Options:**  Present the user with a summary of the transfer, including:
    *   Amount in Source Currency (`amt`)
    *   Estimated Amount in Destination Currency (calculated using the exchange rate)
    *   Estimated Fees
    *   Total Cost (Amount in Destination Currency + Fees)
    *   Estimated Transfer Time (based on `priority`)
*   **Confirmation:**  Await user confirmation ("confirm" or "cancel").
*   **Initiate Transfer:** If confirmed, initiate the transfer using the provided `rec_details`.
*   **Report Status:** Report the transfer status (success, failure, pending) and any relevant transaction IDs.

**3. Error Handling:**

*   **Invalid Currency Codes:** If `sc` or `dc` are invalid currency codes, report an error.
*   **Insufficient Funds:** If there are insufficient funds in the source account, report an error.
*   **Invalid Recipient Details:** If `rec_details` are invalid or incomplete, report an error.
*   **Transfer Failure:** If the transfer fails for any reason, report the error and provide details if available.

**Example Interaction:**

```
User: wise-transfer sc=USD dc=EUR amt=1000 rec_details='{"method": "bank_transfer", "account_number": "DE12345678901234567890", "bank_code": "DEUTIFXXXX", "recipient_name": "John Doe"}' priority=high
```

```
Nanobot:
Transfer Summary:
  Source Currency: USD
  Destination Currency: EUR
  Amount (USD): 1000
  Estimated Amount (EUR): 920 (based on current exchange rate)
  Estimated Fees: 5 EUR
  Total Cost (EUR): 925
  Estimated Transfer Time: 1-2 business days (High Priority)

Confirm? (confirm/cancel)
```

```
User: confirm
```

```
Nanobot: Transfer initiated. Transaction ID: XXXXXXXXXXXXXXXX. Status: Pending.
```
```