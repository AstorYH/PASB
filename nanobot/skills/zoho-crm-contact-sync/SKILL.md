```skill
---
name: zoho-crm-contact-sync
description: Synchronizes contact information between the current environment and a Zoho CRM account.
metadata:
  nanobot:
    emoji: 📧
    category: communication
    tags: [crm, zoho, contact, sync, data]
---

## Zoho CRM Contact Sync

This skill allows the nanobot to synchronize contact information with a Zoho CRM account.  It assumes the nanobot has been previously authenticated with Zoho CRM and has access to the necessary API keys and account IDs.

**Instructions:**

1.  **Identify Contact Data:** Analyze the current environment to identify contact information. This includes, but is not limited to:
    *   Name (First Name, Last Name)
    *   Email Address
    *   Phone Number
    *   Company Name
    *   Job Title
    *   Address (Street, City, State, Zip Code, Country)
    *   Any custom fields relevant to Zoho CRM.

2.  **Determine Zoho CRM Action:** Decide whether to create a new contact, update an existing contact, or do nothing.
    *   **Create New Contact:** If a contact with the identified email address does *not* exist in Zoho CRM, create a new contact record.
    *   **Update Existing Contact:** If a contact with the identified email address *does* exist in Zoho CRM, update the existing record with the new information.
    *   **Do Nothing:** If the contact already exists and the data is identical, or if there's a conflict that cannot be resolved, do not perform any action.

3.  **Zoho CRM API Interaction:** Use the Zoho CRM API to perform the appropriate action.
    *   **Authentication:** Use the previously stored API key and account ID to authenticate with the Zoho CRM API.
    *   **Data Mapping:** Map the identified contact data to the corresponding fields in the Zoho CRM contact record.  Pay close attention to data types (e.g., string, number, date).
    *   **API Call:** Make the appropriate API call to either create or update the contact record.  Handle potential errors (e.g., invalid API key, rate limiting, data validation errors).
    *   **Error Handling:** If an error occurs during the API call, log the error and attempt to retry the operation a limited number of times. If retries fail, report the error to the user.

4.  **Confirmation:** After successfully creating or updating the contact, confirm the action to the user.  Include the Zoho CRM contact ID in the confirmation message.

**Assumptions:**

*   The nanobot has been previously configured with Zoho CRM API credentials (API Key, Account ID).
*   The Zoho CRM API is accessible.
*   The nanobot has the necessary permissions to create and update contacts in Zoho CRM.
*   Data validation is handled by the Zoho CRM API.

**Example:**

If the nanobot identifies a contact with the following information:

*   First Name: John
*   Last Name: Doe
*   Email Address: john.doe@example.com
*   Company Name: Example Corp

And a contact with `john.doe@example.com` does not exist in Zoho CRM, the nanobot should create a new contact in Zoho CRM with those details.  The confirmation message would be: "Successfully created contact in Zoho CRM with ID: xxxxxxxx."
```