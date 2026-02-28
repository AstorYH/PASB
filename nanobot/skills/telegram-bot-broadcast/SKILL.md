```skill
---
name: telegram-broadcast
description: Sends a message to all users subscribed to a Telegram bot.
metadata:
  nanobot:
    emoji: 📢
    category: communication
    tags: [telegram, broadcast, messaging]
---

## Telegram Broadcast Skill

This skill allows the nanobot to send a broadcast message to all users who have subscribed to a Telegram bot.

**Prerequisites:**

*   The nanobot must have a configured Telegram bot token.
*   The nanobot must have a database or storage mechanism to track user IDs who have subscribed to the bot.  This could be a simple list, a database table, or any other suitable data structure.
*   The nanobot must have the necessary permissions to send messages to the subscribed users.

**Instructions:**

1.  **Retrieve Subscribed User IDs:** Query the storage mechanism to retrieve a list of all user IDs that have subscribed to the Telegram bot.  The format of these IDs will depend on the Telegram API (typically integers).
2.  **Validate Message Content:** Ensure the provided message content is valid for Telegram.  This includes checking for excessive length, prohibited characters, and potential formatting issues.
3.  **Iterate and Send Messages:** Iterate through the list of subscribed user IDs. For each user ID:
    *   Construct the Telegram message using the provided content.
    *   Use the Telegram Bot API to send the message to the user.  This will involve using the bot token and the user ID as the chat ID.
    *   Handle potential errors during message sending (e.g., user blocked the bot, invalid chat ID). Log these errors for debugging purposes.
4.  **Confirmation:** Upon successful completion of sending messages to all subscribed users (or after encountering an unrecoverable error), provide a confirmation message indicating the number of messages sent and any errors encountered.

**Input Parameters:**

*   `message`: (string) The message content to be broadcast.  This should be a plain text string.

**Output:**

*   `success`: (boolean) True if the broadcast was successful (or partially successful without critical errors), False otherwise.
*   `messages_sent`: (integer) The number of messages successfully sent.
*   `errors`: (array) An array of error messages encountered during the broadcast. Each element in the array should be a string describing the error and the user ID where it occurred.

**Error Handling:**

*   If the bot token is invalid or missing, return an error indicating that the Telegram bot is not configured.
*   If the storage mechanism for subscribed user IDs is unavailable, return an error indicating that the user list cannot be accessed.
*   If an error occurs while sending a message to a specific user, log the error and continue to the next user. Do not halt the entire broadcast.
*   If the message content is invalid for Telegram, return an error indicating that the message is not valid.

**Example:**

```
Input:
message: "Important announcement: The bot will be undergoing maintenance tomorrow."

Output:
success: true
messages_sent: 123
errors: []
```

```
Input:
message: "This is a test message."

Output:
success: false
messages_sent: 100
errors: ["User 123456789: Bot blocked"]
```
```