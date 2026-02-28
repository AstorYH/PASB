```skill
---
name: square-pos-sync
description: Synchronizes local inventory and sales data with a Square Point-of-Sale system.
metadata:
  nanobot:
    emoji: 🛒
    category: commerce
    tags: [pos, inventory, sales, synchronization, square]
---

## Square POS Sync Skill

This skill allows the nanobot to interact with a Square Point-of-Sale (POS) system to synchronize inventory levels and sales data.  It assumes the nanobot has been previously authenticated with the Square API and possesses the necessary credentials (API key, access token, etc.).

**Prerequisites:**

*   **Authentication:** The nanobot must be authenticated with the Square API. This typically involves obtaining an access token and client ID.  Store these securely.
*   **Square API Access:** The nanobot needs appropriate permissions within the Square developer dashboard to access the necessary APIs (e.g., Inventory, Payments).
*   **Location ID:**  You'll need the Location ID of the Square store you want to interact with.

**Instructions:**

1.  **Identify Data to Sync:** Determine what data needs to be synchronized. This could include:
    *   **Inventory Updates:**  Changes to product quantities in the local system need to be reflected in Square.
    *   **Sales Data:**  New sales transactions from the local system need to be recorded in Square.
    *   **Product Information:**  Updates to product details (name, description, price) need to be synchronized.

2.  **Format Data for Square API:**  The Square API requires data to be formatted in a specific JSON structure.  The nanobot must convert the local data into the correct format for each API endpoint.  Refer to the Square API documentation for details: [https://developer.squareup.com/](https://developer.squareup.com/)

3.  **Inventory Synchronization:**
    *   For each product:
        *   Retrieve the current inventory quantity from the local system.
        *   Use the Square Inventory API to update the quantity for that product at the specified Location ID.  The API endpoint is typically `/inventory/items/{item_id}/inventory`.
        *   Handle potential errors (e.g., product not found, API rate limits).

4.  **Sales Data Synchronization:**
    *   For each new sale:
        *   Construct a payment object in the format required by the Square Payments API.  This will include details like the customer, items purchased, total amount, and payment method.
        *   Use the Square Payments API to create a new payment. The API endpoint is typically `/payments`.
        *   Handle potential errors (e.g., invalid payment details, API rate limits).

5.  **Product Information Synchronization (Optional):**
    *   If product details need to be synchronized:
        *   Compare the local product information with the corresponding product in Square.
        *   If there are differences, use the Square Items API to update the product details. The API endpoint is typically `/items/{item_id}`.
        *   Handle potential errors (e.g., product not found, API rate limits).

6.  **Error Handling:** Implement robust error handling to gracefully manage API errors, network issues, and data inconsistencies. Log errors for debugging purposes.

7.  **Rate Limiting:** Be mindful of Square API rate limits. Implement strategies to avoid exceeding these limits, such as batching requests or using exponential backoff.

**Example (Inventory Update - Simplified):**

```json
{
  "locationId": "YOUR_LOCATION_ID",
  "item": {
    "id": "ITEM_ID_FROM_LOCAL_SYSTEM",
    "quantity": NEW_QUANTITY_FROM_LOCAL_SYSTEM
  }
}
```

**Important Considerations:**

*   **Security:** Protect your Square API credentials. Do not hardcode them directly into the skill. Use environment variables or a secure configuration management system.
*   **Idempotency:** Design the skill to be idempotent, meaning that running it multiple times with the same input should have the same effect as running it once. This is important for handling potential errors and retries.
*   **Data Validation:** Validate the data before sending it to the Square API to prevent errors and ensure data integrity.
*   **Testing:** Thoroughly test the skill in a development environment before deploying it to production.
```