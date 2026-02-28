```skill
---
name: news-api-headline-scraper
description: Retrieves and summarizes top headlines from a specified news source via a News API.
metadata:
  nanobot:
    emoji: 📰
    version: 1.0
    category: information-gathering
    tags: [news, api, headlines, summarization]
---

## Instructions

This skill allows you to retrieve and summarize headlines from a news source using a News API.  You will need to provide the API key and the news source identifier.

**Input:**

*   `api_key`: (string) Your News API key.  This is required.
*   `source`: (string, optional) The News API source identifier (e.g., "bbc-news", "cnn"). If not provided, the skill will attempt to retrieve top headlines from a default source (e.g., "bbc-news").
*   `num_headlines`: (integer, optional) The number of headlines to retrieve. Defaults to 5.

**Process:**

1.  **Authentication:** Use the provided `api_key` to authenticate with the News API.
2.  **Request:** Construct a request to the News API to retrieve top headlines from the specified `source`. If no source is provided, use a default source.  Limit the number of headlines to `num_headlines`.
3.  **Data Extraction:** Parse the JSON response from the News API. Extract the headlines and their corresponding descriptions (if available).
4.  **Summarization (Optional):** If descriptions are available, attempt to summarize each headline and description into a concise summary.
5.  **Output Formatting:** Format the retrieved headlines (and summaries, if available) into a readable list.

**Output:**

A list of headlines (and summaries, if available) retrieved from the News API.  The output should be formatted as follows:

```
Headline 1: [Headline Text]
Summary (if available): [Summary Text]

Headline 2: [Headline Text]
Summary (if available): [Summary Text]

...
```

**Error Handling:**

*   If the `api_key` is missing, return an error message indicating that the API key is required.
*   If the News API request fails (e.g., due to an invalid API key or network error), return an error message indicating the failure and the reason (if available).
*   If the News API response is invalid JSON, return an error message indicating the invalid response.
*   If the source is invalid, return an error message indicating the source is not found.

**Example:**

**Input:**

```json
{
  "api_key": "YOUR_NEWS_API_KEY",
  "source": "bbc-news",
  "num_headlines": 3
}
```

**Possible Output:**

```
Headline 1: UK inflation falls to 2.3% in surprise drop
Summary (if available): UK inflation unexpectedly fell to 2.3% in April, easing pressure on the Bank of England to raise interest rates.

Headline 2: Russia launches major offensive in Kharkiv region
Summary (if available): Russian forces have intensified their offensive in Ukraine's Kharkiv region, prompting evacuations and raising concerns about a wider conflict.

Headline 3: US warns China over Taiwan military drills
Summary (if available): The US has warned China against conducting military drills near Taiwan, calling for restraint and peaceful resolution of tensions.
```
```