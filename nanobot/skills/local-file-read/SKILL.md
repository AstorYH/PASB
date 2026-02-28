```skill
---
name: local-file-read
description: Reads the contents of a specified local file.
metadata:
  nanobot:
    emoji: 📄
    category: data-access
    tags: [file, read, local]
---

## Skill: local-file-read

**Goal:** Retrieve the contents of a file located on the local system.

**Instructions:**

1.  **Input:** You will receive a string representing the absolute path to the file you need to read.  For example: `/home/user/documents/report.txt` or `C:\Users\User\Documents\report.txt`.
2.  **File Access:** Attempt to open the file specified by the provided path in read mode.
3.  **Content Retrieval:** If the file is successfully opened, read its entire contents as a single string.
4.  **Error Handling:**
    *   If the file does not exist, or you lack the necessary permissions to access it, report an error: `ERROR: File not found or access denied.`
    *   If any other error occurs during file access or reading, report a generic error: `ERROR: Unable to read file.`
5.  **Output:** If successful, output the file's contents as a single string.  If an error occurred, output the corresponding error message.

**Example:**

**Input:** `/tmp/my_data.txt`

**Possible Output (Success):**

```
This is the content of my_data.txt.
It contains some important information.
```

**Possible Output (Error):**

```
ERROR: File not found or access denied.
```

**Constraints:**

*   The file path provided will be a string.
*   Assume the file is a text file.  Do not attempt to interpret binary files.
*   Do not attempt to modify the file.  This skill is for reading only.
*   Report errors clearly and concisely.
```