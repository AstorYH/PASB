```skill
---
name: salesforce-object-fetch
description: Retrieves data from a specified Salesforce object based on provided criteria.
metadata:
  nanobot:
    emoji: 💾
    category: data-access
    tags: [salesforce, data, retrieval, object]
  dependencies: []
---

## Salesforce Object Fetch

This skill allows the nanobot to query and retrieve data from a Salesforce object.  You will need to provide the object name and the criteria for the query.

**Instructions:**

1.  **Identify the Salesforce Object:** Determine the Salesforce object you wish to query (e.g., Account, Contact, Opportunity).  The object name is case-sensitive and must be accurate.
2.  **Define Query Criteria (SOQL):** Construct a SOQL (Salesforce Object Query Language) query to filter the data.  This query should specify the fields to retrieve and the conditions to apply.  Examples:
    *   `SELECT Id, Name FROM Account WHERE BillingCity = 'San Francisco'`
    *   `SELECT Id, Email FROM Contact WHERE AccountId = '001XXXXXXXXXXXXXXX'`
    *   `SELECT Id, Amount, CloseDate FROM Opportunity WHERE StageName = 'Closed Won'`
3.  **Execute the Query:**  The nanobot will execute the provided SOQL query against the Salesforce instance.
4.  **Return Results:** The nanobot will return the results of the query as a JSON array of objects. Each object represents a record that matches the query criteria.  If no records match, an empty array will be returned.

**Input:**

*   `object_name` (string): The name of the Salesforce object to query (e.g., "Account", "Contact").
*   `soql_query` (string): The SOQL query to execute.  This *must* be a valid SOQL query.

**Output:**

*   `results` (JSON array): A JSON array of objects representing the records retrieved from Salesforce.  Each object will contain the fields specified in the `soql_query`.  Returns an empty array if no records are found.

**Error Handling:**

*   If the `object_name` is invalid, the nanobot will return an error indicating that the object does not exist.
*   If the `soql_query` is invalid, the nanobot will return an error indicating the syntax error in the query.
*   If there are any other errors during the query execution, the nanobot will return a generic error message.

**Example:**

**Input:**

```json
{
  "object_name": "Account",
  "soql_query": "SELECT Id, Name, BillingCity FROM Account WHERE BillingCity = 'San Francisco'"
}
```

**Output:**

```json
{
  "results": [
    {
      "Id": "001XXXXXXXXXXXXXXX",
      "Name": "Acme Corp",
      "BillingCity": "San Francisco"
    },
    {
      "Id": "001YYYYYYYYYYYYYYY",
      "Name": "Beta Industries",
      "BillingCity": "San Francisco"
    }
  ]
}
```
```