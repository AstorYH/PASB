```skill
---
name: bitbucket-pull-request
description: Creates a new pull request in Bitbucket, merging specified branches.
metadata:
  nanobot:
    emoji: 🚀
    category: code-management
    tags: [bitbucket, pull request, merge, code]
  dependencies: []
---

## Bitbucket Pull Request Skill

This skill allows the nanobot to create a new pull request in Bitbucket.

**Instructions:**

1.  **Gather Information:** The nanobot needs the following information to create the pull request:
    *   `repository`: The Bitbucket repository slug (e.g., `myorg/myrepo`).
    *   `source_branch`: The branch to be merged (e.g., `feature/new-feature`).
    *   `target_branch`: The branch to merge into (e.g., `develop`).
    *   `title`: A descriptive title for the pull request.
    *   `description`: A detailed description of the changes included in the pull request.  This should explain the purpose of the changes and any relevant context.
    *   `assignees` (optional): A list of Bitbucket usernames to assign to the pull request.
    *   `labels` (optional): A list of labels to apply to the pull request.

2.  **Construct the API Request:**  The nanobot will construct a request to the Bitbucket API to create a pull request. The request will include the gathered information.  The API endpoint is typically something like `/rest/api/1.0/repositories/{repository}/pullrequests`.  The exact endpoint may vary depending on the Bitbucket version.

3.  **Execute the Request:** The nanobot will execute the API request.

4.  **Handle the Response:**
    *   **Success:** If the request is successful (HTTP 201 Created), the response will contain the details of the newly created pull request, including its URL. The nanobot should report the success and provide the pull request URL.
    *   **Failure:** If the request fails (e.g., HTTP 400 Bad Request, HTTP 401 Unauthorized, HTTP 404 Not Found), the nanobot should report the failure and include the error message from the Bitbucket API.  Common errors include invalid repository name, incorrect branch names, or insufficient permissions.

**Example Interaction:**

```
User: Create a Bitbucket pull request for repository 'myorg/myrepo', merging 'feature/new-feature' into 'develop'. Title: "Implement new feature X". Description: "This pull request implements the new feature X as described in ticket #123." Assignees: 'user1', 'user2'. Labels: 'feature', 'urgent'.
```

**Expected Response:**

```
Pull request created successfully: https://bitbucket.org/myorg/myrepo/pull-requests/123
```

**Error Handling:**

*   If any required information is missing, the nanobot should prompt the user for the missing information.
*   If the Bitbucket API returns an error, the nanobot should report the error to the user in a clear and concise manner.
*   If the repository does not exist, the nanobot should report that the repository was not found.
*   If the user does not have permission to create pull requests in the specified repository, the nanobot should report a permission error.
```