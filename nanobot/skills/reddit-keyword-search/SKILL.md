```skill
---
name: reddit-keyword-search
description: Searches Reddit for posts containing specified keywords and returns a summary of the top results.
metadata:
  nanobot:
    emoji: 🔎
    category: information-gathering
    tags: [reddit, search, keywords, social media]
---

## Instructions

This skill allows you to search Reddit for posts containing specific keywords.  The agent will query the Reddit API (simulated) and return a summary of the top results.

**Input:**

*   `keywords` (string): A comma-separated list of keywords to search for.  For example: "AI, machine learning, neural networks".
*   `subreddit` (string, optional): The specific subreddit to search within. If not provided, the search will be across all public subreddits.  For example: "r/technology".
*   `sort` (string, optional):  The sorting method for the results.  Valid options are "hot", "new", "top", "relevance". Defaults to "relevance".
*   `limit` (integer, optional): The maximum number of results to return. Defaults to 5.

**Process:**

1.  **Validate Input:** Ensure `keywords` is provided. If `subreddit` is provided, ensure it starts with "r/". Validate `sort` against the allowed values. Ensure `limit` is a positive integer.
2.  **Simulate Reddit API Query:**  Simulate a query to the Reddit API using the provided `keywords`, `subreddit`, `sort`, and `limit`.  Assume the API returns a list of posts, each with a title, score, and URL.  For the simulation, generate plausible results.  Prioritize results that contain all keywords.
3.  **Summarize Results:**  Create a summary of the top results.  The summary should include:
    *   A brief introduction stating the search terms and subreddit (if specified).
    *   A numbered list of the top `limit` results.  Each result should include:
        *   The post title.
        *   The post score.
        *   The post URL.
4.  **Return Output:** Return the summary as a formatted string.

**Output:**

A string containing a summary of the Reddit search results.  Example:

```
Reddit Search Results:

Searching for: AI, machine learning, neural networks in all subreddits, sorted by relevance, limit 5.

1. Title: "New Breakthrough in Neural Network Training!" Score: 1250 URL: https://www.reddit.com/r/MachineLearning/comments/xyz123/new_breakthrough_in_neural_network_training/
2. Title: "AI-Powered Image Recognition System Achieves Record Accuracy" Score: 980 URL: https://www.reddit.com/r/artificialintelligence/comments/abc456/ai_powered_image_recognition_system_achieves/
3. Title: "The Future of Machine Learning: A Discussion" Score: 720 URL: https://www.reddit.com/r/technology/comments/def789/the_future_of_machine_learning_a_discussion/
4. Title: "Neural Networks and Deep Learning Explained" Score: 600 URL: https://www.reddit.com/r/learnmachinelearning/comments/ghi012/neural_networks_and_deep_learning_explained/
5. Title: "AI Ethics: Concerns and Considerations" Score: 450 URL: https://www.reddit.com/r/artificialintelligence/comments/jkl345/ai_ethics_concerns_and_considerations/
```

**Error Handling:**

*   If `keywords` is not provided, return an error message: "Error: Keywords are required."
*   If `subreddit` is provided but does not start with "r/", return an error message: "Error: Subreddit must start with 'r/'."
*   If `sort` is an invalid value, return an error message: "Error: Invalid sort value.  Valid options are 'hot', 'new', 'top', 'relevance'."
*   If `limit` is not a positive integer, return an error message: "Error: Limit must be a positive integer."
```