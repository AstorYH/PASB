```skill
---
name: slack-thread-reply
description: Sends a reply to a specific message within a Slack thread.
metadata:
  nanobot:
    emoji: 💬
  category: communication
  tags: [slack, thread, reply, message]
---

## Skill: Slack Thread Reply

This skill allows the nanobot to reply to a specific message within a Slack thread.  It requires the thread's channel ID, the message ID to reply to, and the text of the reply.

**Instructions:**

1.  **Identify the Thread:** The nanobot needs to know which Slack channel the thread exists in. This is provided as the `channel_id`.
2.  **Locate the Message:** The nanobot needs the unique ID of the message within the thread that you want to reply to. This is provided as the `message_id`.
3.  **Compose the Reply:** The nanobot needs the text of the reply you want to send. This is provided as the `reply_text`.
4.  **Send the Reply:** The nanobot will use the Slack API to send a reply to the specified message within the thread.

**Parameters:**

*   `channel_id` (string): The ID of the Slack channel where the thread is located.
*   `message_id` (string): The ID of the message within the thread to reply to.
*   `reply_text` (string): The text of the reply to send.

**Example:**

To reply to message ID `1234567890` in channel `C1234567890` with the text "Sounds good!", the nanobot would be given the following parameters:

*   `channel_id`: `C1234567890`
*   `message_id`: `1234567890`
*   `reply_text`: `Sounds good!`

**Error Handling:**

*   If the `channel_id` is invalid, the nanobot should report an error.
*   If the `message_id` is invalid, the nanobot should report an error.
*   If the `reply_text` is empty, the nanobot should prompt for a valid reply.
*   If the Slack API call fails, the nanobot should report the error.
```