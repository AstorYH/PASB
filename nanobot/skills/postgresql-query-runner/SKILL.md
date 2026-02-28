```skill
---
name: postgresql-query-runner
description: Executes a PostgreSQL query and returns the results.
metadata:
  nanobot:
    emoji: 💾
    category: data-access
    tags: [database, postgresql, query, sql]
---

## Instructions

This skill allows you to execute a PostgreSQL query and retrieve the results.  You will provide the query as input, and the skill will attempt to connect to a PostgreSQL database and run the query.

**Input:**

*   `query`: (string, required) The PostgreSQL query to execute.  Ensure the query is valid SQL.
*   `connection_string`: (string, optional) The PostgreSQL connection string. If not provided, the skill will attempt to use a default connection string configured in the environment.  The connection string should include the host, port, database name, username, and password. Example: `postgresql://user:password@host:port/database`.

**Output:**

*   `results`: (list of dictionaries) A list of dictionaries, where each dictionary represents a row in the result set.  The keys of each dictionary are the column names.
*   `error`: (string, optional) If an error occurred during query execution, this field will contain an error message.

**Process:**

1.  **Establish Connection:** Attempt to connect to the PostgreSQL database using the provided `connection_string` or the default connection string.
2.  **Execute Query:** Execute the provided `query` against the database.
3.  **Retrieve Results:** Fetch all rows from the result set.
4.  **Format Results:** Convert the result set into a list of dictionaries, where each dictionary represents a row and the keys are the column names.
5.  **Return Results:** Return the formatted `results` and any potential `error` message.

**Error Handling:**

*   If the connection to the database fails, return an `error` message indicating the connection failure.
*   If the query is invalid or fails to execute, return an `error` message indicating the query failure.
*   If any other error occurs during the process, return an `error` message describing the error.

**Example:**

**Input:**

```json
{
  "query": "SELECT * FROM users WHERE age > 25;"
}
```

**Output (Success):**

```json
{
  "results": [
    {
      "id": 1,
      "username": "john.doe",
      "age": 30,
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "username": "jane.smith",
      "age": 28,
      "email": "jane.smith@example.com"
    }
  ]
}
```

**Output (Error):**

```json
{
  "error": "Unable to connect to the database: Connection refused."
}
```
```