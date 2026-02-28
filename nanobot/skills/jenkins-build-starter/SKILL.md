```skill
---
name: jenkins-build-starter
description: Initiates a build within a Jenkins instance based on provided parameters.
metadata:
  nanobot:
    emoji: 🚀
    category: automation
    tags: [jenkins, build, automation, CI/CD]
---

## Jenkins Build Starter

This skill allows you to trigger a build in a Jenkins instance.  It requires you to provide the Jenkins URL, the job name, and any necessary build parameters.

**Instructions:**

1.  **Determine the Jenkins URL:** This is the base URL of your Jenkins server (e.g., `https://jenkins.example.com`).
2.  **Identify the Job Name:** This is the name of the Jenkins job you want to trigger.
3.  **Gather Build Parameters (Optional):**  Some Jenkins jobs require parameters to be passed during the build.  If your job uses parameters, you'll need to provide them as key-value pairs.
4.  **Execute the Skill:** Provide the following information:

    *   `jenkins_url`: The URL of the Jenkins server.
    *   `job_name`: The name of the Jenkins job.
    *   `parameters` (optional): A JSON string representing the build parameters.  For example: `{"BRANCH":"main", "VERSION":"1.2.3"}`.  If no parameters are needed, omit this field.

**Example Usage:**

```
initiate jenkins-build-starter jenkins_url=https://jenkins.example.com job_name=my-awesome-project
```

**Example Usage with Parameters:**

```
initiate jenkins-build-starter jenkins_url=https://jenkins.example.com job_name=my-awesome-project parameters='{"BRANCH":"develop", "ENVIRONMENT":"staging"}'
```

**Error Handling:**

*   If the Jenkins URL is invalid, the skill will report an error.
*   If the job name does not exist in Jenkins, the skill will report an error.
*   If the provided parameters are invalid JSON, the skill will report an error.
*   If the Jenkins server is unreachable, the skill will report an error.
```