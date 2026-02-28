```skill
---
name: system-path-cleaner
description: Removes obsolete or redundant files and directories from a designated system path to optimize storage and performance.
metadata:
  nanobot:
    emoji: 🧹
    category: maintenance
    tags: [system, path, cleanup, optimization, storage]
---

## System Path Cleaner Skill

This skill allows the nanobot to clean up a specified system path by identifying and removing obsolete or redundant files and directories.  The cleaning process prioritizes safety and avoids deleting essential system files.

**Instructions:**

1.  **Input:** The skill requires a single input parameter: `path`. This parameter is a string representing the absolute path to the directory you want to clean.  Example: `/var/log/application_logs`.
2.  **Analysis Phase:**
    *   **Path Validation:** Verify that the provided `path` exists and is a directory. If not, report an error and terminate the skill.
    *   **File Age Assessment:**  For each file within the specified `path`, determine its last modified time.  Files older than a configurable threshold (default: 30 days) are flagged as potential candidates for removal.  This threshold can be adjusted via a future configuration option.
    *   **Redundancy Detection:**  Identify duplicate files within the `path`.  This can be done by comparing file hashes (e.g., MD5 or SHA-256).  If duplicates are found, one copy is flagged for removal (prioritizing the older copy).
    *   **Directory Size Analysis:**  For each subdirectory within the `path`, calculate its size.  Empty directories are flagged for removal.  Directories containing only files older than the age threshold are also flagged.
3.  **Confirmation Phase:**
    *   **Report Findings:**  Present a summary of the findings to the user, including:
        *   Number of files older than the age threshold.
        *   Number of duplicate files found.
        *   Number of empty directories.
        *   Number of directories containing only old files.
        *   Total estimated space that could be reclaimed.
    *   **User Confirmation:**  Request explicit user confirmation before proceeding with the removal process.  The user should be able to approve the entire cleanup or selectively approve individual files/directories.
4.  **Execution Phase (Upon User Approval):**
    *   **Safe Removal:**  Carefully remove the files and directories that were approved during the confirmation phase.  Implement robust error handling to prevent data loss.
    *   **Logging:**  Log all actions taken during the cleanup process, including files/directories removed and any errors encountered.
5.  **Completion:** Report success or failure to the user.

**Error Handling:**

*   Invalid `path` provided.
*   Insufficient permissions to access the `path`.
*   Errors encountered during file removal (e.g., file in use).
*   Disk space errors.

**Future Considerations:**

*   Configurable age threshold for file removal.
*   More sophisticated redundancy detection algorithms (e.g., content-based similarity).
*   Integration with backup systems to ensure data safety.
*   Option to move files to a quarantine directory instead of permanently deleting them.
```