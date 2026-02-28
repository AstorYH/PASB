```skill
---
name: github-action-trigger
description: Triggers a GitHub Actions workflow based on a provided workflow file and event.
metadata:
  nanobot:
    emoji: 🚀
    category: integration
    tags: [github, action, trigger, workflow]
---

## Skill: github-action-trigger

This skill allows the nanobot to trigger a GitHub Actions workflow.  It requires the workflow file path and the event that should trigger the workflow.

**Instructions:**

1.  **Workflow File Path:** Provide the path to the workflow file within the repository (e.g., `.github/workflows/my-workflow.yml`). This is a *required* parameter.
2.  **Event:** Specify the event that should trigger the workflow.  Valid events include (but are not limited to):
    *   `push`: Triggered on a push to the repository.
    *   `pull_request`: Triggered on a pull request event.
    *   `issue_opened`: Triggered when a new issue is opened.
    *   `issue_closed`: Triggered when an issue is closed.
    *   `schedule`: Triggered by a scheduled event (requires a cron expression in the workflow file).
    *   `repository_dispatch`: Triggered by a custom event dispatched from another system.
    This is a *required* parameter.
3.  **Optional Parameters:**
    *   `token`: (string) A GitHub personal access token (PAT) with `repo` scope. If not provided, the nanobot will attempt to use the default GITHUB_TOKEN.  **WARNING:** Using a PAT is generally more secure than relying on the GITHUB_TOKEN, especially for private repositories.
    *   `ref`: (string) The branch or tag to trigger the workflow on.  Defaults to the default branch (usually `main` or `master`).  Relevant for `push` events.
    *   `inputs`: (JSON string) A JSON string containing input values to pass to the workflow.  For example: `{"name":"My Input", "value":"My Value"}`.  This allows you to dynamically configure the workflow.

**Example Usage:**

```
trigger-github-action workflow_file=".github/workflows/deploy.yml" event="push" ref="main" token="YOUR_GITHUB_TOKEN" inputs='{"environment":"production", "version":"1.2.3"}'
```

This example triggers the `deploy.yml` workflow on a `push` event to the `main` branch, using the provided GitHub token and passing the `environment` and `version` inputs to the workflow.

**Error Handling:**

*   If the workflow file path is invalid or the workflow file does not exist, the skill will return an error.
*   If the event is not supported, the skill will return an error.
*   If the GitHub token is invalid or lacks the necessary permissions, the skill will return an error.
*   If the `inputs` parameter is not valid JSON, the skill will return an error.
*   If the GitHub API request fails for any other reason, the skill will return an error.

**Security Considerations:**

*   **GitHub Token Security:**  Treat GitHub tokens as highly sensitive credentials.  Never hardcode them directly into the skill definition.  Use environment variables or a secure secrets management system.
*   **Input Validation:**  Carefully validate any input values passed to the workflow to prevent potential security vulnerabilities (e.g., command injection).
```