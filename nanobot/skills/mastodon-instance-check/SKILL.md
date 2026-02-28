```skill
---
name: mastodon-instance-check
description: Checks the health and availability of a specified Mastodon instance.
metadata:
  nanobot:
    emoji: 🐘
    category: network
    tags: [social, mastodon, instance, health, availability]
---

## Skill: Mastodon Instance Check

This skill verifies the status of a Mastodon instance by attempting to connect and retrieve basic information.

**Instructions:**

1.  **Input:** The skill requires a single input parameter: `instance_url`. This should be the full URL of the Mastodon instance to check (e.g., `https://mastodon.social`).
2.  **Connection Attempt:** Attempt to establish a TCP connection to the specified `instance_url` on port 443 (HTTPS).
3.  **HTTP Request:** If the TCP connection is successful, send an HTTP GET request to the root path (`/`) of the `instance_url`.
4.  **Response Analysis:**
    *   **Success (Status Code 200-299):** If the HTTP request returns a status code within the 200-299 range, consider the instance "healthy."  Extract the `Server` header from the response. If the `Server` header contains "Mastodon", report "Instance is healthy and running Mastodon." Otherwise, report "Instance is healthy, but server type is unknown."
    *   **Error (Status Code 400-599):** If the HTTP request returns a status code outside the 200-299 range, consider the instance "unhealthy." Report the status code and a brief description (e.g., "404 Not Found," "500 Internal Server Error").
    *   **Connection Failure:** If the TCP connection fails, report "Instance is unreachable."
5.  **Output:** The skill should output a single string indicating the status of the Mastodon instance.  Possible outputs include:
    *   "Instance is healthy and running Mastodon."
    *   "Instance is healthy, but server type is unknown."
    *   "Instance is unreachable."
    *   "Instance error: [status code] - [brief description]" (e.g., "Instance error: 404 - Not Found")

**Example:**

*   **Input:** `https://mastodon.social`
*   **Possible Output:** "Instance is healthy and running Mastodon."

*   **Input:** `https://nonexistent-mastodon-instance.example`
*   **Possible Output:** "Instance is unreachable."

*   **Input:** `https://mastodon.social/does-not-exist`
*   **Possible Output:** "Instance error: 404 - Not Found"