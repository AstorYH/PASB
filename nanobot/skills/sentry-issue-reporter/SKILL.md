```skill
---
name: sentry-issue-reporter
description: Automatically creates a Sentry issue report when a critical error is detected.
metadata:
  nanobot:
    emoji: 🐛
    category: monitoring
    tags:
      - error
      - reporting
      - sentry
  dependencies: []
---

## Sentry Issue Reporter

This skill monitors for critical error conditions and, upon detection, automatically creates a new issue report in Sentry.

**Instructions:**

1.  **Error Detection:** Continuously monitor system logs, application output, or other relevant data streams for indications of critical errors.  Define "critical error" as a specific pattern or set of conditions (e.g., "ExceptionType: FatalError", "ErrorLevel: Critical", "SystemStatus: Down").  The exact criteria should be configurable (see "Configuration" below).

2.  **Data Extraction:** When a critical error is detected, extract relevant information to include in the Sentry issue report. This should include:
    *   Timestamp of the error
    *   Error message
    *   Stack trace (if available)
    *   System state (e.g., CPU usage, memory usage, network status)
    *   Any relevant contextual data (e.g., user ID, request parameters)

3.  **Sentry API Interaction:** Use the Sentry API to create a new issue.  The API endpoint is typically `https://sentry.io/api/0/issues/`.  You will need to authenticate with a Sentry API key (see "Configuration" below).

4.  **Issue Details:** When creating the issue, provide the following details:
    *   `title`: A concise description of the error.
    *   `description`: A detailed explanation of the error, including the extracted data.
    *   `culprit`: The component or module where the error originated (if identifiable).
    *   `level`: Set the issue level to "critical".
    *   `fingerprint`: A unique identifier for the error (e.g., a hash of the error message and stack trace).

5.  **Confirmation:** After successfully creating the issue, log a confirmation message indicating the issue ID and URL.

**Configuration:**

*   `sentry_api_key`: (Required) Your Sentry API key.  This is used to authenticate with the Sentry API.
*   `sentry_public_key`: (Required) Your Sentry public key. This is used to identify the project.
*   `sentry_project_id`: (Required) The ID of the Sentry project to create the issue in.
*   `sentry_url`: (Optional, defaults to `https://sentry.io`) The base URL of your Sentry instance.
*   `critical_error_pattern`: (Required) A regular expression or string pattern that defines what constitutes a critical error.  For example, `.*FatalError.*` or `"ErrorLevel: Critical"`.
*   `data_extraction_rules`: (Optional) A set of rules for extracting data from the error message.  These rules can be simple key-value pairs or more complex regular expressions.
*   `log_level`: (Optional, defaults to `INFO`) The logging level for this skill.

**Example:**

If a log message contains "FatalError: Disk Full", the skill might extract the following data:

*   Timestamp: 2023-10-27 10:00:00
*   Error Message: FatalError: Disk Full
*   System State: CPU Usage: 95%, Memory Usage: 80%

This data would then be used to create a Sentry issue with the title "Disk Full Error" and a description including the timestamp, error message, and system state.
```