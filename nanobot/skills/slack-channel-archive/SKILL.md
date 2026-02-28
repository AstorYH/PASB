```skill
---
name: slack-channel-archive
description: Archives a specified Slack channel, moving all messages to a compressed archive format.
metadata:
  nanobot:
    emoji: 💾
    category: data-management
    tags: [slack, archive, data, compression]
---

## Slack Channel Archive

This skill allows the nanobot to archive a Slack channel.  It will move all messages from the specified channel to a compressed archive file.  The archive will be stored locally (or in a designated storage location, if configured - see Configuration below).

**Prerequisites:**

*   Access to the Slack API with appropriate permissions to read channel history.
*   Sufficient storage space for the archive.

**Instructions:**

1.  **Identify the Channel:** The nanobot needs to know which Slack channel to archive. This is provided as an argument to the skill. The channel identifier can be the channel name (e.g., `#general`) or the channel ID (e.g., `C1234567890`).  The nanobot will attempt to resolve the name to an ID if a name is provided.
2.  **Retrieve Channel History:** The nanobot will use the Slack API to retrieve the complete message history for the specified channel. This may involve pagination if the channel has a large number of messages.
3.  **Compress the Data:** The retrieved messages will be compressed into a single archive file. The compression format will be determined by the configuration (see Configuration below).  Common formats include `.zip`, `.tar.gz`, or `.bz2`.
4.  **Store the Archive:** The compressed archive file will be stored in a designated location. The storage location is determined by the configuration (see Configuration below).
5.  **Confirmation:** The nanobot will report the successful archiving of the channel, including the archive file name and storage location.  If an error occurs, the nanobot will report the error message.

**Arguments:**

*   `channel`: (Required) The name or ID of the Slack channel to archive (e.g., `#general` or `C1234567890`).

**Configuration:**

The following configuration options can be set to customize the behavior of this skill:

*   `storage_location`: (Optional) The directory where the archive file will be stored.  Defaults to `/archives`.
*   `compression_format`: (Optional) The compression format to use.  Defaults to `zip`.  Valid values are `zip`, `tar.gz`, and `bz2`.
*   `slack_api_token`: (Required) The Slack API token with sufficient permissions.  This should be securely stored and not hardcoded.

**Error Handling:**

*   **Invalid Channel:** If the specified channel does not exist or the nanobot does not have access to it, an error message will be reported.
*   **Insufficient Permissions:** If the nanobot does not have sufficient permissions to read the channel history, an error message will be reported.
*   **Storage Error:** If there is an error writing the archive file to the storage location, an error message will be reported.
*   **API Rate Limit:** If the Slack API rate limit is exceeded, the nanobot will pause and retry the request after a short delay.

**Example Usage:**

`slack-channel-archive channel:#general`

This will archive the Slack channel named `#general` and store the archive file in the default storage location (`/archives`) using the default compression format (`zip`).
```