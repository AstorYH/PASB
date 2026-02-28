```skill
---
name: gmail-send
description: Sends an email via Gmail using pre-defined parameters.
metadata:
  nanobot:
    emoji: 📧
    category: communication
    tags: [email, gmail, send, message]
---

## Skill: gmail-send

This skill allows the nanobot to send an email using a Gmail account.  It requires pre-configured credentials (username and password) stored securely within the nanobot's memory.  **Do not attempt to access external services without explicit authorization and secure credential management.**

**Instructions:**

1.  **Check Credentials:** Verify that the `gmail_username` and `gmail_password` variables are set and contain valid credentials.  If not, report an error and halt execution.
2.  **Parse Parameters:** Extract the following parameters from the input:
    *   `recipient`: The email address of the recipient.
    *   `subject`: The subject of the email.
    *   `body`: The body of the email.
3.  **Compose Email:** Construct the email message with the provided recipient, subject, and body.
4.  **Send Email:** Using the configured Gmail credentials, attempt to send the email.
5.  **Report Status:** Report the status of the email sending operation.  Success should indicate the email was sent without errors. Failure should indicate the reason for the failure (e.g., invalid credentials, network error, recipient address invalid).

**Variables (Pre-configured within the Nanobot):**

*   `gmail_username`: The Gmail address to use for sending emails.
*   `gmail_password`: The password for the Gmail account.  **This must be stored securely and accessed only within this skill.**

**Input Parameters:**

*   `recipient` (string, required): The email address of the recipient.
*   `subject` (string, required): The subject of the email.
*   `body` (string, required): The body of the email.

**Output:**

*   `status` (string):  "success" if the email was sent successfully, otherwise an error message.
*   `message_id` (string, optional): The unique identifier of the sent email (if available).

**Example Input:**

```json
{
  "recipient": "user@example.com",
  "subject": "Important Update",
  "body": "This is an important update regarding your account."
}
```

**Example Output (Success):**

```json
{
  "status": "success",
  "message_id": "1234567890abcdef1234567890abcdef"
}
```

**Example Output (Failure - Invalid Credentials):**

```json
{
  "status": "error: Invalid Gmail credentials. Please check the configured username and password."
}
```

**Error Handling:**

*   Handle invalid input parameters (e.g., missing recipient, subject, or body).
*   Handle network errors during email sending.
*   Handle authentication errors (e.g., invalid username or password).
*   Handle errors related to the recipient's email address (e.g., invalid format).
```