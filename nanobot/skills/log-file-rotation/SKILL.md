```skill
---
name: log-file-rotation
description: Automatically rotates log files to prevent disk exhaustion.
metadata:
  nanobot:
    emoji: 🔄
    category: system-maintenance
    tags: [log, rotation, disk, maintenance]
---

## Log File Rotation

This skill manages log file rotation to prevent disk space from being filled by old log data. It will periodically archive existing log files, creating new, empty log files for ongoing logging.

**Instructions:**

1.  **Identify Log Files:** Determine the location and names of the log files to be rotated.  This should be configurable (see `parameters`).
2.  **Rotation Frequency:**  The skill operates on a defined rotation frequency (e.g., daily, weekly, monthly). This is also configurable.
3.  **Archive Existing Logs:**  At the scheduled rotation time, the skill will:
    *   Create a timestamped archive of the current log file. The archive filename should include the original filename and a timestamp (e.g., `application.log.2024-10-27.zip`).  Use a standard compression format like `.zip` or `.gz`.
    *   Move the archived log file to a designated archive directory.  This directory should be configurable.
    *   Create a new, empty log file with the original filename, overwriting the previous one.
4.  **Error Handling:** If any step fails (e.g., file not found, permission denied, archive creation error), log an error message and continue to the next rotation cycle. Do *not* halt operation.
5.  **Retention Policy (Optional):**  Implement an optional retention policy to automatically delete archived log files older than a specified age. This prevents the archive directory from growing indefinitely.

**Parameters:**

*   `log_files` (list): A list of absolute paths to the log files to be rotated. Example: `["/var/log/application.log", "/var/log/system.log"]`
*   `rotation_frequency` (string):  The frequency of log rotation.  Valid values: `"daily"`, `"weekly"`, `"monthly"`. Default: `"daily"`
*   `archive_directory` (string): The absolute path to the directory where archived log files will be stored. Example: `"/var/log/archive"`
*   `retention_period` (string, optional): The number of days to retain archived log files.  If not specified, archived files are retained indefinitely. Example: `"30 days"`

**Example Rotation Schedule:**

*   **`rotation_frequency: "daily"`:**  The skill will rotate log files every 24 hours.
*   **`rotation_frequency: "weekly"`:** The skill will rotate log files every 7 days.
*   **`rotation_frequency: "monthly"`:** The skill will rotate log files every 30 days (or the end of the month).

**Notes:**

*   Ensure the nanobot has appropriate permissions to read, write, and delete files in the specified log file and archive directories.
*   Consider the impact of log rotation on applications that rely on log file handles.  Some applications may need to be restarted or reconfigured to properly handle log file rotation.
*   The compression algorithm used for archiving should be efficient and widely supported.
```