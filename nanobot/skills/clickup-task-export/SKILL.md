```skill
---
name: clickup-task-export
description: Exports a ClickUp task and its subtasks as a structured data object.
metadata:
  nanobot:
    emoji: 📝
    category: data-extraction
    tags: [clickup, task, export, data]
  dependencies: []
---

## ClickUp Task Export Skill

This skill extracts data from a ClickUp task and its subtasks, returning it as a structured data object.

**Input:**

*   `task_url`: (string, required) The URL of the ClickUp task to export.  This URL must be directly accessible and contain the task ID.

**Output:**

A JSON object containing the following keys:

*   `task_id`: (string) The ID of the ClickUp task.
*   `task_name`: (string) The name of the ClickUp task.
*   `task_status`: (string) The current status of the ClickUp task (e.g., "To Do", "In Progress", "Done").
*   `task_priority`: (string) The priority of the ClickUp task (e.g., "High", "Normal", "Low").
*   `task_due_date`: (string, optional) The due date of the ClickUp task in ISO 8601 format (YYYY-MM-DD).  Null if no due date is set.
*   `task_description`: (string) The description of the ClickUp task.
*   `subtasks`: (array of objects) An array of subtask objects. Each subtask object contains:
    *   `subtask_id`: (string) The ID of the subtask.
    *   `subtask_name`: (string) The name of the subtask.
    *   `subtask_status`: (string) The status of the subtask.
    *   `subtask_due_date`: (string, optional) The due date of the subtask in ISO 8601 format. Null if no due date is set.
    *   `subtask_completed`: (boolean) Whether the subtask is completed.

**Instructions:**

1.  **Validate Input:** Ensure the `task_url` is a valid URL and contains a ClickUp task ID.
2.  **Fetch Task Data:** Use the `task_url` to retrieve the ClickUp task data.  Assume the URL directly points to the task's API endpoint (e.g., `/api/task/12345`).
3.  **Parse Task Data:** Parse the retrieved data to extract the `task_id`, `task_name`, `task_status`, `task_priority`, `task_due_date`, and `task_description`.
4.  **Fetch Subtasks:** Retrieve the subtasks associated with the task using the task ID.
5.  **Parse Subtasks:** For each subtask, extract the `subtask_id`, `subtask_name`, `subtask_status`, `subtask_due_date`, and `subtask_completed` status.
6.  **Construct Output:** Create a JSON object with the extracted task data and an array of subtask objects as described in the "Output" section.
7.  **Return Output:** Return the constructed JSON object.

**Error Handling:**

*   If the `task_url` is invalid or the task cannot be found, return an error message indicating the issue.
*   If there are any errors during data retrieval or parsing, return an error message with details about the error.
```