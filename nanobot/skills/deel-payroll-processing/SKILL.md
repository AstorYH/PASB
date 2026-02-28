```skill
---
name: deel-payroll-processing
description: Processes payroll data through the Deel API to ensure accurate and timely payments to contractors.
metadata:
  nanobot:
    emoji: 💰
    category: finance
    tags: [payroll, finance, api, contractor, payments]
---

## Deel Payroll Processing Instructions

This skill allows you to interact with the Deel API to manage and process payroll for contractors.  You will need to authenticate with the Deel API using your API key.  **Important:** Treat your API key with utmost security. Do not expose it in logs or store it insecurely.

**Prerequisites:**

*   **Deel API Key:** Obtain a Deel API key from your Deel account. This key is essential for authentication.
*   **Contractor IDs:** You'll need the Deel IDs of the contractors you want to process payroll for.
*   **Payment Details:**  Have the necessary payment details (amount, currency, payment method) ready for each contractor.

**Workflow:**

1.  **Authentication:**  The first step is to authenticate with the Deel API.  You will be provided with the API key.  Store this securely.
2.  **Data Gathering:** Collect the required data for each contractor:
    *   Contractor Deel ID
    *   Payment Amount
    *   Currency (e.g., USD, EUR)
    *   Payment Method (e.g., Wise, direct deposit)
    *   Payment Date
3.  **API Call:** Construct the appropriate API request to Deel to initiate payroll processing.  The specific endpoint and request body will depend on the desired action (e.g., creating a payment run, marking a payment as sent).  Refer to the Deel API documentation for the correct format.
4.  **Error Handling:**  Check the API response for errors.  If an error occurs, log the error message and attempt to retry the operation (with exponential backoff).  If the error persists, escalate the issue to a human operator.
5.  **Confirmation:** If the API call is successful, log the confirmation and update any relevant records.

**Example API Request (Illustrative - consult Deel API documentation for specifics):**

```json
{
  "contractor_id": "1234567890",
  "amount": 1000.00,
  "currency": "USD",
  "payment_method": "wise",
  "payment_date": "2024-10-27"
}
```

**Important Considerations:**

*   **Rate Limiting:** Be mindful of Deel API rate limits. Implement appropriate delays and error handling to avoid exceeding the limits.
*   **Security:**  Protect your Deel API key and any sensitive data.
*   **Data Validation:** Validate all input data before sending it to the Deel API.
*   **Logging:** Log all API requests and responses for auditing and debugging purposes.
*   **Deel API Documentation:**  Always refer to the official Deel API documentation for the most up-to-date information on endpoints, request formats, and error codes: [https://docs.deel.com/](https://docs.deel.com/)

**Failure States:**

*   Invalid API Key
*   Contractor ID Not Found
*   Insufficient Funds
*   API Rate Limit Exceeded
*   Network Error
*   Invalid Payment Details
```