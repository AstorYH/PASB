```skill
---
name: gist-search
description: Searches GitHub Gists for code snippets matching a given query.
metadata:
  nanobot:
    emoji: 🔍
    category: information-retrieval
    tags: [search, code, github, gist]
---

## Skill Instructions

This skill allows you to search GitHub Gists for code snippets.

**Input:** A search query string. This should be a description of the code you are looking for (e.g., "python list comprehension", "javascript event listener", "c++ linked list").

**Process:**

1.  **Construct the API Request:** Formulate a request to the GitHub Gist API. The base URL is `https://api.github.com/gists/public`.  The query parameter should be `search`.  Append the provided search query to the `search` parameter.  For example, if the query is "python list comprehension", the URL will be `https://api.github.com/gists/public?search=python+list+comprehension`.
2.  **Execute the API Request:** Send a GET request to the constructed URL.
3.  **Parse the Response:** The API will return a JSON response. Parse this response.  The relevant data is in the `items` array. Each item in the `items` array represents a Gist.
4.  **Extract Relevant Information:** For each Gist in the `items` array, extract the following information:
    *   `id`: The Gist ID.
    *   `description`: The Gist description (if available).
    *   `files`: A dictionary where keys are filenames and values are file contents.  Extract the first file found and its content.
    *   `url`: The URL to the Gist on GitHub.
5.  **Format the Results:**  Present the results in a clear and concise format. For each Gist, include:
    *   The Gist description (if available).
    *   A snippet of the code (the first file's content).  Limit the snippet to a reasonable length (e.g., 200 characters) to avoid overwhelming the user.
    *   The Gist URL.

**Output:** A formatted list of GitHub Gist results, including description, code snippet, and URL for each Gist. If no Gists are found, output "No Gists found matching your query."

**Example:**

**Input:** `javascript array filter`

**Output:**

```
Gist 1:
Description: Simple array filter example
Code Snippet: function filterArray(arr, callback) { ... }
URL: https://gist.github.com/user/1234567

Gist 2:
Description: Another example of array filtering
Code Snippet: const filtered = arr.filter(item => item > 5);
URL: https://gist.github.com/anotheruser/8901234
```

**Error Handling:**

*   If the API request fails (e.g., network error, invalid URL), output "Error: Could not connect to the GitHub API."
*   If the API returns an error (e.g., rate limit exceeded), output "Error: GitHub API rate limit exceeded. Please try again later."
*   If the response is not valid JSON, output "Error: Invalid response from the GitHub API."
```