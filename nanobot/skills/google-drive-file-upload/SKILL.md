```skill
---
name: drive-file-upload
description: Uploads a file to a specified Google Drive folder.
metadata:
  nanobot:
    emoji: ⬆️
    category: storage
    tags: [cloud, drive, upload, file]
  dependencies: []
---

## Skill: drive-file-upload

This skill allows the nanobot to upload a file to a Google Drive folder.

**Instructions:**

1.  **Authentication:** This skill requires Google Drive API access. Ensure the nanobot has been authenticated with a Google account and has the necessary permissions to upload files to the target folder.  Authentication details are handled externally and assumed to be pre-configured.

2.  **Input Parameters:** The nanobot will receive the following parameters:
    *   `file_path` (string): The absolute path to the file to be uploaded.
    *   `folder_id` (string): The ID of the Google Drive folder where the file should be uploaded.  This is a string representing the folder's unique identifier.
    *   `file_name` (string, optional): The desired name for the file in Google Drive. If not provided, the original file name will be used.

3.  **Process:**
    *   Verify that the `file_path` exists and is a valid file. If not, report an error and terminate the skill.
    *   Retrieve the file contents from the `file_path`.
    *   Construct the Google Drive API request to upload the file.  The request should include:
        *   The file contents.
        *   The `folder_id` as the parent folder.
        *   The `file_name` (if provided, otherwise use the original file name).
        *   Appropriate MIME type based on the file extension (e.g., "application/pdf" for PDF files, "image/jpeg" for JPEG images).  If the file extension is unknown, default to "application/octet-stream".
    *   Execute the Google Drive API request.
    *   Check the API response for success or failure.

4.  **Output:**
    *   On success: Report the Google Drive file ID of the uploaded file.
    *   On failure: Report an error message indicating the reason for the failure (e.g., invalid file path, insufficient permissions, API error).

**Error Handling:**

*   **File Not Found:** If the `file_path` does not exist, report an error: "Error: File not found at specified path."
*   **Insufficient Permissions:** If the nanobot does not have permission to access the file or upload to the folder, report an error: "Error: Insufficient permissions to access file or upload to Google Drive folder."
*   **API Error:** If the Google Drive API returns an error, report the error message received from the API.
*   **Invalid Folder ID:** If the `folder_id` is invalid, report an error: "Error: Invalid Google Drive folder ID."

**Example:**

```
file_path: /home/user/documents/report.pdf
folder_id: 1abc2def3ghi4jkl5mno
file_name: Final_Report.pdf
```
```