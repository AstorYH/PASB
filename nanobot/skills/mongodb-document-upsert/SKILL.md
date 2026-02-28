```skill
---
name: mongodb-document-upsert
description: Inserts a new document into a MongoDB collection or updates an existing one if it already exists.
metadata:
  nanobot:
    emoji: 💾
    category: data-management
    tags: [database, mongodb, upsert, document, insert, update]
---

## Instructions

This skill allows you to perform an upsert operation on a MongoDB collection. An upsert operation either inserts a new document or updates an existing one based on a query.

**Input:**

*   `collection`: (string, required) The name of the MongoDB collection to operate on.
*   `query`: (object, required) A MongoDB query object that specifies the criteria for finding an existing document.  This should be a valid JSON object representing a MongoDB query.
*   `update`: (object, required) A MongoDB update object that specifies the changes to apply to the document. This should be a valid JSON object representing a MongoDB update.  Use `$set`, `$inc`, `$push`, etc. as needed.
*   `upsert`: (boolean, optional, default: true)  If true, insert a new document if no document matches the query. If false, do not insert a new document.

**Output:**

*   `result`: (object) A JSON object containing the result of the upsert operation. This will typically include the `upsertedId` (if a new document was inserted) and the matched count.  The exact structure of the result depends on the MongoDB driver.

**Example:**

Let's say you want to update a user's score in a "users" collection. If the user doesn't exist, you want to create a new user with a score of 100.

```json
{
  "collection": "users",
  "query": { "username": "john.doe" },
  "update": { "$inc": { "score": 10 } },
  "upsert": true
}
```

This will either increment the score of the user "john.doe" by 10, or create a new user document with `username: "john.doe"` and `score: 100`.

**Error Handling:**

*   If the `collection` is invalid, report an error.
*   If the `query` or `update` are invalid JSON, report an error.
*   If the MongoDB connection fails, report an error.
*   If the upsert operation fails for any other reason, report an error.

**Important Considerations:**

*   Ensure the MongoDB connection is properly configured and accessible.
*   Be mindful of the potential impact of updates on existing data.
*   Use appropriate indexing on the `query` fields to optimize performance.
*   The `update` object should be carefully constructed to avoid unintended consequences.
```