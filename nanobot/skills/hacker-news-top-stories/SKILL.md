```skill
---
name: hacker-news-top-stories
description: Retrieves the top stories from Hacker News and presents a concise summary.
metadata:
  nanobot:
    emoji: 📰
    category: information-gathering
    tags: [news, web, aggregation]
---

## Instructions

This skill allows you to retrieve and summarize the top stories from Hacker News.

**Process:**

1.  **Access Hacker News API:**  Utilize the Hacker News API (https://news.ycombinator.com/); specifically, the endpoint for top stories (`https://hacker-news.firebaseio.com/v0/topstories.json`).  Assume the API returns a JSON array of story IDs.
2.  **Fetch Story Details:** For the top 5 story IDs retrieved in the previous step, fetch the full details from the corresponding API endpoint (`https://hacker-news.firebaseio.com/v0/item/{story_id}.json`).
3.  **Extract Relevant Information:** For each story, extract the following:
    *   `title`: The title of the story.
    *   `url`: The URL of the story.
    *   `score`: The story's score.
    *   `num_comments`: The number of comments on the story.
4.  **Summarize and Present:**  Present the information in a clear, concise format.  For each story, output:
    *   The title.
    *   A brief summary (first 100 characters of the `text` field if available, otherwise use the title).
    *   The URL.
    *   The score.
    *   The number of comments.

**Output Format:**

```
Top Hacker News Stories:

1. Title: [Story Title]
   Summary: [Brief Summary]
   URL: [Story URL]
   Score: [Story Score]
   Comments: [Number of Comments]

2. Title: [Story Title]
   Summary: [Brief Summary]
   URL: [Story URL]
   Score: [Story Score]
   Comments: [Number of Comments]

... (repeat for top 5 stories)
```

**Error Handling:**

*   If the Hacker News API is unavailable, report an error: "Unable to retrieve Hacker News top stories."
*   If a story detail cannot be fetched, skip that story and continue with the next.
*   If the API returns an unexpected format, report an error: "Unexpected data format from Hacker News API."
```