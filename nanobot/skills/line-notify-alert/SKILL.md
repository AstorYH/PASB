```skill
---
name: line-notify-alert
description: Sends a notification to a Line Notify account with a specified message.
metadata:
  nanobot:
    emoji: 📱
    category: communication
    tags:
      - notification
      - alert
      - messaging
  dependencies: []
---

## Line Notify Alert

This skill allows the nanobot to send a notification to a Line Notify account.  You will need to have a Line Notify access token configured in the nanobot's environment variables. The environment variable name is `LINE_NOTIFY_TOKEN`.

**Instructions:**

1.  **Check for Token:** First, verify that the `LINE_NOTIFY_TOKEN` environment variable is set. If it's not, respond with "Error: Line Notify token not configured." and halt execution.
2.  **Extract Message:** Extract the message to be sent from the user's input.  The message should be the entire input after the command.
3.  **Send Notification:** Use the Line Notify API to send a POST request to `https://notify-api.line.me/v1/notify` with the following parameters:
    *   `Authorization`: `Bearer ${LINE_NOTIFY_TOKEN}`
    *   `message`: The extracted message.
4.  **Confirmation:** If the notification is sent successfully, respond with "Line Notify alert sent!". If there's an error (e.g., invalid token, network error), respond with "Error sending Line Notify alert." and include the error message if available.

**Example Input:**

`line-notify-alert Hello, world!`

**Expected Output (Success):**

`Line Notify alert sent!`

**Expected Output (Failure - Token Missing):**

`Error: Line Notify token not configured.`

**Expected Output (Failure - API Error):**

`Error sending Line Notify alert. [Error details from API]`
```