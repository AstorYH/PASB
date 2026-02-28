```skill
---
name: workspace-member-invite
description: Invites a new member to the current workspace, providing their email address.
metadata:
  nanobot:
    emoji: 🤝
    category: communication
    tags: [workspace, member, invite, user]
---

## Workspace Member Invite

This skill allows you to invite a new member to the current workspace.  You will be prompted for the email address of the person you wish to invite.

**Instructions:**

1.  **Acknowledge Request:** Respond with "Okay, I'm ready to invite a member."
2.  **Prompt for Email:**  Ask the user: "Please provide the email address of the person you want to invite."
3.  **Receive Email Address:** Wait for the user to provide an email address.
4.  **Validate Email (Optional):**  (If possible, perform a basic email validation check.  This is not strictly required, but improves robustness.)
5.  **Initiate Invitation:**  Simulate sending an invitation to the provided email address.  Respond with: "Invitation sent to [email address]. They should receive an email shortly with instructions on how to join."
6.  **Confirmation:**  Confirm the action is complete: "The workspace member invite process is now complete."

**Example Interaction:**

**User:** Invite a new member to the workspace.
**Nanobot:** Okay, I'm ready to invite a member.
**User:** john.doe@example.com
**Nanobot:** Invitation sent to john.doe@example.com. They should receive an email shortly with instructions on how to join.
**Nanobot:** The workspace member invite process is now complete.
```