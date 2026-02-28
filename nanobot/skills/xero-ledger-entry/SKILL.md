```skill
---
name: xero-ledger-entry
description: Creates a new ledger entry in Xero, recording a financial transaction.
metadata:
  nanobot:
    emoji: 💰
    category: financial
    tags: [ledger, xero, accounting, finance, transaction]
  dependencies: []
---

## Xero Ledger Entry Skill

This skill allows the nanobot to create a new ledger entry in Xero, recording a financial transaction.  It requires a clear understanding of the transaction details, including account codes, amounts, and descriptions.

**Instructions:**

1.  **Gather Information:**  The nanobot must first gather all necessary information for the ledger entry. This includes:
    *   **Organization ID:** The Xero organization to which the entry belongs.  This is a unique identifier for the Xero company.
    *   **Account Code:** The Xero account code to which the transaction should be posted (e.g., "101" for Bank Account, "200" for Sales).
    *   **Amount:** The monetary value of the transaction (positive for income, negative for expense).  Must be a valid numerical value.
    *   **Description:** A brief, descriptive explanation of the transaction.
    *   **Date:** The date of the transaction (YYYY-MM-DD format).
    *   **Type:** The type of transaction.  Valid values are "Invoice", "Payment", "Expense Claim", "Purchase Order", "Bill", "Credit Note", "Journal".
    *   **Contact ID (Optional):** If applicable, the Xero Contact ID associated with the transaction.
    *   **Reference (Optional):** A reference number or identifier for the transaction.

2.  **Validate Information:**  Before creating the ledger entry, the nanobot should validate the gathered information:
    *   Ensure the Organization ID is valid and accessible.
    *   Verify that the Account Code exists in the Xero organization.
    *   Confirm that the Amount is a valid numerical value.
    *   Check that the Date is in the correct format.
    *   Validate the Type against the allowed values.

3.  **Construct Xero API Request:**  Based on the gathered and validated information, construct the appropriate Xero API request to create the ledger entry. The specific request format will depend on the transaction type.  For example, for a "Journal" entry, the request would include details about the account, amount, and description.

4.  **Execute API Request:**  Send the constructed Xero API request to the Xero API endpoint for creating ledger entries.

5.  **Handle Response:**  Process the response from the Xero API.
    *   **Success:** If the API request is successful, confirm the creation of the ledger entry and report success to the user.
    *   **Failure:** If the API request fails, analyze the error message from the Xero API and report the error to the user, including potential reasons for the failure (e.g., invalid account code, insufficient permissions).

**Example Scenario:**

The user requests: "Create a Xero ledger entry for $100 to Account Code 101, Description 'Payment for Supplies', Date 2024-01-26, Type 'Journal', Organization ID 'abc-123'."

The nanobot would:

1.  Gather the information: Organization ID = "abc-123", Account Code = "101", Amount = 100, Description = "Payment for Supplies", Date = "2024-01-26", Type = "Journal".
2.  Validate the information.
3.  Construct a Xero API Journal entry request.
4.  Execute the request.
5.  Report success or failure based on the API response.
```