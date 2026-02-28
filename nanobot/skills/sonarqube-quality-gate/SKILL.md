```skill
---
name: sonarqube-quality-gate
description: Checks the status of a SonarQube Quality Gate and reports its result.
metadata:
  nanobot:
    emoji: 🚦
    category: analysis
    tags: [quality, sonarqube, gate]
---

## SonarQube Quality Gate Skill

This skill checks the status of a SonarQube Quality Gate for a given project.

**Instructions:**

1.  **Project Key:** You will be provided with a project key (e.g., `my-project`). This is the unique identifier for the project in SonarQube.
2.  **SonarQube URL:** You will be provided with the SonarQube server URL (e.g., `https://sonarqube.example.com`).
3.  **Authentication:**  You may be provided with a SonarQube token or credentials. If so, use them to authenticate with the SonarQube server.  If no credentials are provided, attempt unauthenticated access.
4.  **API Request:** Construct an API request to the SonarQube server to retrieve the Quality Gate status for the specified project. The endpoint is typically: `[SonarQube URL]/api/qualitygates/project_status?projectKey=[Project Key]`.
5.  **Response Parsing:** Parse the JSON response from the API request. The response will contain information about the Quality Gate status, including:
    *   `project`: The project key.
    *   `qualityGate`: An object containing the Quality Gate status.
    *   `qualityGate.status`: The status of the Quality Gate (e.g., `OPEN`, `PASSED`, `FAILED`).
6.  **Reporting:** Report the Quality Gate status to the user.  The report should include:
    *   The project key.
    *   The Quality Gate status (e.g., "PASSED", "FAILED", "OPEN").
    *   A brief explanation of what the status means (e.g., "The Quality Gate has passed, indicating that the code meets the defined quality standards.").
7.  **Error Handling:** If the API request fails or the response cannot be parsed, report an error to the user, including the error message.  Also report an error if the project key is invalid or the SonarQube server is unreachable.

**Example Report (PASSED):**

```
Project: my-project
Quality Gate Status: PASSED
The Quality Gate has passed, indicating that the code meets the defined quality standards.
```

**Example Report (FAILED):**

```
Project: my-project
Quality Gate Status: FAILED
The Quality Gate has failed, indicating that the code does not meet the defined quality standards.  Review the SonarQube analysis for details.
```

**Example Report (OPEN):**

```
Project: my-project
Quality Gate Status: OPEN
The Quality Gate is currently open, meaning an analysis has not yet been completed or the results are still being processed.
```

**Example Error Report:**

```
Error: Could not connect to SonarQube server at https://sonarqube.example.com. Please check the URL and your network connection.
```
```