```skill
---
name: intercom-ticket-update
description: Updates an Intercom ticket with a specified message.
metadata:
  nanobot:
    emoji: 💬
    category: communication
    tags: [intercom, ticket, update, messaging]
  dependencies: []
---

## Intercom Ticket Update

This skill allows you to update an existing Intercom ticket with a new message.  It requires the ticket ID to be provided.

**Instructions:**

1.  **Identify the Ticket:** You must first know the ID of the Intercom ticket you wish to update. This ID is a unique string of characters.
2.  **Provide the Update Message:**  Clearly state the message you want to add to the ticket. This message will be appended to the existing conversation.
3.  **Execute:**  The nanobot will attempt to update the specified Intercom ticket with the provided message.

**Example Input:**

```
Update Intercom ticket ID '1234567890' with the message 'Acknowledged the issue and escalating to engineering.'
```

**Expected Output (Success):**

```
Ticket '1234567890' updated successfully with the message 'Acknowledged the issue and escalating to engineering.'
```

**Expected Output (Failure):**

```
Error: Could not update ticket '1234567890'.  Reason: Ticket not found.
```

**Error Handling:**

*   **Ticket Not Found:** If the provided ticket ID does not exist, the nanobot will return an error indicating that the ticket was not found.
*   **Invalid Ticket ID:** If the provided ticket ID is not a valid format, the nanobot will return an error indicating an invalid ticket ID.
*   **Internal Error:**  In the event of an unexpected error during the update process, the nanobot will return a generic error message.

**Important Considerations:**

*   This skill assumes you have the necessary permissions to update Intercom tickets.
*   The message will be appended to the existing conversation history.
*   The nanobot does not currently support formatting or rich text within the update message.  It will be treated as plain text.
```