```skill
---
name: whatsapp-business-notify
description: Sends a WhatsApp Business notification to a specified contact.
metadata:
  nanobot:
    emoji: 📱
    category: communication
    tags: [whatsapp, business, notification, messaging]
---

## Skill: whatsapp-business-notify

This skill allows the nanobot to send a WhatsApp Business notification to a contact.  It assumes the nanobot has been previously configured with a WhatsApp Business API account and has access to the contact's phone number.

**Instructions:**

1.  **Identify the Contact:** Determine the phone number of the recipient. This should be in international format (e.g., +15551234567).
2.  **Compose the Message:**  Formulate the notification message. Keep it concise and relevant.
3.  **Execute the API Call:**  Use the configured WhatsApp Business API to send the message to the identified phone number.  The API call should include the recipient's phone number and the message content.
4.  **Handle Errors:** If the API call fails (e.g., due to invalid phone number, API error, or network issues), log the error and report it to the user.  Do *not* retry automatically.
5.  **Confirmation:** Upon successful message delivery, log the event.

**Input Parameters:**

*   `phone_number` (string, required): The recipient's phone number in international format (e.g., +15551234567).
*   `message` (string, required): The notification message to send.

**Output:**

*   `status` (string):  "success" if the message was sent successfully, "error" otherwise.
*   `error_message` (string, optional):  If `status` is "error", this field contains a description of the error.

**Example:**

To send a notification to +15551234567 with the message "Your order has shipped!", the nanobot would execute the skill with the following parameters:

```json
{
  "phone_number": "+15551234567",
  "message": "Your order has shipped!"
}
```

**Error Handling:**

*   **Invalid Phone Number:** If the `phone_number` is not a valid international phone number, return `status: error` and `error_message: "Invalid phone number format."`
*   **API Error:** If the WhatsApp Business API returns an error, return `status: error` and `error_message: "WhatsApp Business API error: [API error message]."`.
*   **Network Error:** If there is a network error preventing the API call, return `status: error` and `error_message: "Network error: Unable to connect to WhatsApp Business API."`
```