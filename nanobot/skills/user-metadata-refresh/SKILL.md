```skill
---
name: user-metadata-refresh
description: Updates user metadata based on recent activity and available data sources.
metadata:
  nanobot:
    emoji: 🔄
    category: data-management
    tags: [user, metadata, refresh, update, profile]
  dependencies: []
---

## User Metadata Refresh

This skill refreshes a user's metadata by analyzing recent activity and available data sources. The goal is to ensure the user's profile is as accurate and up-to-date as possible.

**Instructions:**

1.  **Identify User:** Determine the target user for metadata refresh. This could be based on a user ID, username, or other unique identifier.
2.  **Gather Recent Activity:** Collect data on the user's recent activity. This includes, but is not limited to:
    *   Recent communications (emails, messages, calls)
    *   Files accessed and modified
    *   Applications used
    *   Websites visited (if permissible and available)
    *   Location data (if available and permissible)
3.  **Access Data Sources:** Access relevant data sources that contain user metadata. Examples include:
    *   User profile database
    *   CRM system
    *   Social media profiles (if authorized)
    *   Activity logs
4.  **Analyze Data:** Analyze the collected activity data and existing metadata to identify potential updates. Consider the following:
    *   **Interests:** Infer user interests based on accessed content and applications used.
    *   **Skills:** Identify potential skills based on applications used and tasks performed.
    *   **Role/Title:** Update role or title if indicated by recent communications or activity.
    *   **Location:** Update location based on recent location data.
    *   **Contact Information:** Verify and update contact information if necessary.
5.  **Apply Updates:** Apply the identified updates to the user's metadata in the designated data sources. Ensure data integrity and consistency across all sources.
6.  **Verification:** After applying updates, perform a verification check to ensure the changes were successful and accurate. Log any errors or discrepancies.
7.  **Completion:** Report the completion of the metadata refresh process, including any updates made and any errors encountered.

**Example Scenario:**

A user has recently been accessing several documents related to "machine learning" and using a "Python IDE." The skill should update the user's metadata to reflect an interest in "machine learning" and potentially add "Python programming" to their skills list.

**Error Handling:**

*   If a data source is unavailable, log the error and attempt to refresh metadata from other available sources.
*   If an update fails, log the error and retry the update later.
*   If conflicting data is detected, prioritize the most recent and reliable data source.