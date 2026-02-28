```skill
---
name: npm-package-version
description: Determines the latest published version of an NPM package.
metadata:
  nanobot:
    emoji: 📦
    category: information
    tags:
      - npm
      - package
      - version
      - dependency
    complexity: low
    risk: none
---

## Skill Instructions

This skill retrieves the latest published version of a specified NPM package.

**Input:**

*   `package_name` (string): The name of the NPM package to query.  This is a required parameter.

**Process:**

1.  Query the NPM registry for the specified `package_name`.
2.  Extract the latest published version number from the registry response.
3.  Return the version number as a string.

**Output:**

*   `version` (string): The latest published version of the NPM package.  If the package is not found, return "Not Found".

**Error Handling:**

*   If the NPM registry is unavailable, return "Registry Unavailable".
*   If the `package_name` is invalid or empty, return "Invalid Package Name".

**Example:**

*   **Input:** `package_name = react`
*   **Output:** `version = 18.2.0` (or whatever the latest version is at the time of execution)

*   **Input:** `package_name = non-existent-package`
*   **Output:** `version = Not Found`

*   **Input:** `package_name = ""`
*   **Output:** `version = Invalid Package Name`
```