```skill
---
name: medium-post-scraper
description: Extracts text and metadata from a Medium post URL.
metadata:
  nanobot:
    emoji: 📰
    category: information-gathering
    tags: [web, scraping, text, metadata]
---

## Medium Post Scraper

This skill scrapes a Medium post and extracts its title, author, publication, and content.

**Instructions:**

1.  **Input:** A valid URL pointing to a Medium post (e.g., `https://medium.com/@author/post-title-12345`).
2.  **Process:**
    *   Access the provided URL.
    *   Parse the HTML content of the page.
    *   Locate the following elements using appropriate HTML parsing techniques (e.g., CSS selectors, XPath):
        *   **Title:** The title of the post.
        *   **Author:** The name of the author.
        *   **Publication:** The name of the publication (if applicable).
        *   **Content:** The main text content of the post.  Remove any HTML tags and extraneous whitespace.
    *   Handle potential errors gracefully, such as invalid URLs or changes in Medium's HTML structure.  If an error occurs, return an error message indicating the problem.
3.  **Output:** A JSON object containing the extracted data:

    ```json
    {
      "title": "Post Title",
      "author": "Author Name",
      "publication": "Publication Name",
      "content": "The full text content of the post."
    }
    ```

    If the publication is not available, the `publication` field should be `null`. If an error occurs, the output should be a JSON object with an "error" field:

    ```json
    {
      "error": "Could not scrape post from URL."
    }
    ```

**Example:**

**Input:** `https://medium.com/@elonmusk/tesla-ai-day-update-a79999999999`

**Possible Output:**

```json
{
  "title": "Tesla AI Day Update",
  "author": "Elon Musk",
  "publication": "Medium",
  "content": "Tesla AI Day Update\n\nIt’s time for another Tesla AI Day! This year’s event will be held on September 30th at the Tesla factory in Fremont, California. We’ll be showcasing the latest advancements in our AI and robotics programs, including...\n\n[Rest of the post content]"
}
```