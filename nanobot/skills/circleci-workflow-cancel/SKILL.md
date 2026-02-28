```skill
---
name: circleci-workflow-cancel
description: Cancels a specific CircleCI workflow by its ID.
metadata:
  nanobot:
    emoji: 🛑
    category: infrastructure
    tags: [circleci, workflow, cancel, automation]
---

## CircleCI Workflow Cancel

This skill allows you to cancel a CircleCI workflow given its workflow ID.  It's useful for stopping long-running or erroneous builds.

**Instructions:**

1.  **Identify the Workflow ID:** You need the ID of the CircleCI workflow you want to cancel. This ID is a long string of characters and numbers, typically found in the CircleCI web interface URL (e.g., `https://app.circleci.com/workflows/<workflow_id>`).
2.  **Provide the Workflow ID:**  Provide the workflow ID to the agent.  The agent will then construct and execute the necessary API call to cancel the workflow.
3.  **Confirmation:** The agent will report whether the cancellation was successful or if an error occurred.

**Example Interaction:**

```
User: Cancel CircleCI workflow with ID 12345678-9abc-def0-1234-567890abcdef
Agent: Cancelling CircleCI workflow 12345678-9abc-def0-1234-567890abcdef...
Agent: Workflow cancellation successful.
```

**Error Handling:**

*   **Invalid Workflow ID:** If the provided ID is not a valid CircleCI workflow ID, the agent will report an error.
*   **Insufficient Permissions:** If the agent does not have the necessary permissions to cancel the workflow, it will report an error.
*   **Workflow Already Completed:** If the workflow has already completed (either successfully or unsuccessfully), the agent will report an error.
*   **API Errors:**  Any errors from the CircleCI API will be reported.

**Important Considerations:**

*   This skill assumes the agent has been configured with appropriate CircleCI API credentials (API token) and project access.  This configuration is outside the scope of this skill definition.
*   Cancelling a workflow will stop all currently running jobs within that workflow.
*   Use this skill with caution, as it can disrupt ongoing builds.
```