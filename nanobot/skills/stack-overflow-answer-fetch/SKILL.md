```skill
---
name: stack-overflow-answer-fetch
description: Retrieves the top-rated answer from a Stack Overflow question based on a provided query.
metadata:
  nanobot:
    emoji: 📚
  category: information-retrieval
  tags: [search, question-answering, stack-overflow, api]
---

## Instructions

This skill allows you to retrieve the top-rated answer from Stack Overflow for a given search query.  It leverages the Stack Overflow API to find relevant questions and then extracts the top answer.

**Input:**

*   `query`: (string, required) The search query to use on Stack Overflow.  This should be a concise description of the problem you're trying to solve.  Example: "python list comprehension performance".

**Process:**

1.  **Construct Stack Overflow API URL:** Build a URL to the Stack Overflow API's search endpoint. The base URL is `https://api.stackexchange.com/2.3/search/advanced`.  Include the following parameters:
    *   `q`: Set this to the value of the `query` input.
    *   `site`: Set this to `stackoverflow`.
    *   `order`: Set this to `desc`.
    *   `sort`: Set this to `votes`.
    *   `filter`: Set this to `1` (this filter includes the title, body, and owner).

2.  **Make API Request:** Send an HTTP GET request to the constructed URL.

3.  **Parse API Response:** Parse the JSON response from the API.

4.  **Extract Question ID:**  Iterate through the `items` array in the response.  Select the first item (the top result). Extract the `items[0].question_id`.

5.  **Fetch Question Details:** Construct a URL to retrieve the details of the question using the extracted `question_id`. The URL is `https://api.stackexchange.com/2.3/questions/{question_id}`.  Replace `{question_id}` with the actual ID.

6.  **Make Question Details Request:** Send an HTTP GET request to the question details URL.

7.  **Parse Question Details Response:** Parse the JSON response.

8.  **Extract Top Answer:**  From the `answers` array in the response, select the first element (the top-rated answer). Extract the `body` of the answer.

**Output:**

*   `answer`: (string) The text content of the top-rated answer from Stack Overflow.  If no answer is found, return an empty string.

**Error Handling:**

*   If the API request fails (e.g., network error, invalid API key), return an error message indicating the failure and the reason (if available).
*   If the API response is not in the expected format, return an error message indicating the parsing failure.
*   If no results are found on Stack Overflow, return an empty string.

**Example:**

*   **Input:** `query = "python list comprehension performance"`
*   **Output:** (The text of the top-rated answer on Stack Overflow regarding Python list comprehension performance.)
```