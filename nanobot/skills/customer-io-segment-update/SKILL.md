```skill
---
name: customerio-segment-update
description: Updates a Customer.io segment membership for a given user based on provided criteria.
metadata:
  nanobot:
    emoji: 👥
    category: communication
    tags: [customerio, segmentation, user, update]
---

## Customer.io Segment Update

This skill allows you to update a user's membership in a Customer.io segment.  It requires you to specify the Customer.io API key, the segment ID, and the user's email address.  The skill will then attempt to add or remove the user from the specified segment based on the provided `action`.

**Prerequisites:**

*   Access to a Customer.io account.
*   Customer.io API key.
*   Segment ID within Customer.io.

**Instructions:**

1.  **Provide the API Key:**  You *must* provide the Customer.io API key. This is essential for authentication.  Store this securely and do not expose it unnecessarily.
2.  **Specify the Segment ID:**  Provide the ID of the Customer.io segment you want to update. This is a unique identifier for the segment within your Customer.io account.
3.  **Identify the User:**  Provide the email address of the user whose segment membership you want to modify.
4.  **Define the Action:**  Specify the `action` to take.  Valid actions are:
    *   `add`: Adds the user to the segment.
    *   `remove`: Removes the user from the segment.

**Input Parameters:**

*   `api_key` (string, required): Your Customer.io API key.
*   `segment_id` (string, required): The ID of the Customer.io segment.
*   `email` (string, required): The email address of the user.
*   `action` (string, required):  The action to perform (`add` or `remove`).

**Example Usage:**

To add user `john.doe@example.com` to segment with ID `12345` using API key `abcdefg12345`, you would provide the following parameters:

```
{
  "api_key": "abcdefg12345",
  "segment_id": "12345",
  "email": "john.doe@example.com",
  "action": "add"
}
```

To remove user `jane.doe@example.com` from segment with ID `67890` using API key `uvwxyz45678`, you would provide:

```
{
  "api_key": "uvwxyz45678",
  "segment_id": "67890",
  "email": "jane.doe@example.com",
  "action": "remove"
}
```

**Error Handling:**

*   The skill will return an error if the API key is invalid or missing.
*   The skill will return an error if the segment ID is invalid or missing.
*   The skill will return an error if the email address is invalid or missing.
*   The skill will return an error if the action is not `add` or `remove`.
*   The skill will return an error if the Customer.io API returns an error (e.g., user not found).

**Output:**

The skill will return a success message if the update was successful.  If an error occurred, it will return an error message describing the problem.
```