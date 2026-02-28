```skill
---
name: asana-project-backup
description: Backs up an Asana project's tasks and details to a local data store.
metadata:
  nanobot:
    emoji: 💾
    category: data-management
    tags: [asana, backup, data, project, tasks]
---

# Asana Project Backup

This skill allows you to create a local backup of an Asana project, including task details, assignees, due dates, and custom fields.  The backup will be stored in a structured format (JSON) within the nanobot's local storage.

## Instructions

1.  **Identify the Asana Project:** You will need the *Project ID* of the Asana project you wish to back up.  You can find this in the URL of the project in Asana (e.g., `https://app.asana.com/0/project/YOUR_PROJECT_ID`).
2.  **Access Asana API:** The nanobot will use its internal Asana API access (assumed to be pre-configured).  If API access is not available, the skill will fail.
3.  **Fetch Project Tasks:** Use the Asana API to retrieve all tasks within the specified project.  Handle pagination if the project has a large number of tasks.
4.  **Extract Task Details:** For each task, extract the following information:
    *   `task_id`: The unique identifier for the task.
    *   `name`: The task's name.
    *   `assignee`: The user assigned to the task (user ID or name).
    *   `due_date`: The task's due date (in ISO 8601 format, if available).
    *   `completed`: A boolean indicating whether the task is completed.
    *   `custom_fields`: A dictionary of custom field names and their values.
    *   `dependencies`: A list of task IDs that this task depends on.
    *   `tags`: A list of tags associated with the task.
5.  **Structure the Data:** Organize the extracted task details into a JSON structure.  The top-level structure should be a dictionary with the following keys:
    *   `project_id`: The ID of the Asana project.
    *   `tasks`: A list of dictionaries, where each dictionary represents a task and contains the extracted details.
6.  **Store the Backup:** Save the JSON data to a file within the nanobot's local storage.  The filename should be based on the project ID and a timestamp (e.g., `asana_project_backup_YOUR_PROJECT_ID_YYYYMMDDHHMMSS.json`).
7.  **Confirmation:** Report success and the location of the backup file.

## Error Handling

*   **Invalid Project ID:** If the provided Project ID is invalid, report an error.
*   **API Errors:** Handle any errors returned by the Asana API (e.g., authentication errors, rate limiting).  Retry with exponential backoff if appropriate.
*   **Storage Errors:** Handle any errors that occur while saving the backup file.
*   **No Tasks:** If the project is empty, report that the backup was created successfully but contains no tasks.

## Example Output (JSON)

```json
{
  "project_id": "1234567890",
  "tasks": [
    {
      "task_id": "9876543210",
      "name": "Write Report",
      "assignee": "john.doe",
      "due_date": "2024-12-31T00:00:00Z",
      "completed": false,
      "custom_fields": {
        "priority": "High",
        "estimated_time": "4h"
      },
      "dependencies": [],
      "tags": ["report", "urgent"]
    },
    {
      "task_id": "5555555555",
      "name": "Review Code",
      "assignee": "jane.smith",
      "due_date": "2025-01-15T00:00:00Z",
      "completed": true,
      "custom_fields": {
        "status": "Approved"
      },
      "dependencies": ["9876543210"],
      "tags": ["code", "review"]
    }
  ]
}
```