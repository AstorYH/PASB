```skill
---
name: auth0-role-assignment
description: Assigns a user to a specific role within an Auth0 organization.
metadata:
  nanobot:
    emoji: 🛂
    category: security
    tags: [auth0, roles, authorization, identity]
  dependencies: []
---

## Auth0 Role Assignment

This skill allows the nanobot to assign a user to a specific role within an Auth0 organization.  You will need to provide the user's email address and the name of the role to assign.

**Instructions:**

1.  **Identify User:** Determine the email address of the user you wish to modify.
2.  **Identify Role:** Determine the exact name of the Auth0 role you want to assign.  Role names are case-sensitive.
3.  **Execute Assignment:**  The nanobot will attempt to assign the specified role to the specified user in Auth0.
4.  **Confirmation:** The nanobot will report success or failure, including any error messages received from the Auth0 API.

**Input Parameters:**

*   `email`: (string, required) The email address of the user to be assigned the role.
*   `role_name`: (string, required) The name of the Auth0 role to assign.

**Example:**

To assign the role "administrator" to the user with the email address "user@example.com", the command would be:

```
auth0-role-assignment email=user@example.com role_name=administrator
```

**Error Handling:**

*   **Invalid Email:** If the provided email address is not a valid email format, the nanobot will return an error.
*   **Role Not Found:** If the specified role name does not exist in the Auth0 organization, the nanobot will return an error.
*   **User Not Found:** If the specified user does not exist in Auth0, the nanobot will return an error.
*   **API Errors:** Any errors returned by the Auth0 API will be propagated to the user.
*   **Insufficient Permissions:** If the nanobot does not have sufficient permissions to modify user roles in Auth0, an error will be returned.
```