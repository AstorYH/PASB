```skill
---
name: twitter-trend-fetch
description: Retrieves the current trending topics on Twitter for a specified location.
metadata:
  nanobot:
    emoji: 📈
    category: information-gathering
    tags: [social-media, twitter, trends, data]
---

## Instructions

This skill allows you to fetch the current trending topics on Twitter.  You will need to specify a location (e.g., "Worldwide", "United States", "London").  The skill will then query the Twitter API (simulated) and return a list of trending topics.

**Input:**

*   `location`: (String) The location for which to retrieve trends.  Examples: "Worldwide", "United States", "London", "Tokyo".  Defaults to "Worldwide" if not provided.

**Output:**

*   A list of trending topics. Each topic will be a string representing the trend name.  If no trends are found, return an empty list.

**Process:**

1.  **Receive Input:**  Receive the `location` parameter. If `location` is not provided, default to "Worldwide".
2.  **Simulate API Query:**  Simulate a query to the Twitter API for trending topics in the specified `location`.  (Note: This is a simulation; actual API access is not required.)
3.  **Generate Trends (Simulation):**  Based on the `location`, generate a list of simulated trending topics.  Use the following guidelines for trend generation:
    *   **Worldwide:** ["#AI", "#ClimateChange", "#Music", "#News", "#Sports"]
    *   **United States:** ["#USPolitics", "#NFL", "#Tech", "#BreakingNews", "#Entertainment"]
    *   **London:** ["#London", "#Theatre", "#Food", "#Travel", "#RoyalFamily"]
    *   **Tokyo:** ["#Tokyo", "#Anime", "#Japan", "#Food", "#Culture"]
    *   **Other Locations:**  Generate a list of 5 random trending topics.  These can be generic (e.g., "#Trending", "#Viral", "#News", "#Entertainment", "#Music").
4.  **Return Results:** Return the list of trending topics.

**Example:**

*   **Input:** `location: "United States"`
*   **Output:** `["#USPolitics", "#NFL", "#Tech", "#BreakingNews", "#Entertainment"]`

*   **Input:** `location: "London"`
*   **Output:** `["#London", "#Theatre", "#Food", "#Travel", "#RoyalFamily"]`

*   **Input:** (No location provided)
*   **Output:** `["#AI", "#ClimateChange", "#Music", "#News", "#Sports"]`
```