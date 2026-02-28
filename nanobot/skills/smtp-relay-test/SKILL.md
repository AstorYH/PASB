```skill
---
name: smtp-relay-test
description: Verifies the functionality of an SMTP relay by sending a test email.
metadata:
  nanobot:
    emoji: 📧
    category: communication
    tags: [email, relay, test, network]
---

## Skill: SMTP Relay Test

This skill attempts to send a test email through a specified SMTP relay to confirm its operational status.

**Instructions:**

1.  **Gather Information:** The agent needs the following information:
    *   `relay_host`: The hostname or IP address of the SMTP relay server (e.g., "smtp.example.com").
    *   `relay_port`: The port number the relay server is listening on (e.g., 25, 587, 465).
    *   `username`: The username for authentication with the relay (if required).  If no authentication is required, set to an empty string.
    *   `password`: The password for authentication with the relay (if required). If no authentication is required, set to an empty string.
    *   `sender_email`: The email address the test email will be sent from (e.g., "test@example.com").
    *   `recipient_email`: The email address the test email will be sent to (e.g., "admin@example.com").
    *   `use_tls`: Boolean value indicating whether to use TLS encryption (true/false).

2.  **Establish Connection:** Attempt to establish a TCP connection to the `relay_host` on the specified `relay_port`.

3.  **Authentication (Conditional):** If `username` and `password` are provided (not empty strings), perform SMTP authentication using the provided credentials.  The specific authentication mechanism (e.g., LOGIN, PLAIN) should be determined based on the relay server's capabilities.

4.  **TLS Negotiation (Conditional):** If `use_tls` is true, initiate TLS negotiation after the connection is established but before authentication (if authentication is required).

5.  **Construct Email:** Construct a simple test email with the following characteristics:
    *   `From`: `sender_email`
    *   `To`: `recipient_email`
    *   `Subject`: "SMTP Relay Test"
    *   `Body`: "This is a test email sent via the SMTP relay."

6.  **Send Email:** Use the SMTP protocol to send the constructed email.

7.  **Verify Response:**  Analyze the SMTP server's response. A successful response typically includes a "250 OK" or similar indicating successful delivery.

8.  **Report Status:**
    *   **Success:** If the email is sent successfully and the server returns a positive response, report "Success: Email sent successfully."
    *   **Failure:** If any step fails (connection error, authentication error, email sending error, or negative server response), report the specific error encountered.  Include details like the error message and the step where the failure occurred.  For example: "Failure: Connection refused to relay_host." or "Failure: Authentication failed."

**Error Handling:**

*   Handle connection errors gracefully.
*   Handle authentication errors gracefully.
*   Log all errors encountered during the process.
*   If the relay server returns an error code, include the code in the error report.
```