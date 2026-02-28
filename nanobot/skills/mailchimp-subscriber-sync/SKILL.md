```skill
---
name: mailchimp-subscriber-sync
description: Synchronizes a local contact list with a Mailchimp audience.
metadata:
  nanobot:
    emoji: 📧
    category: communication
    tags: [email, mailchimp, synchronization, contact management]
---

## Mailchimp Subscriber Sync

This skill allows the nanobot to synchronize a local contact list (represented as a structured data object) with a Mailchimp audience.  The local contact list should contain email addresses and optionally other fields like first name, last name, and any custom fields you want to sync.

**Input:**

*   `contact_list`: A JSON object representing the contact list to synchronize.  The object should be an array of contact objects. Each contact object should have at least an `email` field.  Optional fields include `first_name`, `last_name`, and any custom fields you define. Example:

    ```json
    [
      {
        "email": "john.doe@example.com",
        "first_name": "John",
        "last_name": "Doe"
      },
      {
        "email": "jane.smith@example.com",
        "first_name": "Jane",
        "last_name": "Smith",
        "custom_field_1": "value1"
      }
    ]
    ```

*   `mailchimp_api_key`: Your Mailchimp API key.  This is required for authentication.
*   `mailchimp_audience_id`: The ID of the Mailchimp audience you want to synchronize with.
*   `email_field_name`: The name of the email field in Mailchimp (usually "EMAIL").
*   `merge_fields`: (Optional) A JSON object mapping local contact list fields to Mailchimp merge field tags.  For example, `{"first_name": "FNAME", "last_name": "LNAME"}`. If not provided, only the email address will be synchronized.

**Process:**

1.  **Authentication:** Use the provided `mailchimp_api_key` to authenticate with the Mailchimp API.
2.  **Iterate Contacts:** Iterate through each contact in the `contact_list`.
3.  **Find or Add Subscriber:** For each contact, attempt to find a subscriber in the Mailchimp audience with the matching email address (using the `email_field_name`).
    *   If the subscriber is found, update their merge fields with the data from the contact list, using the `merge_fields` mapping (if provided).
    *   If the subscriber is not found, add a new subscriber to the audience with the contact's email address and merge fields (using the `merge_fields` mapping if provided).
4.  **Error Handling:**  Log any errors encountered during the synchronization process (e.g., invalid API key, audience not found, rate limiting).

**Output:**

*   `status`: A string indicating the overall status of the synchronization ("success" or "failure").
*   `synced_count`: The number of contacts successfully synchronized.
*   `skipped_count`: The number of contacts that were skipped (e.g., because they already existed in Mailchimp with different email addresses).
*   `error_messages`: An array of strings containing any error messages encountered during the synchronization process.  Empty if no errors occurred.

**Example:**

```json
{
  "status": "success",
  "synced_count": 2,
  "skipped_count": 0,
  "error_messages": []
}
```

**Notes:**

*   This skill assumes you have a valid Mailchimp API key and audience ID.
*   Rate limiting may apply when using the Mailchimp API.  Implement appropriate retry logic if necessary.
*   Consider adding error handling for invalid contact list data.
*   The `merge_fields` mapping allows you to customize which fields from your local contact list are synchronized to Mailchimp.
```