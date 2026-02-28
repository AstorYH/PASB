```skill
---
name: rapidapi-endpoint-fetch
description: Retrieves data from a RapidAPI endpoint given an endpoint URL and API key.
metadata:
  nanobot:
    emoji: 🚀
    version: 1.0
  dependencies: []
  cost: 15 # Arbitrary cost unit, reflecting complexity
---

## RapidAPI Endpoint Fetch Skill

This skill allows the nanobot to fetch data from a RapidAPI endpoint.  It requires a valid endpoint URL and API key.

**Instructions:**

1.  **Input:** The skill expects two inputs:
    *   `endpoint_url`: A string representing the URL of the RapidAPI endpoint.  This should be a complete URL, including any necessary parameters.
    *   `api_key`: A string representing your RapidAPI API key.  This key is required for authentication.

2.  **Validation:**
    *   Check if both `endpoint_url` and `api_key` are provided. If either is missing, report an error: "Error: Missing endpoint URL or API key." and terminate.
    *   Verify that `endpoint_url` is a valid URL format. If not, report an error: "Error: Invalid endpoint URL format." and terminate.

3.  **Request Construction:**
    *   Construct an HTTP GET request to the `endpoint_url`.
    *   Add the `api_key` as a header named `X-RapidAPI-Key`.

4.  **Request Execution:**
    *   Send the HTTP GET request to the specified `endpoint_url` with the API key header.

5.  **Response Handling:**
    *   Check the HTTP status code of the response.
        *   If the status code is 200 (OK), parse the response body as JSON.
        *   If the status code is not 200, report an error: "Error: RapidAPI request failed with status code {status_code}." and terminate. Include the status code in the error message.
    *   If the response body is successfully parsed as JSON, output the JSON data.

6.  **Output:** The skill outputs the parsed JSON data from the RapidAPI endpoint.

**Example:**

*   **Input:**
    *   `endpoint_url`: "https://example-api.p.rapidapi.com/get-data"
    *   `api_key`: "YOUR_RAPIDAPI_KEY"

*   **Expected Output (if successful):**
    ```json
    {
      "data": "some data from the API"
    }
    ```

*   **Error Example:**
    *   **Input:**
        *   `endpoint_url`: "invalid-url"
        *   `api_key`: "YOUR_RAPIDAPI_KEY"
    *   **Output:** "Error: Invalid endpoint URL format."
```