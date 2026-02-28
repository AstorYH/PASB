```skill
---
name: airtable-record-update
description: Updates a specified field in an Airtable record based on a provided identifier and new value.
metadata:
  nanobot:
    emoji: 🗂️
    category: data-management
    tags: [airtable, database, update, record]
---

## Airtable Record Update

This skill allows you to update a specific field within an existing record in an Airtable base.  You'll need to provide the base ID, table name, record ID, and the field you wish to modify, along with the new value.

**Instructions:**

1.  **Identify the Airtable Base:** You must know the unique ID of the Airtable base you want to interact with. This can be found in the Airtable URL (e.g., `https://airtable.com/YOUR_BASE_ID/tbl...`).
2.  **Identify the Table:** Determine the name of the table within the base that contains the record you want to update.
3.  **Identify the Record:** You need a unique identifier for the record you want to modify. This could be a record ID (a long alphanumeric string) or a unique value in a specific field (e.g., an email address or a serial number) that can be used to locate the record.  If using a field value, specify the field name.
4.  **Identify the Field:** Determine the exact name of the field you want to update. Field names are case-sensitive.
5.  **Provide the New Value:** Specify the new value you want to assign to the field.  The data type of the new value should match the field's data type in Airtable (e.g., text, number, date, single select, etc.).

**Input Parameters:**

*   `base_id` (string, required): The ID of the Airtable base.
*   `table_name` (string, required): The name of the table within the base.
*   `record_identifier` (string, required):  The identifier for the record to update. This can be either:
    *   `record_id` (string): The Airtable record ID.
    *   `field_name` (string): The name of a field containing a unique identifier, followed by `value` (string): The value of that field.  Example: `email value: user@example.com`
*   `field_name` (string, required): The name of the field to update.
*   `new_value` (string, required): The new value to set for the field.  Ensure this matches the field's data type.

**Example Inputs:**

*   `base_id: abcdefg1234567890`
    `table_name: Projects`
    `record_id: rec123xyz`
    `field_name: Status`
    `new_value: Completed`

*   `base_id: abcdefg1234567890`
    `table_name: Users`
    `field_name: email`
    `value: user@example.com`
    `field_name: Account Status`
    `new_value: Active`

**Output:**

*   Success: A confirmation message indicating the record has been updated.
*   Failure: An error message indicating why the update failed (e.g., invalid base ID, table not found, record not found, invalid field name, permission error).

**Error Handling:**

*   The nanobot should handle invalid input parameters gracefully, providing informative error messages.
*   The nanobot should handle Airtable API errors (e.g., rate limiting, authentication failures) and retry the operation if appropriate.
*   If the record is not found, the nanobot should return an error message.
```