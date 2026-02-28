```skill
---
name: disk-space-checker
description: Checks the available disk space on the current storage device.
metadata:
  nanobot:
    emoji: 💾
    category: system
    tags:
      - storage
      - monitoring
      - system-health
---

## Disk Space Checker

This skill assesses the available disk space on the system's primary storage device. It provides a report on total capacity, used space, and free space.

**Instructions:**

1.  **Identify Storage Device:** Determine the primary storage device (e.g., `/`, `C:`, `/dev/sda1`).  Assume `/` if no other information is available.
2.  **Retrieve Disk Information:** Use the appropriate system command to obtain disk space information.  Examples:
    *   Linux/macOS: `df -h /`
    *   Windows: `wmic logicaldisk where DriveType=3 get FreeSpace,Size,Caption`
3.  **Parse Output:** Extract the following values from the command output:
    *   `total`: Total disk space in human-readable format (e.g., "250G").
    *   `used`: Used disk space in human-readable format (e.g., "180G").
    *   `free`: Free disk space in human-readable format (e.g., "70G").
4.  **Report:**  Present the information in a clear and concise format.  For example:

    ```
    Disk Space Report:

    Total: 250G
    Used: 180G
    Free: 70G
    ```

**Error Handling:**

*   If the command fails to execute, report an error: "Unable to retrieve disk space information."
*   If the output cannot be parsed, report an error: "Unable to parse disk space information."
```