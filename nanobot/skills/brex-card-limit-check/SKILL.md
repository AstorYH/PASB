```skill
---
name: brex-card-limit-check
description: Checks the current spending limit on a Brex corporate card.
metadata:
  nanobot:
    emoji: 💳
    category: finance
    tags: [brex, card, limit, spending]
---

## Brex Card Limit Check

This skill allows you to query the current spending limit for a specified Brex corporate card.

**Instructions:**

1.  **Identify the Card:**  You must first identify the Brex card you wish to check. This is typically done by referencing the last four digits of the card number or the cardholder's name.  The more specific the identifier, the better.
2.  **Access Brex API (Simulated):**  Assume access to a simulated Brex API endpoint. This endpoint requires authentication (which is handled internally and not exposed to the user).
3.  **Query the API:** Construct a request to the Brex API, specifying the card identifier. The request should be formatted as a JSON object.
    *   Example Request (Simulated): `{"card_identifier": "XXXX-1234"}`
4.  **Parse the Response:**  The Brex API will return a JSON response containing the card's details, including the current spending limit. Parse this response.
5.  **Extract the Limit:** Extract the `spending_limit` value from the parsed JSON response. This value will be a numerical representation of the limit (e.g., 10000.00 for $10,000.00).
6.  **Report the Limit:**  Clearly state the current spending limit to the user. Include the currency (USD).
    *   Example Response: "The current spending limit for card XXXX-1234 is $10,000.00."

**Error Handling:**

*   **Invalid Card Identifier:** If the provided card identifier is invalid or not found, respond with an error message: "Error: Invalid card identifier. Please provide a valid card number or name."
*   **API Error:** If the Brex API returns an error, respond with a generic error message: "Error: Unable to retrieve card limit. Please try again later."
*   **Missing Limit Data:** If the API response is received but the `spending_limit` field is missing, respond with: "Error: Spending limit data not found for this card."
```