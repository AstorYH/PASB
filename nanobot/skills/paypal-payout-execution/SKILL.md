```skill
---
name: paypal-payout-execute
description: Executes a PayPal payout to a specified recipient using provided details.
metadata:
  nanobot:
    emoji: 💸
    category: financial
    tags: [paypal, payout, payment, transaction]
  dependencies: []
---

## Skill: paypal-payout-execute

This skill allows the nanobot to execute a PayPal payout to a designated recipient.  It requires specific details about the payout, including the recipient's email address, the amount, and a currency.

**Instructions:**

1.  **Receive Payout Details:** The nanobot will receive the following information as input:
    *   `recipient_email`: (String) The email address of the PayPal recipient.  This *must* be a valid PayPal email address.
    *   `amount`: (Float) The amount to be paid out.
    *   `currency`: (String) The currency of the payout (e.g., "USD", "EUR").
    *   `note`: (String, Optional) A note to include with the payout.  This is for informational purposes only and will be visible to the recipient.
    *   `payer_email`: (String) The email address associated with the PayPal account making the payment. This is crucial for authorization.

2.  **Validate Input:**
    *   Verify that `recipient_email` is a valid email format.
    *   Verify that `amount` is a positive number.
    *   Verify that `currency` is a valid ISO 4217 currency code.
    *   Verify that `payer_email` is a valid email format.

3.  **Simulate PayPal Payout:**  Since this is a simulated environment, the nanobot will *not* actually make a real PayPal transaction. Instead, it will simulate the process and report the outcome.

4.  **Report Outcome:**  The nanobot will report the outcome of the simulated payout.  Possible outcomes include:
    *   `success`: The payout was successfully simulated.  Report the following details:
        *   `status`: "success"
        *   `recipient_email`: (String) The recipient's email address.
        *   `amount`: (Float) The payout amount.
        *   `currency`: (String) The currency.
        *   `note`: (String, Optional) The note included with the payout.
        *   `transaction_id`: (String) A simulated transaction ID (e.g., "sim-txn-12345").
    *   `failure`: The payout failed.  Report the following details:
        *   `status`: "failure"
        *   `reason`: (String) A description of the failure reason (e.g., "Invalid recipient email", "Insufficient funds", "Invalid currency").

**Example Input:**

```json
{
  "recipient_email": "recipient@example.com",
  "amount": 10.00,
  "currency": "USD",
  "note": "Thank you for your contribution!",
  "payer_email": "payer@example.com"
}
```

**Example Success Output:**

```json
{
  "status": "success",
  "recipient_email": "recipient@example.com",
  "amount": 10.00,
  "currency": "USD",
  "note": "Thank you for your contribution!",
  "transaction_id": "sim-txn-98765"
}
```

**Example Failure Output (Invalid Email):**

```json
{
  "status": "failure",
  "reason": "Invalid recipient email format."
}
```
```