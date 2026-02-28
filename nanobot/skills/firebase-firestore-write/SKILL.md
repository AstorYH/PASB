```skill
---
name: firestore-write
description: Writes data to a specified document in a Firebase Firestore database.
metadata:
  nanobot:
    emoji: 💾
  category: data-management
  tags: [database, firestore, write, data]
---

## Skill Instructions

This skill allows you to write data to a Firebase Firestore document.  You *must* provide the necessary credentials and database details.

**Input Parameters:**

*   `database_url`: (string, required) The URL of your Firebase Firestore database.  Example: `https://your-project-id.firebaseio.com`
*   `collection_name`: (string, required) The name of the Firestore collection where the document resides.
*   `document_id`: (string, required) The ID of the document to write to.  If the document doesn't exist, it will be created.
*   `data`: (object, required) A JSON object representing the data to write to the document.  This should be a valid JSON object.
*   `credentials_file`: (string, required) The path to your Firebase credentials file (JSON format). This file contains the necessary authentication information to access your Firebase project.

**Execution Steps:**

1.  **Authentication:** Use the provided `credentials_file` to authenticate with Firebase.
2.  **Database Connection:** Connect to the Firestore database using the `database_url`.
3.  **Document Access:** Access the document specified by `collection_name` and `document_id`.
4.  **Data Writing:** Write the `data` object to the document.  This will overwrite any existing data in the document.
5.  **Confirmation:** Verify that the write operation was successful.

**Output:**

*   `success`: (boolean) `true` if the write operation was successful, `false` otherwise.
*   `message`: (string) A message indicating the result of the operation.  This may include error messages if the write failed.

**Error Handling:**

*   If the `database_url`, `collection_name`, `document_id`, `data`, or `credentials_file` are missing, return `success: false` and a descriptive error message.
*   If there is an authentication error, return `success: false` and an error message indicating the authentication failure.
*   If there is an error connecting to the database, return `success: false` and an error message indicating the connection failure.
*   If there is an error writing the data, return `success: false` and an error message indicating the write failure.

**Example:**

```json
{
  "database_url": "https://my-project.firebaseio.com",
  "collection_name": "users",
  "document_id": "user123",
  "data": {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
  },
  "credentials_file": "/path/to/my-credentials.json"
}
```
```