```skill
---
name: instagram-business-insight
description: Analyzes Instagram Business data to identify trends and opportunities.
metadata:
  nanobot:
    emoji: 📊
    category: analysis
    tags: [social media, instagram, business, data, trends]
---

## Instagram Business Insight

This skill allows the nanobot to analyze Instagram Business data and provide insights.  It assumes access to the Instagram Business API or a similar data feed.

**Instructions:**

1.  **Data Acquisition:** First, retrieve the relevant data from the Instagram Business account. This includes, but is not limited to:
    *   Follower count and growth over time (daily/weekly/monthly).
    *   Post engagement metrics (likes, comments, shares, saves) for each post over the last [configurable period, default: 30 days].
    *   Reach and impressions for each post.
    *   Demographics of followers (age, gender, location).
    *   Website clicks from profile and posts.
    *   Hashtag performance (reach, impressions, engagement).
    *   Story metrics (views, replies, exits).
2.  **Data Processing:** Clean and organize the acquired data. Handle missing values appropriately (e.g., imputation with mean/median, or exclusion).
3.  **Trend Identification:** Analyze the data to identify key trends.  Specifically:
    *   **Follower Growth:** Determine the rate of follower growth and identify any significant spikes or dips.  Correlate these with specific events (e.g., posts, promotions).
    *   **Engagement Analysis:** Identify posts with the highest and lowest engagement rates. Analyze the content of these posts to understand what resonates with the audience.  Look for patterns in post type (image, video, carousel), caption length, and hashtags.
    *   **Demographic Insights:**  Identify the dominant demographic groups among followers.  Consider how this aligns with the target audience.
    *   **Hashtag Performance:** Determine which hashtags are driving the most reach and engagement.
    *   **Story Performance:** Analyze story views, replies, and exits to understand what types of stories are most engaging.
4.  **Insight Generation:** Based on the trend analysis, generate actionable insights. Examples:
    *   "Follower growth spiked on [date] following the post about [topic]. Consider creating more content related to [topic]."
    *   "Posts with [specific characteristic, e.g., short captions, video format] consistently receive higher engagement.  Prioritize this type of content."
    *   "The majority of followers are located in [location]. Tailor content to appeal to this region."
    *   "The hashtag #[hashtag] is performing well.  Incorporate it into future posts."
    *   "Stories with [specific characteristic, e.g., polls, questions] have higher completion rates.  Use these more frequently."
5.  **Reporting:**  Present the insights in a clear and concise format.  This could include:
    *   Summary of key findings.
    *   Visualizations (e.g., charts, graphs) to illustrate trends.
    *   Specific recommendations for improving Instagram Business performance.

**Error Handling:**

*   If data retrieval fails, report an error and suggest checking API credentials or network connectivity.
*   If the data is incomplete or inconsistent, report the issue and attempt to proceed with the available data.
*   If no significant trends are identified, report that the data does not reveal any actionable insights at this time.
```