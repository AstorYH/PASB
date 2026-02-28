```skill
---
name: stripe-invoice-creation
description: Creates a Stripe invoice for a given customer and amount.
metadata:
  nanobot:
    emoji: 🧾
    category: financial
    tags: [stripe, invoice, payment]
---

## Skill: Stripe Invoice Creation

This skill allows the nanobot to create a Stripe invoice for a specified customer and amount.  It assumes the nanobot has access to a Stripe API key and the necessary customer information.

**Instructions:**

1.  **Input Validation:**
    *   Verify that the `customer_id` is a valid Stripe Customer ID. If not, respond with an error: "Error: Invalid Customer ID provided."
    *   Verify that the `amount` is a positive number. If not, respond with an error: "Error: Amount must be a positive number."
    *   Verify that the `currency` is a valid ISO 4217 currency code (e.g., USD, EUR, GBP). If not, respond with an error: "Error: Invalid Currency Code provided."

2.  **Stripe API Call:**
    *   Use the Stripe API to create an invoice. The request should include:
        *   `customer`: The `customer_id` provided as input.
        *   `amount`: The `amount` provided as input (in cents).
        *   `currency`: The `currency` provided as input.
        *   `automatic_tax`: `true` (to automatically calculate taxes if configured in Stripe).

3.  **Response Handling:**
    *   **Success:** If the invoice is created successfully, respond with the following information:
        *   `invoice_id`: The ID of the newly created invoice.
        *   `invoice_url`: A URL to view the invoice in the Stripe dashboard.
        *   `status`: "created"
    *   **Failure:** If the invoice creation fails (e.g., due to invalid input or API errors), respond with an error message that includes the Stripe API error details.  For example: "Error: Stripe API Error - [Error Message from Stripe]."

**Input Parameters:**

*   `customer_id` (string): The Stripe Customer ID to create the invoice for.
*   `amount` (number): The amount to charge in the invoice (e.g., 100 for $1.00).
*   `currency` (string): The currency for the invoice (e.g., "usd").

**Example Input:**

```json
{
  "customer_id": "cus_XXXXXXXXXXXXXXX",
  "amount": 1000,
  "currency": "usd"
}
```

**Example Success Response:**

```json
{
  "invoice_id": "invo_XXXXXXXXXXXXXXX",
  "invoice_url": "https://dashboard.stripe.com/invoices/invo_XXXXXXXXXXXXXXX",
  "status": "created"
}
```

**Error Handling:**

*   Implement robust error handling to catch potential issues with the Stripe API and provide informative error messages to the user.
*   Log all errors for debugging purposes.
```