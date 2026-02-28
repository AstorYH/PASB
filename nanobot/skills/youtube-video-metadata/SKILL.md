```skill
---
name: youtube-video-metadata
description: Extracts metadata (title, description, tags, upload date) from a YouTube video URL.
metadata:
  nanobot:
    emoji: 🎬
    type: information
    category: web-interaction
    tags: [youtube, metadata, video, information]
  dependencies: []
---

## Skill Instructions

This skill allows you to extract metadata from a YouTube video given its URL.

**Input:**

*   `url`: A string representing the URL of the YouTube video.  Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

**Process:**

1.  **Validate URL:** Ensure the input `url` is a valid YouTube video URL.  A basic check is to see if it starts with `https://www.youtube.com/watch?v=`.  If not, report an error and stop.
2.  **Fetch HTML:** Retrieve the HTML content of the provided YouTube video URL.
3.  **Parse HTML:** Parse the HTML content to extract the following metadata:
    *   `title`: The title of the video. Look for the `<title>` tag in the HTML.
    *   `description`: The video description.  Look for a `<p>` tag with the class "content" or similar, containing the description.
    *   `tags`: The video tags. These are often embedded in the description or in a meta tag.  Look for meta tags with the name "keywords" or similar.  If tags are found in the description, extract them by splitting the description string by commas.
    *   `upload_date`: The date the video was uploaded. This is often found in a meta tag with the name "upload-date" or similar.  If not found, attempt to extract it from the video page's HTML structure (e.g., looking for a "Published on" label).
4.  **Return Metadata:** Return the extracted metadata as a dictionary.

**Output:**

A dictionary containing the extracted metadata.  The dictionary should have the following keys:

*   `title`: (string) The title of the video.
*   `description`: (string) The video description.
*   `tags`: (list of strings) A list of video tags.
*   `upload_date`: (string) The date the video was uploaded (in a standard format like YYYY-MM-DD).

**Error Handling:**

*   If the URL is invalid, return an error message: "Invalid YouTube URL."
*   If the HTML cannot be fetched, return an error message: "Failed to fetch HTML."
*   If any of the metadata fields cannot be extracted, return `None` for that field in the output dictionary.

**Example:**

**Input:**

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
}
```

**Output:**

```json
{
  "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
  "description": "Never gonna give you up, never gonna let you down...",
  "tags": ["Rick Astley", "Never Gonna Give You Up", "Music Video", "80s", "Pop"],
  "upload_date": "2008-05-22"
}
```
```