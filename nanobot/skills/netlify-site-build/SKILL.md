```skill
---
name: netlify-site-build
description: Automatically builds and deploys a website to Netlify based on a Git repository.
metadata:
  nanobot:
    emoji: 🚀
    category: deployment
    tags: [web, deployment, netlify, git]
---

## Netlify Site Build

This skill automates the process of building and deploying a website to Netlify. It requires access to a Git repository and a Netlify site ID.

**Prerequisites:**

*   **Git Repository:** The website's code must be hosted in a Git repository (e.g., GitHub, GitLab, Bitbucket).
*   **Netlify Site ID:** You need the Site ID of the Netlify site you want to deploy to. This can be found in the Netlify dashboard.
*   **Netlify API Token:** A Netlify API token with deploy permissions is required.  Store this securely.

**Instructions:**

1.  **Identify the Git Repository:** Determine the URL of the Git repository containing the website's code.
2.  **Specify the Netlify Site ID:** Provide the Site ID of the Netlify site.
3.  **Provide the Netlify API Token:** Supply the Netlify API token.
4.  **Build Command (Optional):** If your website requires a build command (e.g., `npm run build`, `yarn build`), specify it. If no build command is provided, Netlify will attempt to auto-detect the build process.
5.  **Publish Directory (Optional):** If your website's built files are located in a specific directory (e.g., `dist`, `public`), specify the publish directory. If not provided, Netlify will use the default publish directory.
6.  **Execute the Build:** The nanobot will use the Netlify API to trigger a build and deploy of the website.

**Example:**

Let's say you have a website hosted on GitHub at `https://github.com/your-username/your-repo`, and your Netlify Site ID is `your-netlify-site-id`.  You also have a Netlify API token.  Your build command is `npm run build` and your publish directory is `public`.

The nanobot would execute the following steps:

1.  Fetch the Git repository URL: `https://github.com/your-username/your-repo`
2.  Fetch the Netlify Site ID: `your-netlify-site-id`
3.  Fetch the Netlify API Token (securely).
4.  Set the build command to `npm run build`.
5.  Set the publish directory to `public`.
6.  Use the Netlify API to trigger a build and deploy with the provided information.

**Error Handling:**

*   **Invalid Git Repository URL:** The nanobot will report an error if the Git repository URL is invalid.
*   **Invalid Netlify Site ID:** The nanobot will report an error if the Netlify Site ID is invalid.
*   **Invalid Netlify API Token:** The nanobot will report an error if the Netlify API token is invalid or lacks sufficient permissions.
*   **Build Failure:** If the build process fails, the nanobot will report the error from Netlify.
*   **Deployment Failure:** If the deployment process fails, the nanobot will report the error from Netlify.
```