```skill
---
name: zendesk-internal-note
description: Creates an internal note within a Zendesk ticket.
metadata:
  nanobot:
    emoji: 📝
    category: communication
    tags: [zendesk, ticket, note, internal]
---

## Zendesk Internal Note Skill

This skill allows the nanobot to create an internal note within a Zendesk ticket.  It's designed for communicating with other agents without the customer seeing the message.

**Instructions:**

1.  **Identify the Ticket:** The nanobot needs to know which Zendesk ticket to update. This will be provided as input.  The input should be a valid Zendesk ticket ID (e.g., `ZENDESK-12345`).
2.  **Compose the Note:** The nanobot needs the text of the internal note to be added. This will also be provided as input.
3.  **Create the Note:** The nanobot will use the provided ticket ID and note text to create a new internal note within the specified Zendesk ticket.
4.  **Confirmation:** The nanobot will confirm the creation of the note, including the ticket ID and a truncated version of the note text (to avoid revealing sensitive information).

**Input:**

*   `ticket_id`: (string, required) The Zendesk ticket ID.
*   `note_text`: (string, required) The text of the internal note.

**Output:**

*   `status`: (string) "success" or "failure"
*   `message`: (string) A confirmation message or an error message.  Example: "Successfully added internal note to ticket ZENDESK-12345: 'Agent update...'".  If failure, the message will describe the error.

**Example:**

**Input:**

```json
{
  "ticket_id": "ZENDESK-98765",
  "note_text": "Agent update: Customer confirmed they received the replacement part.  Escalating to closure."
}
```

**Output:**

```json
{
  "status": "success",
  "message": "Successfully added internal note to ticket ZENDESK-98765: 'Agent update...'"
}
```

**Error Handling:**

*   If the `ticket_id` is invalid or not found, return `status: "failure"` and `message: "Invalid or not found ticket ID."`
*   If `note_text` is missing, return `status: "failure"` and `message: "Note text is required."`
*   If there's an error communicating with the Zendesk API, return `status: "failure"` and `message: "Error communicating with Zendesk API."`
```