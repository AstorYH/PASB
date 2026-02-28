```skill
---
name: vercel-deployment-check
description: Checks the status of a Vercel deployment and reports success or failure.
metadata:
  nanobot:
    emoji: 🚀
    category: deployment
    tags: [vercel, deployment, status, check]
---

## Vercel Deployment Check

This skill checks the status of a Vercel deployment. It requires the Vercel project name and deployment ID.

**Instructions:**

1.  **Obtain Vercel Project Name:** Determine the name of the Vercel project you want to check. This is typically the name of the repository on GitHub or GitLab connected to your Vercel project.
2.  **Obtain Deployment ID:** Find the ID of the specific deployment you want to check. This can be found in the Vercel dashboard under the "Deployments" tab, or in the URL when viewing a specific deployment.
3.  **Execute the Skill:** Provide the Vercel project name and deployment ID to the nanobot.
4.  **Status Reporting:** The nanobot will query the Vercel API to determine the deployment status. It will then report one of the following:
    *   `Success`: The deployment is complete and successful.
    *   `Failure`: The deployment failed.  The nanobot will attempt to provide a brief reason for the failure if available in the Vercel API response.
    *   `Pending`: The deployment is still in progress.
    *   `Unknown`: An error occurred while querying the Vercel API.

**Example Input:**

```
vercel-deployment-check project-name=my-awesome-project deployment-id=1234567890
```

**Error Handling:**

*   If the Vercel project name or deployment ID is missing, the nanobot will prompt the user to provide them.
*   If the Vercel API returns an error, the nanobot will report an "Unknown" status and include the error message in its response.
*   If the deployment ID is invalid, the nanobot will report an "Unknown" status.
```