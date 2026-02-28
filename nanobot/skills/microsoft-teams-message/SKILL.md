```skill
---
name: teams-message
description: Sends a message to a specified Microsoft Teams channel.
metadata:
  nanobot:
    emoji: 💬
    category: communication
    tags: [teams, messaging, collaboration]
  dependencies: []
---

## Skill: teams-message

This skill allows the nanobot to send a message to a Microsoft Teams channel.

**Instructions:**

1.  **Channel Identification:** The nanobot needs to know the Teams channel to send the message to. This is provided as a parameter named `channel_id`.  The `channel_id` should be the unique identifier for the channel (e.g., a GUID).  The nanobot *must* validate that the `channel_id` is a valid format before proceeding.  If invalid, report an error.

2.  **Message Content:** The message to be sent is provided as a parameter named `message`. This should be a string containing the text of the message.

3.  **Authentication:**  The nanobot *must* have pre-configured credentials to access the Microsoft Teams API. These credentials are assumed to be stored securely and accessible to the nanobot.  This skill does *not* handle credential management.

4.  **API Call:** Use the Microsoft Teams API (specifically the `IM.PostMessage` endpoint) to send the message.  The `channel_id` is used as the target channel.

5.  **Error Handling:**
    *   If the API call fails (e.g., due to invalid credentials, network issues, or invalid `channel_id`), report an error to the user.  Include the error message from the API.
    *   If the `message` parameter is empty or null, report an error indicating that the message cannot be empty.

6.  **Success:** If the message is successfully sent, report a success message to the user.

**Parameters:**

*   `channel_id` (string, required): The ID of the Microsoft Teams channel to send the message to.
*   `message` (string, required): The text of the message to send.

**Example:**

```
teams-message channel_id="12345678-1234-1234-1234-1234567890ab" message="Hello from the nanobot!"
```

**Error Messages:**

*   `Error: Invalid channel_id format.`
*   `Error: Could not send message to Teams. API error: [API error message].`
*   `Error: Message cannot be empty.`
```