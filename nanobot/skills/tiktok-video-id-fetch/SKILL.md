```skill
---
name: tiktok-video-id-fetch
description: Extracts the TikTok video ID from a given TikTok URL.
metadata:
  nanobot:
    emoji: 📹
    category: data-extraction
    tags: [tiktok, url, id, extraction]
---

## Instructions

This skill extracts the TikTok video ID from a provided URL.

**Input:** A string representing a TikTok URL.  This URL can be a short link (e.g., `tiktok.com/@user/video/1234567890123456`) or a longer redirect URL.

**Output:** A string representing the TikTok video ID.  If the input is not a valid TikTok URL, or if the ID cannot be extracted, return an empty string.

**Process:**

1.  **Validate URL:** Check if the input string is a valid URL.  A simple check for `http://` or `https://` followed by a domain name is sufficient for this purpose. If not, return an empty string.
2.  **Parse URL:** Parse the URL to extract the path component.
3.  **Extract ID:**
    *   If the path starts with `/video/`, extract the ID as the part after `/video/`.
    *   If the path starts with `/@username/video/`, extract the ID as the part after `/@username/video/`.
    *   If the path contains `/item/`, extract the ID as the part after `/item/`.
    *   If the path contains `/v/`, extract the ID as the part after `/v/`.
4.  **Return ID:** Return the extracted ID.

**Examples:**

| Input URL                               | Output ID        |
| --------------------------------------- | ----------------- |
| `https://www.tiktok.com/@user/video/1234567890123456` | `1234567890123456` |
| `https://tiktok.com/video/9876543210987654` | `9876543210987654` |
| `https://www.tiktok.com/@anotheruser/video/5555555555555555` | `5555555555555555` |
| `https://www.tiktok.com/@someuser/item/abcdefg123456` | `abcdefg123456` |
| `https://www.tiktok.com/@testuser/v/hijklmnop789012` | `hijklmnop789012` |
| `https://example.com/not-a-tiktok-url` | ``                |
| `invalid url`                           | ``                |
```