```skill
---
name: http-get-request
description: Retrieves data from a specified URL using an HTTP GET request.
metadata:
  nanobot:
    emoji: 🌐
    category: network
    tags: [http, get, request, data]
---

## Instructions

This skill allows you to retrieve data from a URL using an HTTP GET request.  Follow these steps carefully to ensure successful execution.

**1. Input:**

You will receive a single input parameter: `url`. This is a string representing the URL you want to access.  Ensure the URL is properly formatted (e.g., `https://www.example.com/api/data`).

**2. Action:**

*   Initiate an HTTP GET request to the provided `url`.
*   Handle potential errors during the request.  Specifically, check for:
    *   **Connection Errors:** If a connection cannot be established, report an error indicating a network issue.
    *   **HTTP Status Codes:**  If the response status code is not in the 200-299 range (success), report an error indicating the request failed with the specific status code.
*   If the request is successful (status code 200-299), extract the response body as a string.

**3. Output:**

*   **Success:** If the request is successful, output the response body as a string.
*   **Failure:** If any error occurs (connection error or non-success status code), output an error message. The error message should clearly state the nature of the failure (e.g., "Connection refused", "HTTP Error 404: Not Found").

**4. Example:**

*   **Input:** `url = "https://www.example.com"`
*   **Expected Output (Success):**  (The HTML content of example.com)
*   **Input:** `url = "https://www.example.com/nonexistent_page"`
*   **Expected Output (Failure):** "HTTP Error 404: Not Found"
*   **Input:** `url = "http://invalid_domain.example"`
*   **Expected Output (Failure):** "Connection refused"

**5. Considerations:**

*   This skill does *not* handle authentication or authorization.  If the URL requires authentication, the request will likely fail.
*   The response body is treated as a string.  If you need to parse the response as JSON or XML, you will need a separate parsing skill.
*   Be mindful of the size of the response body.  Very large responses could consume significant resources.
*   This skill does not implement any rate limiting. Excessive requests to a single URL could lead to being blocked.
```