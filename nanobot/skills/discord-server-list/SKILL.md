```skill
---
name: discord-server-list
description: Generates a formatted list of Discord servers the user is a member of, including server name and member count.
metadata:
  nanobot:
    emoji: 💬
    category: information
    tags: [discord, social, list, information]
---

## Instructions

This skill allows the nanobot to list the Discord servers the user is a member of. The output will be a formatted list containing the server name and the number of members in each server.

**Process:**

1.  **Authenticate:** The nanobot must first authenticate with the user's Discord account. This assumes a pre-existing authentication mechanism is in place.
2.  **Retrieve Guilds:**  Using the authenticated Discord API, retrieve a list of all guilds (servers) the user is a member of.
3.  **Format Output:**  Iterate through the list of guilds and format each entry as follows:
    *   `Server Name: [Server Name]`
    *   `Member Count: [Member Count]`
    *   Separate each server entry with a horizontal rule (`---`).
4.  **Present Results:**  Present the formatted list to the user.  If the user is not a member of any servers, inform them of this. If an error occurs during API retrieval, inform the user of the error.

**Example Output (if the user is in 3 servers):**

```
Server Name: General Discussion
Member Count: 542

---
Server Name: Coding Help
Member Count: 1234

---
Server Name: Gaming Community
Member Count: 87
```

**Error Handling:**

*   **Authentication Failure:** If the nanobot cannot authenticate with the user's Discord account, respond with "Authentication failed. Please ensure you are properly authenticated."
*   **API Error:** If there is an error retrieving the guild list from the Discord API, respond with "An error occurred while retrieving server information. Please try again later."
*   **No Servers:** If the user is not a member of any Discord servers, respond with "You are not a member of any Discord servers."
```