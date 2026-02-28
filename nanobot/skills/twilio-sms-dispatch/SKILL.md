```skill
---
name: sms-dispatch
description: Sends an SMS message via the Twilio API.
metadata:
  nanobot:
    emoji: 📱
    category: communication
    tags: [sms, messaging, twilio]
  twilio:
    account_sid: REQUIRED
    auth_token: REQUIRED
    from_number: REQUIRED
---

## Instructions

This skill allows you to send SMS messages using the Twilio API.  You **must** provide your Twilio Account SID, Auth Token, and a Twilio phone number (from_number) in the environment variables.

**Prerequisites:**

*   A Twilio account.
*   A Twilio phone number.
*   The `twilio` Python library installed (though this is handled automatically by the nanobot environment).

**Usage:**

To send an SMS, provide the `to_number` and `message_body` as arguments.

**Arguments:**

*   `to_number` (string): The recipient's phone number (in E.164 format, e.g., +15551234567).  **REQUIRED**
*   `message_body` (string): The text of the SMS message. **REQUIRED**

**Example:**

```
sms-dispatch to_number="+15558675309" message_body="Hello from the nanobot!"
```

**Error Handling:**

*   If any of the required environment variables (`account_sid`, `auth_token`, `from_number`) are missing, the skill will return an error.
*   If the `to_number` is invalid, the skill will return an error.
*   If the Twilio API returns an error (e.g., due to insufficient funds or a problem with the Twilio service), the skill will return an error.

**Return Value:**

On success, the skill will return a JSON object containing the Twilio `message_sid`.

```json
{
  "message_sid": "SMxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

On failure, the skill will return an error message.

**Code Implementation (for reference - you do not need to modify this):**

```python
import os
from twilio.rest import Client

def main(to_number, message_body):
    """Sends an SMS message using the Twilio API."""

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_FROM_NUMBER")

    if not account_sid or not auth_token or not from_number:
        return "Error: Twilio credentials (account_sid, auth_token, from_number) not set in environment variables."

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            to=to_number,
            from_=from_number,
            body=message_body
        )
        return {"message_sid": message.sid}
    except Exception as e:
        return f"Error sending SMS: {str(e)}"
```
```