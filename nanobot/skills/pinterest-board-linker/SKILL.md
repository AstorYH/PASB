```skill
---
name: pinterest-board-linker
description: Creates a Pinterest board link from a given board name.
metadata:
  nanobot:
    emoji: 📌
    category: communication
    tags: [social media, pinterest, link]
---

## Pinterest Board Linker

This skill generates a Pinterest board link given a board name.

**Instructions:**

1.  **Input:** You will receive a string representing the name of a Pinterest board.
2.  **Processing:** Construct the Pinterest board URL using the following format: `https://www.pinterest.com/YOUR_USERNAME/BOARD_NAME/`.  Replace `YOUR_USERNAME` with a placeholder (e.g., "pinterestuser") and `BOARD_NAME` with the board name provided as input.  Encode the `BOARD_NAME` to be URL-safe (replace spaces with `%20`, and other special characters as needed).
3.  **Output:** Return the constructed Pinterest board URL as a string.

**Example:**

*   **Input:** "My Vacation Photos"
*   **Output:** `https://www.pinterest.com/pinterestuser/My%20Vacation%20Photos/`

**Error Handling:**

*   If the input is empty or null, return an error message: "Error: Board name cannot be empty."
*   If the board name contains characters that cannot be URL-encoded, return an error message: "Error: Invalid characters in board name."
```