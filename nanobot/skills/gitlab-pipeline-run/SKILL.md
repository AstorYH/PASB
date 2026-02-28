```skill
---
name: gitlab-pipeline-run
description: Initiates a new pipeline run in a specified GitLab project.
metadata:
  nanobot:
    emoji: 🚀
    category: automation
    tags: [gitlab, pipeline, ci, cd]
  dependencies: []
---

## Skill: gitlab-pipeline-run

This skill allows you to trigger a pipeline run in a GitLab project.  You'll need to provide the project path and, optionally, a branch to run the pipeline on.

**Instructions:**

1.  **Project Path:**  You *must* specify the GitLab project path. This is the full path to the project, e.g., `group/subgroup/project-name`.
2.  **Branch (Optional):**  If you want to run the pipeline on a specific branch, provide the branch name. If omitted, the default branch of the project will be used.
3.  **Variables (Optional):** You can pass variables to the pipeline.  Provide these as a comma-separated list of `key=value` pairs.  For example: `VARIABLE1=value1,VARIABLE2=value2`.
4.  **Confirmation:** The nanobot will confirm the details of the pipeline run before executing it.  Review the confirmation and respond with "yes" to proceed.

**Example Interactions:**

*   **User:** `run gitlab pipeline on group/my-project`
    *   **Nanobot:** "Okay, I will run a pipeline on `group/my-project` using the default branch. Confirm? (yes/no)"
    *   **User:** `yes`
    *   **Nanobot:** "Pipeline run initiated.  Check GitLab for status."

*   **User:** `run gitlab pipeline on group/my-project branch=develop`
    *   **Nanobot:** "Okay, I will run a pipeline on `group/my-project` using the `develop` branch. Confirm? (yes/no)"
    *   **User:** `yes`
    *   **Nanobot:** "Pipeline run initiated.  Check GitLab for status."

*   **User:** `run gitlab pipeline on group/my-project branch=feature/new-stuff variable1=test,variable2=123`
    *   **Nanobot:** "Okay, I will run a pipeline on `group/my-project` using the `feature/new-stuff` branch, with variables `variable1=test` and `variable2=123`. Confirm? (yes/no)"
    *   **User:** `yes`
    *   **Nanobot:** "Pipeline run initiated.  Check GitLab for status."

**Error Handling:**

*   If the project path is invalid, the nanobot will respond with an error message.
*   If the branch does not exist, the nanobot will respond with an error message.
*   If the confirmation is not "yes", the pipeline run will be cancelled.
```