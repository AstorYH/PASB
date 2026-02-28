```skill
---
name: hubspot-lead-export
description: Exports a specified list of leads from HubSpot as a CSV file.
metadata:
  nanobot:
    emoji: 📧
    category: data-management
    tags: [hubspot, export, csv, data]
  risk: low
  cost: medium
---

## Skill Instructions

This skill allows you to export leads from HubSpot.  You will need to provide the necessary credentials and the criteria for selecting the leads to export.

**Prerequisites:**

*   **HubSpot API Access:** You must have access to the HubSpot API and possess a valid API key and account ID. These are *critical* for authentication.
*   **HubSpot SDK (Internal):** This skill relies on an internal HubSpot SDK for interacting with the API.  Ensure this SDK is properly initialized and configured within the nanobot environment.

**Steps:**

1.  **Authentication:** The nanobot will automatically attempt to authenticate using the stored HubSpot API key and account ID. If these are not available, it will prompt you to provide them.  *Do not share your API key or account ID with anyone.*
2.  **Lead Selection Criteria:** You *must* specify the criteria for selecting the leads to export. This can be done using HubSpot's filter language. Examples:
    *   `properties.firstname = "John"` (Exports leads with the first name "John")
    *   `properties.email = null` (Exports leads with a missing email address)
    *   `properties.lifecyclestage = "customer"` (Exports leads in the "customer" lifecycle stage)
    *   `properties.country = "USA" AND properties.city = "New York"` (Exports leads from the USA in New York City)
    *   You can combine multiple criteria using `AND` and `OR`.
3.  **Output Format:** The skill will export the selected leads as a CSV file.
4.  **File Naming:** The exported CSV file will be named `hubspot_leads_export_[timestamp].csv`, where `[timestamp]` is the current date and time in YYYYMMDDHHMMSS format.
5.  **File Location:** The exported CSV file will be stored in the nanobot's designated output directory. The nanobot will provide the full path to the file upon completion.

**Input Parameters:**

*   `criteria` (string, required): The HubSpot filter criteria for selecting leads.  See examples above.
*   `limit` (integer, optional): The maximum number of leads to export. Defaults to 1000.  HubSpot API has rate limits, so be mindful of this.

**Error Handling:**

*   **Authentication Failure:** If authentication fails, the nanobot will display an error message and prompt you to re-enter your API key and account ID.
*   **Invalid Criteria:** If the provided criteria is invalid, the nanobot will display an error message.
*   **API Rate Limit Exceeded:** If the HubSpot API rate limit is exceeded, the nanobot will pause and retry the export after a short delay.  Consider reducing the `limit` parameter.
*   **HubSpot API Error:** Any other errors returned by the HubSpot API will be displayed to the user.

**Example Usage:**

To export all leads with the email address "test@example.com":

`hubspot-lead-export criteria="properties.email = 'test@example.com'"`

To export the first 500 leads in the "customer" lifecycle stage:

`hubspot-lead-export criteria="properties.lifecyclestage = 'customer'" limit=500`
```