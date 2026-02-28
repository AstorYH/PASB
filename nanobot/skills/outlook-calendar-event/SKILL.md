```skill
---
name: outlook-calendar-event
description: Creates a new event in the user's Outlook calendar.
metadata:
  nanobot:
    emoji: 🗓️
    category: productivity
    tags: [calendar, outlook, event, scheduling]
  dependencies: []
---

## Instructions

This skill allows you to create a new event in your Outlook calendar.  The nanobot will prompt you for the necessary information to create the event.  Please provide clear and concise answers.

**Workflow:**

1.  **Initiation:** The nanobot will initiate the process with a greeting and request for event details.
2.  **Subject:** The nanobot will ask: "What is the subject of the event?"  Provide a brief and descriptive subject.
3.  **Start Time:** The nanobot will ask: "What time should the event start? (e.g., 10:00 AM, tomorrow, 2024-12-25)"  Provide a clear date and time.  The nanobot will attempt to parse natural language.
4.  **End Time:** The nanobot will ask: "What time should the event end? (e.g., 11:00 AM, in one hour, 2024-12-26 11:00)" Provide a clear date and time. The nanobot will attempt to parse natural language.
5.  **Attendees (Optional):** The nanobot will ask: "Who should be invited? (Separate multiple email addresses with commas, or say 'none')"  Provide email addresses of attendees. If no attendees are needed, respond with "none".
6.  **Location (Optional):** The nanobot will ask: "Where will the event be held? (e.g., Conference Room A, Online Meeting, or say 'none')" Provide a location. If no location is needed, respond with "none".
7.  **Body (Optional):** The nanobot will ask: "Do you want to add a body/description to the event? (yes/no)" If you answer "yes", the nanobot will ask: "What is the body/description?" Provide a brief description of the event.
8.  **Confirmation:** The nanobot will summarize the event details and ask for confirmation: "Confirm event details: Subject: [Subject], Start Time: [Start Time], End Time: [End Time], Attendees: [Attendees], Location: [Location], Body: [Body].  Confirm? (yes/no)"
9.  **Completion:** If you confirm, the nanobot will create the event in your Outlook calendar and report success. If you decline, the nanobot will cancel the operation.

**Example Interaction:**

```
Nanobot: Let's create a new Outlook calendar event. What is the subject of the event?
User: Project Meeting
Nanobot: What time should the event start? (e.g., 10:00 AM, tomorrow, 2024-12-25)
User: Tomorrow at 2:00 PM
Nanobot: What time should the event end? (e.g., 11:00 AM, in one hour, 2024-12-26 11:00)
User: Tomorrow at 3:00 PM
Nanobot: Who should be invited? (Separate multiple email addresses with commas, or say 'none')
User: john.doe@example.com, jane.smith@example.com
Nanobot: Where will the event be held? (e.g., Conference Room A, Online Meeting, or say 'none')
User: Online Meeting
Nanobot: Do you want to add a body/description to the event? (yes/no)
User: yes
Nanobot: What is the body/description?
User: Discuss project progress and next steps.
Nanobot: Confirm event details: Subject: Project Meeting, Start Time: Tomorrow at 2:00 PM, End Time: Tomorrow at 3:00 PM, Attendees: john.doe@example.com, jane.smith@example.com, Location: Online Meeting, Body: Discuss project progress and next steps. Confirm? (yes/no)
User: yes
Nanobot: Event created successfully in Outlook calendar.
```
```