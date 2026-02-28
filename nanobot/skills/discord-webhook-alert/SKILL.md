```skill
---
name: discord-webhook-alert
description: Sends a formatted alert message to a specified Discord webhook URL.
metadata:
  nanobot:
    emoji: 📢
    category: communication
    tags:
      - alert
      - discord
      - webhook
  dependencies: []
---

## Instructions

This skill allows you to send a formatted alert message to a Discord webhook.  You must provide the webhook URL and the message content.

**Input Parameters:**

*   `webhook_url` (string, required): The URL of the Discord webhook to send the message to.  This URL is publicly accessible and allows external services to post messages to a specific channel.
*   `message` (string, required): The message to send to the Discord channel.  This can be plain text or include basic markdown formatting (e.g., *italics*, **bold**, `code`).
*   `username` (string, optional): The username that will appear as the sender of the message in Discord. Defaults to "Nanobot Alert".
*   `avatar_url` (string, optional): The URL of an avatar image to use for the sender in Discord.

**Process:**

1.  Validate that `webhook_url` is a valid URL. If not, report an error and halt execution.
2.  Validate that `message` is a non-empty string. If not, report an error and halt execution.
3.  Construct a JSON payload containing the message details. The payload should include:
    *   `username`: The value of the `username` parameter, or "Nanobot Alert" if not provided.
    *   `avatar_url`: The value of the `avatar_url` parameter, if provided.
    *   `content`: The value of the `message` parameter.
4.  Send an HTTP POST request to the `webhook_url` with the JSON payload as the request body.  Set the `Content-Type` header to `application/json`.
5.  Check the HTTP response status code.
    *   If the status code is 200-299 (success), report success.
    *   If the status code is outside this range (error), report an error with the status code and a brief description.

**Output:**

*   Success: "Alert message sent to Discord webhook."
*   Error: "Error sending alert message to Discord webhook: [status code] - [error description]"

**Example:**

```
Input:
webhook_url: "https://discord.com/api/webhooks/..."
message: "Critical system failure detected!"
username: "System Monitor"
avatar_url: "https://example.com/system_monitor.png"

Output:
"Alert message sent to Discord webhook."
```

```
Input:
webhook_url: "invalid-url"
message: "Test message"

Output:
"Error sending alert message to Discord webhook: 400 - Bad Request"
```
```