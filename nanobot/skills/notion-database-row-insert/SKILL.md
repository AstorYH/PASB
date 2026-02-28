```skill
---
name: notion-db-row-insert
description: Inserts a new row into a specified Notion database, populating fields with provided data.
metadata:
  nanobot:
    emoji: 📝
    category: data-management
    tags: [notion, database, insert, row, data]
---

## Skill: Notion Database Row Insert

This skill allows you to insert a new row into a Notion database. You will need to provide the database ID, and the data to populate the row's properties.

**Input Parameters:**

*   `database_id` (string, required): The ID of the Notion database to insert the row into.  This can be found in the URL of the database page (e.g., `https://www.notion.so/YOUR_DATABASE_ID`).
*   `properties` (object, required): A JSON object where keys are the property names in the Notion database and values are the data to be inserted into those properties.  The data type must match the property type in Notion (e.g., text, number, select, multi-select, date, checkbox, URL, email, phone, file).
    *   **Text:** String
    *   **Number:** Integer or Float
    *   **Select:** String (must match an existing option in the select property)
    *   **Multi-Select:** Array of Strings (each string must match an existing option)
    *   **Date:** ISO 8601 date string (e.g., "2023-10-27")
    *   **Checkbox:** Boolean (true/false)
    *   **URL:** String (valid URL)
    *   **Email:** String (valid email address)
    *   **Phone:** String (valid phone number)
    *   **File:**  This is not directly supported.  You would need to upload the file separately and then provide the file ID in the `properties` object.  The key would be the property name, and the value would be the file ID.
*   `title` (string, optional): If the database has a "Title" property, you can specify it here. If not provided, the "Title" property will be left blank.

**Output:**

*   Success: A JSON object containing the ID of the newly created row.
*   Failure: An error message explaining why the insertion failed.

**Example Input:**

```json
{
  "database_id": "YOUR_DATABASE_ID",
  "properties": {
    "Name": "John Doe",
    "Age": 30,
    "Status": "Active",
    "Due Date": "2023-11-15",
    "Priority": "High"
  },
  "title": "New User"
}
```

**Notes:**

*   Ensure the `properties` object contains only valid property names from the target Notion database.
*   The data types in the `properties` object must match the corresponding property types in the Notion database.
*   For Select and Multi-Select properties, the values must exactly match the existing options in the property.
*   Error handling is crucial.  The skill should gracefully handle invalid database IDs, incorrect data types, and missing properties.
*   This skill assumes you have the necessary permissions to access and modify the Notion database.
```