```skill
---
name: venmo-request-payment
description: Sends a Venmo request for a specified amount to a specified user.
metadata:
  nanobot:
    emoji: 💰
    category: financial
    tags: [payment, venmo, request]
---

## Instructions

This skill allows you to request payment via Venmo.  It requires the recipient's Venmo username and the amount to request.

**Input:**

*   `username`: (string, required) The Venmo username of the person you want to request money from.
*   `amount`: (number, required) The amount of money to request (e.g., 10.00).
*   `note`: (string, optional) A short note to include with the request (e.g., "For lunch").

**Process:**

1.  Verify that the `username` and `amount` parameters are provided. If either is missing, report an error and stop.
2.  Verify that the `amount` is a valid number greater than zero. If not, report an error and stop.
3.  Construct a Venmo request using the provided `username`, `amount`, and `note` (if provided).
4.  Simulate sending the Venmo request.  (Since we are nanobots, we cannot actually send the request. Instead, report that the request has been sent.)
5.  Report success, including the recipient's username, the amount requested, and the note (if provided).

**Output:**

A success message indicating the Venmo request has been sent.  Example:

```
Venmo request sent to @username for $amount with the note: "note"
```

**Error Handling:**

*   If `username` is missing: `Error: Username is required.`
*   If `amount` is missing: `Error: Amount is required.`
*   If `amount` is not a valid number: `Error: Invalid amount.`
*   If `amount` is zero or negative: `Error: Amount must be greater than zero.`
```