```skill
---
name: rest-api-post-builder
description: Constructs a properly formatted POST request body for a given API endpoint and data.
metadata:
  nanobot:
    emoji: 🛠️
    version: 1.0
    category: communication
    tags: [api, rest, post, data, builder]
---

## Instructions

This skill constructs a POST request body in JSON format, ready to be sent to a REST API. You will be provided with an API endpoint and a data dictionary. Your task is to format the data into a valid JSON string suitable for a POST request.

**Input:**

*   `api_endpoint`: (string) The URL of the API endpoint.  This is *not* used in the JSON construction, only for context.
*   `data`: (dictionary) A dictionary containing the data to be included in the POST request body.  The keys of the dictionary will become the keys in the JSON object, and the values will be the corresponding values.

**Output:**

*   (string) A JSON string representing the POST request body.

**Process:**

1.  **Receive Input:** Obtain the `api_endpoint` and `data` from the user.
2.  **JSON Conversion:** Convert the `data` dictionary into a JSON string using the appropriate JSON encoding method. Ensure that the JSON is properly formatted and valid.
3.  **Return JSON:** Return the generated JSON string.

**Example:**

*   `api_endpoint`: "https://example.com/api/users"
*   `data`: {"name": "John Doe", "email": "john.doe@example.com"}

**Output:**

```json
{"name": "John Doe", "email": "john.doe@example.com"}
```

**Error Handling:**

*   If the `data` is not a valid dictionary, return an error message: "Error: Input data must be a dictionary."
*   If the JSON conversion fails, return an error message: "Error: Failed to convert data to JSON."
```