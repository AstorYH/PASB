```skill
---
name: account-preference-sync
description: Synchronizes user account preferences across all connected devices and services.
metadata:
  nanobot:
    emoji: ⚙️
    category: system
    tags: [account, preferences, sync, configuration]
---

## Account Preference Sync

This skill ensures user account preferences are consistent across all devices and services. It operates by identifying and reconciling discrepancies in settings related to display, notifications, security, and accessibility.

**Instructions:**

1.  **Identify Target Accounts:** Determine which accounts require synchronization. Prioritize accounts with frequent usage or known inconsistencies.  This includes, but is not limited to: email, social media, cloud storage, and operating system accounts.
2.  **Gather Current Preferences:** For each target account, retrieve the current preference settings from all connected devices and services.  This involves querying APIs, reading local configuration files, and accessing device settings.
3.  **Establish a Master Source:** Designate a "master" source for each preference category. This could be the device the user is currently using, a central cloud server, or a previously designated preferred device.  The master source's preferences will be used as the baseline for synchronization.
4.  **Compare and Identify Discrepancies:** Compare the preferences from each device/service against the master source for each category.  Flag any differences.
5.  **Resolve Conflicts:** If conflicts exist (e.g., different notification settings on different devices), apply a conflict resolution strategy.  Options include:
    *   **Prioritize Master Source:** Overwrite the device/service preference with the master source preference.
    *   **User Prompt:**  Alert the user to the conflict and allow them to choose which preference to apply. (This requires a higher-level interaction capability not currently implemented.)
    *   **Smart Resolution:**  Attempt to intelligently resolve the conflict based on context (e.g., use the device's location to determine notification preferences).
6.  **Apply Changes:**  Update the preferences on each device/service to match the master source (or the user's chosen preference). This may involve API calls, file modifications, or device setting changes.
7.  **Verification:** After applying changes, verify that the preferences have been successfully synchronized by re-querying the settings from each device/service.
8.  **Logging:** Log all synchronization events, including any conflicts encountered and how they were resolved. This information can be used for debugging and improving the synchronization process.

**Error Handling:**

*   **API Errors:** Handle API errors gracefully. Retry failed requests with exponential backoff.
*   **Permission Errors:** If a device/service lacks the necessary permissions to modify preferences, log the error and skip synchronization for that device/service.
*   **Configuration Errors:** If the configuration files are corrupted or inaccessible, log the error and attempt to restore them from a backup.
*   **Network Errors:** Handle network connectivity issues by queuing synchronization tasks and retrying them when the network is restored.