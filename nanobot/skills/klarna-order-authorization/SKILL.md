```skill
---
name: klarna-order-authorization
description: Authorizes a Klarna order based on provided details and user confirmation.
metadata:
  nanobot:
    emoji: 💳
    category: financial
    tags: [klarna, authorization, payment, order]
---

## Klarna Order Authorization Skill

This skill allows the nanobot to authorize a Klarna order after verifying the details and obtaining user confirmation.

**Instructions:**

1.  **Receive Order Details:** The nanobot will receive order details, including:
    *   `order_id`: A unique identifier for the order.
    *   `amount`: The total amount of the order.
    *   `currency`: The currency of the order (e.g., USD, EUR).
    *   `description`: A brief description of the order.
    *   `klarna_session_token`: A token representing the Klarna session.  This is *critical* for authorization.
    *   `user_email`: The email address associated with the Klarna account.

2.  **Verify Order Details:**  Cross-reference the received details with available data (e.g., previous orders, user profile) to ensure consistency and identify any potential discrepancies.  Log any discrepancies.

3.  **User Confirmation Request:**  Generate a clear and concise message for the user, summarizing the order details and requesting confirmation.  Example: "Authorize Klarna order #12345 for $50.00 USD? (Description: Widget Purchase).  Confirm with 'yes' or 'no'."

4.  **Await User Response:**  Wait for the user's response.

5.  **Process User Response:**
    *   **If User Responds 'yes' or equivalent:** Proceed to authorization.
    *   **If User Responds 'no' or equivalent:**  Inform the user that the order has not been authorized and log the rejection.  Terminate the skill.
    *   **If User Provides Unclear Response:** Prompt the user to confirm with a clear 'yes' or 'no'.

6.  **Authorize Order (Simulated):**  Since this is a simulated environment, the nanobot will *simulate* the authorization process.  Instead of making an actual API call to Klarna, the nanobot will:
    *   Log a message indicating that the order is being authorized.  Include the `order_id`, `amount`, `currency`, and `klarna_session_token`.
    *   Generate a simulated authorization code (e.g., a random alphanumeric string).
    *   Store the simulated authorization code along with the order details.

7.  **Confirmation Message:**  Inform the user that the order has been authorized and provide the simulated authorization code. Example: "Order #12345 authorized. Authorization code: ABCDEFG123."

8.  **Skill Completion:**  Mark the skill as complete and log the successful authorization.

**Error Handling:**

*   **Missing Order Details:** If any required order details are missing, inform the user and request the missing information.
*   **Invalid Klarna Session Token:** If the `klarna_session_token` is invalid, inform the user that the session is expired and authorization cannot proceed.
*   **Unexpected Errors:** Log any unexpected errors and inform the user that an error occurred.
```