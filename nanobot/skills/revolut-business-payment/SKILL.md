```skill
---
name: revolut-business-payment
description: Initiates a payment to a specified recipient through a Revolut Business account.
metadata:
  nanobot:
    emoji: 💸
    category: financial
    tags: [payment, revolut, business, transfer]
---

## Revolut Business Payment Skill

This skill allows the nanobot to initiate a payment through a Revolut Business account.  It requires access to the Revolut Business API and appropriate authentication credentials.

**Prerequisites:**

*   **Revolut Business Account:** The nanobot must be associated with a valid Revolut Business account.
*   **API Credentials:**  The nanobot needs API keys or tokens to authenticate with the Revolut Business API. These should be securely stored and accessed.
*   **Recipient Details:** The recipient's details (name, email, Revolut account identifier) must be provided.

**Instructions:**

1.  **Authentication:** Authenticate with the Revolut Business API using the provided credentials.  This typically involves sending an authentication request to the API endpoint.
2.  **Recipient Validation:** Verify that the recipient's details are valid and that the account exists within the Revolut system.  This may involve querying the API for recipient information.
3.  **Payment Request Construction:** Construct a payment request object containing the following information:
    *   `amount`: The amount to be transferred (in the appropriate currency).
    *   `currency`: The currency of the payment (e.g., "EUR", "USD").
    *   `recipient`: The recipient's Revolut account identifier (e.g., email address or phone number).
    *   `note`: (Optional) A note or description for the payment.
4.  **Payment Initiation:** Send the payment request to the Revolut Business API endpoint for initiating payments.
5.  **Response Handling:**  Process the API response.
    *   **Success:** If the payment is successful, record the transaction details (transaction ID, timestamp, amount, recipient) and report success to the user.
    *   **Failure:** If the payment fails, extract the error message from the API response and report the error to the user.  Common errors include insufficient funds, invalid recipient details, or authentication failures.
6.  **Logging:** Log all actions taken, including authentication attempts, payment requests, and API responses, for auditing and debugging purposes.

**Input Parameters:**

*   `amount`: (Required) The amount to pay (e.g., "100.00").
*   `currency`: (Required) The currency to pay in (e.g., "EUR").
*   `recipient`: (Required) The recipient's Revolut account identifier (e.g., "recipient@example.com").
*   `note`: (Optional) A note for the payment (e.g., "Invoice for services").

**Output:**

*   **Success:** "Payment of [amount] [currency] to [recipient] initiated successfully. Transaction ID: [transaction_id]"
*   **Failure:** "Payment failed: [error_message]"

**Error Handling:**

*   Handle API authentication errors gracefully.
*   Validate input parameters to prevent invalid requests.
*   Implement retry logic for transient API errors.
*   Provide informative error messages to the user.

**Security Considerations:**

*   Securely store and manage API credentials.
*   Validate all input parameters to prevent injection attacks.
*   Implement rate limiting to prevent abuse.
*   Log all actions for auditing and security monitoring.
```