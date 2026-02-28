```skill
---
name: okta-user-provisioning
description: Automatically creates, updates, or deactivates users in Okta based on a provided data structure.
metadata:
  nanobot:
    emoji: 🧑‍💻
    category: integration
    tags: [okta, user management, provisioning, identity]
---

## Okta User Provisioning Skill

This skill allows the nanobot to manage users within an Okta organization. It can create new users, update existing user attributes, or deactivate users.  The skill expects a structured data input representing the user information to be processed.

**Input Data Structure (JSON):**

The input should be a JSON object with the following keys.  All keys are optional, but providing more information allows for more precise provisioning.

*   `operation`: (String, Required)  Specifies the action to perform.  Valid values are: `"create"`, `"update"`, `"deactivate"`.
*   `userId`: (String, Required if `operation` is "create" or "update") The Okta user ID.  For "create", this will be used to generate a unique ID if not provided.
*   `firstName`: (String, Optional) The user's first name.
*   `lastName`: (String, Optional) The user's last name.
*   `email`: (String, Optional) The user's email address.
*   `profile`: (Object, Optional) A nested object containing additional profile attributes.  Keys within this object should correspond to Okta profile attribute names.  Example: `{"department": "Engineering", "title": "Software Engineer"}`.
*   `groups`: (Array of Strings, Optional) An array of Okta group IDs to assign the user to.
*   `status`: (String, Optional, only valid for "update") The desired status of the user. Valid values are `"ACTIVE"`, `"INACTIVE"`. If not provided during an update, the status will remain unchanged.

**Example Input (Create):**

```json
{
  "operation": "create",
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "profile": {
    "department": "Sales",
    "title": "Account Manager"
  },
  "groups": ["Sales Team", "All Employees"]
}
```

**Example Input (Update):**

```json
{
  "operation": "update",
  "userId": "abcdef123456",
  "firstName": "Jonathan",
  "email": "jonathan.doe@example.com",
  "profile": {
    "title": "Senior Account Manager"
  },
  "status": "ACTIVE"
}
```

**Example Input (Deactivate):**

```json
{
  "operation": "deactivate",
  "userId": "abcdef123456"
}
```

**Instructions for the Agent:**

1.  **Parse Input:**  Extract the `operation`, `userId`, and other relevant attributes from the JSON input.
2.  **Validate Input:**
    *   Ensure `operation` is one of `"create"`, `"update"`, or `"deactivate"`.
    *   If `operation` is `"create"` or `"update"`, ensure `userId` is provided or can be generated.
3.  **Okta API Interaction:**  Use the Okta API to perform the requested operation.  You will need to have appropriate Okta API credentials configured (e.g., API token or OAuth client).  The specific API endpoints to use are:
    *   **Create:** `/api/v1/users` (POST)
    *   **Update:** `/api/v1/users/{userId}` (PATCH)
    *   **Deactivate:** `/api/v1/users/{userId}` (DELETE)
4.  **Error Handling:**  If the Okta API call fails, report the error to the user, including the HTTP status code and error message.
5.  **Success Reporting:**  Upon successful completion of the operation, report the success to the user, including the Okta user ID.
6.  **Id Generation (Create):** If a `userId` is not provided during a "create" operation, generate a unique ID (e.g., a UUID).

**Important Considerations:**

*   **Okta API Credentials:** This skill requires access to an Okta organization with appropriate API permissions.  The nanobot must be configured with the necessary credentials.
*   **Attribute Mapping:** Ensure that the attributes in the input JSON map correctly to the corresponding Okta profile attributes.
*   **Rate Limiting:** Be mindful of Okta API rate limits and implement appropriate retry logic.
*   **Security:**  Handle Okta API credentials securely.  Do not hardcode them in the skill definition.
*   **Error Logging:** Implement robust error logging to facilitate debugging and troubleshooting.