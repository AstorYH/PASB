```skill
---
name: viber-service-message
description: Sends a service message (e.g., delivery status, account updates) to a Viber user.
metadata:
  nanobot:
    emoji: 📱
    category: communication
    tags: [viber, messaging, service, notification]
---

## Viber Service Message Skill

This skill allows the nanobot to send a service message to a Viber user. Service messages are used for things like delivery receipts, account updates, and other system-generated notifications.  They are distinct from user-initiated messages and have specific formatting requirements.

**Prerequisites:**

*   The nanobot must have access to a Viber API key and secret. These should be stored securely and accessible to the nanobot.
*   The nanobot must know the Viber user's ID.

**Instructions:**

1.  **Gather Information:** Collect the following information:
    *   `viber_user_id`: The Viber user ID to send the message to. This is a unique identifier for the user within Viber.
    *   `message_type`: The type of service message to send. Valid types include:
        *   `delivery_receipt`: Acknowledges that a message has been delivered.
        *   `read`: Indicates that a message has been read.
        *   `account_updated`: Notifies the user of an account update.
        *   `group_joined`: Notifies the user that they have joined a group.
        *   `group_left`: Notifies the user that they have left a group.
        *   `contact_added`: Notifies the user that a contact has been added.
        *   `contact_removed`: Notifies the user that a contact has been removed.
    *   `message_text` (Optional):  A short text message to accompany the service message.  This is not always required, and the Viber API may have length restrictions.
    *   `timestamp` (Optional): A timestamp indicating when the event occurred.  This can be useful for tracking and debugging.

2.  **Construct the Viber API Request:**  Format the data into a JSON payload suitable for the Viber API. The exact format will depend on the `message_type`, but generally includes the user ID and the message type.  If `message_text` is provided, include it in the payload.

3.  **Send the Request:** Use the Viber API endpoint for sending service messages. Include the API key and secret in the request headers for authentication.

4.  **Handle the Response:** Check the API response for success or failure. If the request fails, log the error and retry the request (with exponential backoff) a limited number of times. If the request succeeds, log the success and proceed.

**Example:**

To send a delivery receipt to user with ID `1234567890`:

```json
{
  "receiver": "1234567890",
  "type": "delivery_receipt",
  "receipt_id": "unique_message_id"
}
```

**Error Handling:**

*   **Invalid Viber User ID:** If the `viber_user_id` is invalid, log an error and do not send the message.
*   **Invalid Message Type:** If the `message_type` is not a supported type, log an error and do not send the message.
*   **API Errors:** Handle API errors gracefully, logging the error and retrying the request.
*   **Authentication Errors:** If the API key or secret is invalid, log an error and alert the administrator.
```