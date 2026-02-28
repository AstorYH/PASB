```skill
---
name: freshbooks-estimate-send
description: Sends a FreshBooks estimate to a client.
metadata:
  nanobot:
    emoji: 📧
    category: communication
    tags: [freshbooks, estimate, email]
---

## FreshBooks Estimate Send

This skill allows you to send a FreshBooks estimate to a client.

**Instructions:**

1.  **Identify the Estimate:** You must first identify the FreshBooks estimate you wish to send.  This requires knowing the estimate ID.  You will be prompted for this ID.
2.  **Identify the Recipient:** You must specify the email address of the client to whom the estimate should be sent. You will be prompted for this email address.
3.  **Optional: Add a Message:** You can optionally add a personalized message to accompany the estimate. If you don't provide a message, a default message will be used.
4.  **Send the Estimate:** Once you have provided the estimate ID and recipient email address (and optionally a message), the skill will send the estimate via FreshBooks.

**Prompts:**

*   `What is the FreshBooks estimate ID?`
*   `What is the recipient's email address?`
*   `Do you want to add a personalized message? (yes/no)`
    *   If `yes`: `What is your message?`

**Success Condition:**

The skill is successful if FreshBooks confirms that the estimate has been sent to the specified email address.

**Failure Conditions:**

*   Invalid estimate ID.
*   Invalid email address.
*   FreshBooks API error.
*   Network connectivity issues.

**Example Interaction:**

```
User: Send a FreshBooks estimate.
Nanobot: What is the FreshBooks estimate ID?
User: 12345
Nanobot: What is the recipient's email address?
User: client@example.com
Nanobot: Do you want to add a personalized message? (yes/no)
User: yes
Nanobot: What is your message?
User: Please review the attached estimate and let me know if you have any questions.
Nanobot: Sending FreshBooks estimate 12345 to client@example.com with the message: "Please review the attached estimate and let me know if you have any questions."
```
```