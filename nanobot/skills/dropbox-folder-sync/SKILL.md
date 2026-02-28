```skill
---
name: dropbox-folder-sync
description: Synchronizes the contents of a specified local folder with a designated Dropbox folder.
metadata:
  nanobot:
    emoji: ☁️
    category: data-management
    tags: [cloud, storage, synchronization, folder]
  dependencies: []
---

## Instructions

This skill allows you to synchronize a local folder with a Dropbox folder.  The synchronization is one-way, from the local folder *to* the Dropbox folder.  Any changes made to files in the local folder will be reflected in the Dropbox folder, and vice versa.  This is *not* a two-way sync; changes made *within* Dropbox will not be reflected locally.

**Prerequisites:**

*   You must have access to a Dropbox account.
*   You must have the Dropbox API key and access token.  These are *not* stored within the nanobot; you will need to provide them dynamically.
*   The local folder you wish to synchronize must exist.

**Execution:**

1.  **Identify the Local Folder:** Determine the absolute path to the local folder you want to synchronize.  This is the source of the data.
2.  **Identify the Dropbox Folder:** Determine the path to the folder within your Dropbox account that you want to synchronize *to*. This is the destination.
3.  **Authentication:** Provide the Dropbox API key and access token.  The nanobot will use these to authenticate with the Dropbox API.
4.  **Synchronization:** The nanobot will iterate through all files and subfolders within the local folder. For each item:
    *   **Check for Existence:** It will check if the item already exists in the Dropbox folder.
    *   **Upload/Update:** If the item does not exist, it will upload it to the Dropbox folder. If the item *does* exist, it will compare the modification timestamps. If the local version is newer, it will upload the updated version.
    *   **Handle Errors:** If an upload fails, log the error and continue with the next item. Do not halt the entire synchronization process.
5.  **Reporting:** After the synchronization is complete, report the number of files uploaded/updated and any errors encountered.

**Input Parameters:**

*   `local_folder_path` (string): The absolute path to the local folder to synchronize.  Example: `/Users/myuser/Documents/myfolder`
*   `dropbox_folder_path` (string): The path to the Dropbox folder to synchronize to. Example: `/MySyncedFolder`
*   `dropbox_api_key` (string): Your Dropbox API key.
*   `dropbox_access_token` (string): Your Dropbox access token.

**Output:**

A report indicating the number of files synchronized and any errors encountered.  Example:

```
Synchronization complete.
Files uploaded/updated: 123
Errors: 0
```

or

```
Synchronization complete.
Files uploaded/updated: 100
Errors: 1 (Failed to upload file: /Users/myuser/Documents/myfolder/image.jpg - Permission denied)
```

**Error Handling:**

*   **Invalid Paths:** If either `local_folder_path` or `dropbox_folder_path` is invalid, report an error.
*   **Authentication Errors:** If the API key or access token is invalid, report an authentication error.
*   **Network Errors:** Handle network errors gracefully and retry failed uploads.
*   **Dropbox API Errors:**  Log any errors returned by the Dropbox API.
*   **Permission Errors:** Handle permission errors when accessing local files or the Dropbox folder.
```