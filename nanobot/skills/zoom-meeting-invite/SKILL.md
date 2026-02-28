```skill
---
name: zoom-meeting-invite
description: Generates and sends a Zoom meeting invitation to a specified list of recipients.
metadata:
  nanobot:
    emoji: 🗓️
    category: communication
    tags: [meeting, scheduling, invitation, zoom]
---

## Skill: Zoom Meeting Invite

This skill allows you to create and send a Zoom meeting invitation to a list of recipients.  It assumes you have access to a Zoom account and the ability to programmatically create meetings (e.g., via the Zoom API, though this skill doesn't directly interface with it - it generates the *content* of the invite).

**Instructions:**

1.  **Gather Information:** You will need the following information to execute this skill:
    *   `recipients`: A comma-separated list of email addresses to invite.  Example: `john.doe@example.com,jane.smith@example.org`
    *   `topic`: The topic of the meeting. Example: "Project Brainstorm"
    *   `start_time`: The date and time the meeting will start, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ). Example: `2024-10-27T14:00:00Z`
    *   `duration`: The duration of the meeting in minutes. Example: `60`
    *   `timezone`: The timezone of the meeting. Example: `America/Los_Angeles`
    *   `agenda`: (Optional) A brief agenda for the meeting. Example: "Discuss Q4 goals, review marketing plan, assign tasks."

2.  **Generate the Invitation Text:**  Construct a well-formatted email invitation using the gathered information.  The email should include:
    *   A clear subject line: "Zoom Meeting Invitation: [topic]"
    *   A greeting (e.g., "Dear [recipients],")
    *   The meeting topic.
    *   The date and time of the meeting, clearly stated in a human-readable format (e.g., "October 27, 2024, at 2:00 PM Pacific Time").  Convert the ISO 8601 `start_time` and `timezone` to a readable format.
    *   The duration of the meeting.
    *   The Zoom meeting link (Placeholder - this skill *does not* generate the link.  Assume a placeholder like `[ZOOM_LINK]` will be inserted here).
    *   The meeting ID (Placeholder - this skill *does not* generate the ID. Assume a placeholder like `[MEETING_ID]` will be inserted here).
    *   The agenda (if provided).
    *   A closing (e.g., "Best regards,")
    *   Your name/signature.

3.  **Output the Invitation Text:** Output the complete generated email invitation text.  This text is intended to be sent via a separate email sending skill or tool.

**Example Input:**

```json
{
  "recipients": "john.doe@example.com,jane.smith@example.org",
  "topic": "Project Alpha Kickoff",
  "start_time": "2024-10-28T09:00:00Z",
  "duration": "30",
  "timezone": "Europe/London",
  "agenda": "Discuss project scope, assign initial tasks, set up communication channels."
}
```

**Example Output:**

```
Subject: Zoom Meeting Invitation: Project Alpha Kickoff

Dear john.doe@example.com, jane.smith@example.org,

You are invited to a Zoom meeting:

Topic: Project Alpha Kickoff
Date: October 28, 2024
Time: 9:00 AM London Time
Duration: 30 minutes

Agenda: Discuss project scope, assign initial tasks, set up communication channels.

Join Zoom Meeting: [ZOOM_LINK]
Meeting ID: [MEETING_ID]

Best regards,

[Your Name]
```