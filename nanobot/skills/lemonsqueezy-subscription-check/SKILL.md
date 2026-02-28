```skill
---
name: lemonsqueezy-subscription-check
description: Checks the status of a LemonSqueezy subscription given a customer ID.
metadata:
  nanobot:
    emoji: 🍋
    category: "information gathering"
    tags: ["lemon squeezy", "subscription", "status", "api"]
---

## LemonSqueezy Subscription Check

This skill allows you to determine the subscription status of a LemonSqueezy customer.

**Instructions:**

1.  **Input:** You will receive a customer ID as a string. This is the unique identifier for the customer within LemonSqueezy.
2.  **Process:**
    *   Construct a request to the LemonSqueezy API to retrieve the subscription details for the given customer ID. The API endpoint is `https://api.lemonsqueezy.com/v1/customers/{customer_id}/subscriptions`. Replace `{customer_id}` with the provided customer ID.
    *   The request requires an API key.  Assume you have access to a LemonSqueezy API key stored securely. Use this key in the `Authorization` header as `Bearer YOUR_LEMONSQUEEZY_API_KEY`.  (Replace `YOUR_LEMONSQUEEZY_API_KEY` with the actual key).
    *   Send the API request.
    *   Parse the JSON response.
3.  **Output:**
    *   If the request is successful (status code 200), extract the `status` field from the JSON response.  Possible values are:
        *   `active`: The subscription is currently active.
        *   `trial`: The subscription is in a trial period.
        *   `canceled`: The subscription has been canceled.
        *   `past_due`: The subscription is past due.
        *   `unpaid`: The subscription is unpaid.
    *   Return the subscription status as a string.
    *   If the request fails (status code other than 200), return an error message indicating the failure and the status code.  For example: "Error: API request failed with status code 404".

**Example:**

*   **Input:** `cus_123456`
*   **API Request:** `GET https://api.lemonsqueezy.com/v1/customers/cus_123456/subscriptions` with `Authorization: Bearer YOUR_LEMONSQUEEZY_API_KEY`
*   **Successful Response (Example):**
    ```json
    {
      "id": "sub_789012",
      "customer_id": "cus_123456",
      "plan_id": "plan_345678",
      "status": "active",
      "current_period_start": "2023-10-26T00:00:00Z",
      "current_period_end": "2024-10-26T00:00:00Z"
    }
    ```
*   **Output:** `active`

*   **Error Response (Example):**
    ```json
    {
      "error": "Customer not found"
    }
    ```
*   **Output:** `Error: API request failed with status code 404`