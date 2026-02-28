```skill
---
name: webex-space-creation
description: Creates a new Webex Space with the specified name and members.
metadata:
  nanobot:
    emoji: 🏢
    category: communication
    tags: [webex, space, collaboration]
  dependencies: []
---

## Webex Space Creation Skill

This skill allows the nanobot to create a new Webex Space.

**Instructions:**

1.  **Receive Input:** The nanobot will receive a request to create a Webex Space. This request will include the following information:
    *   `space_name`: (String, Required) The name of the new Webex Space.
    *   `members`: (List of Strings, Optional) A list of user IDs or email addresses to add as members to the space. If not provided, the space will be created with only the creator as a member.

2.  **Validate Input:**
    *   Ensure `space_name` is a non-empty string.
    *   If `members` is provided, ensure it is a list of valid user IDs or email addresses.  (Note: Actual validation of user IDs/emails is beyond the scope of this skill; assume they are valid for the purpose of this exercise).

3.  **Create Webex Space:** Using the Webex API (assumed to be available), create a new Webex Space with the provided `space_name`.

4.  **Add Members (if provided):** If the `members` list was provided, iterate through the list and add each member to the newly created Webex Space.

5.  **Return Result:**  Return a success message including the name of the created space and a list of members (if any were added).  If the space creation fails, return an error message indicating the failure and the reason (e.g., invalid space name, API error).

**Example Input:**

```json
{
  "space_name": "Project Phoenix",
  "members": ["user123", "john.doe@example.com", "jane.smith@example.com"]
}
```

**Example Output (Success):**

```json
{
  "status": "success",
  "message": "Webex Space 'Project Phoenix' created successfully.",
  "members": ["user123", "john.doe@example.com", "jane.smith@example.com"]
}
```

**Example Output (Failure - Invalid Space Name):**

```json
{
  "status": "error",
  "message": "Failed to create Webex Space. Space name cannot be empty."
}
```

**Error Handling:**

*   Handle potential API errors (e.g., network issues, authentication failures).
*   Provide informative error messages to the user.
```