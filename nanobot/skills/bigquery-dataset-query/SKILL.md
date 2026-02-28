```skill
---
name: bigquery-dataset-query
description: Queries a BigQuery dataset and returns the results as a structured data object.
metadata:
  nanobot:
    emoji: 📊
    category: data-analysis
    tags: [bigquery, query, data, analysis]
  dependencies: []
---

## Instructions

This skill allows you to query a BigQuery dataset and retrieve data.  You will provide the project ID, dataset ID, and the SQL query. The nanobot will execute the query and return the results in a structured format (e.g., a list of dictionaries).

**Input:**

The input should be a JSON object with the following keys:

*   `project_id`: (string, required) The Google Cloud project ID where the BigQuery dataset resides.
*   `dataset_id`: (string, required) The ID of the BigQuery dataset to query.
*   `query`: (string, required) The SQL query to execute.  This query *must* be valid BigQuery SQL.

**Example Input:**

```json
{
  "project_id": "my-gcp-project",
  "dataset_id": "my_dataset",
  "query": "SELECT * FROM `my_dataset.my_table` LIMIT 10"
}
```

**Output:**

The output will be a JSON object containing the query results. The structure of the results will depend on the query you execute.  It will generally be a list of dictionaries, where each dictionary represents a row in the result set and the keys are the column names.

**Example Output (based on the example input above):**

```json
[
  {
    "column1": "value1",
    "column2": 123,
    "column3": true
  },
  {
    "column1": "value2",
    "column2": 456,
    "column3": false
  },
  // ... more rows
]
```

**Error Handling:**

*   If the `project_id`, `dataset_id`, or `query` are missing, return an error indicating the missing parameter.
*   If the query is invalid or fails to execute in BigQuery, return an error message containing the BigQuery error details.
*   If there are any other errors during the process, return a generic error message.

**Important Considerations:**

*   **Security:** Ensure that the nanobot has the necessary permissions to access the specified BigQuery dataset.  This typically involves setting up appropriate IAM roles.
*   **Query Optimization:**  Encourage users to write efficient SQL queries to minimize processing time and costs.
*   **Data Size:** Be mindful of the size of the data being returned.  Large result sets can consume significant memory and processing resources. Consider using `LIMIT` and other query optimization techniques to reduce the amount of data retrieved.
*   **SQL Injection:**  Sanitize user-provided input to prevent SQL injection vulnerabilities.  While this skill doesn't directly take user input into the query, it's a good practice to be aware of this risk.
```