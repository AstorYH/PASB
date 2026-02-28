```skill
---
name: quickbooks-expense-log
description: Records an expense in QuickBooks, including vendor, date, category, and amount.
metadata:
  nanobot:
    emoji: 🧾
    category: finance
    tags: [quickbooks, expense, accounting, record]
  dependencies: []
---

## Instructions

This skill allows you to log an expense in QuickBooks.  You will need to provide the necessary details for the expense.

**Input:**  A description of the expense, including the vendor, date, category, and amount.  The description should be clear and concise.

**Process:**

1.  **Parse the Input:** Extract the vendor, date, category, and amount from the input description.  Assume the date is in YYYY-MM-DD format. If the date is not provided, default to the current date. If the category is not provided, prompt the user for a category.
2.  **Validate Data:** Ensure the amount is a valid number. If not, prompt the user to provide a valid amount.
3.  **QuickBooks API Interaction (Simulated):**  This skill *simulates* interacting with the QuickBooks API.  In a real implementation, you would use a QuickBooks API client library to create and submit an expense record.  For this simulation, simply log the expense details to the console.
4.  **Confirmation:**  Confirm the expense has been logged (simulated).

**Output:** A confirmation message indicating the expense has been logged, including the details.

**Example Input:**

"Log an expense for $50.00 to Staples on 2023-10-27 for office supplies."

**Example Output:**

"Expense logged: Vendor: Staples, Date: 2023-10-27, Category: Office Supplies, Amount: $50.00"

**Error Handling:**

*   If any required information is missing, prompt the user for the missing information.
*   If the amount is not a valid number, prompt the user to provide a valid amount.
*   If there's an issue with the simulated QuickBooks API interaction, report the error to the user.

**Prompting the User:**

*   If the category is missing: "What is the category for this expense?"
*   If the date is missing: "What is the date of this expense (YYYY-MM-DD)?"
*   If the amount is invalid: "Please provide a valid amount for the expense."
```