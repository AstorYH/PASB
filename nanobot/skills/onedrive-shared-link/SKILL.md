```skill
---
name: onedrive-shared-link
description: Generates a shareable link to a file stored in OneDrive.
metadata:
  nanobot:
    emoji: ☁️
    category: storage
    tags: [onedrive, sharing, link]
---

## Skill: OneDrive Shared Link

This skill allows you to create a shareable link to a file stored in your OneDrive account.  The agent will prompt you for the file path and desired sharing permissions.

**Instructions:**

1.  **Identify the File:** Determine the full path to the file you want to share within your OneDrive. This path will be needed in the next step.  Example: `/Documents/Project Reports/Q3 Report.docx`
2.  **Request Permissions:** The agent will ask you to specify the desired sharing permissions.  Options include:
    *   `view`:  Allows anyone with the link to view the file.
    *   `edit`: Allows anyone with the link to view and edit the file.
3.  **Generate Link:**  The agent will use the file path and permissions to generate a OneDrive shared link.
4.  **Output Link:** The agent will output the generated shared link.  Copy and distribute this link as needed.

**Example Interaction:**

```
User: Create a OneDrive shared link for /Documents/Project Reports/Q3 Report.docx
Agent: What sharing permissions do you want to use? (view/edit)
User: view
Agent: Here's your OneDrive shared link: https://1drv.ms/XXXXXXXXXXXXXXX
```

**Error Handling:**

*   **Invalid File Path:** If the provided file path is invalid or the file does not exist, the agent will report an error.
*   **Permission Error:** If the agent lacks the necessary permissions to share the file, it will report an error.
*   **OneDrive Unavailable:** If OneDrive is unavailable, the agent will report an error.
```