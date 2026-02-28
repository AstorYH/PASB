```skill
---
name: permission-group-audit
description: Scans and reports on the current permissions assigned to all user groups within the system.
metadata:
  nanobot:
    emoji: 🛡️
    category: security
    tags: [audit, permissions, security, groups, users]
---

## Permission Group Audit

This skill performs a comprehensive audit of all permission groups within the system, identifying assigned permissions for each group. The output will be a detailed report suitable for security review and compliance checks.

**Instructions:**

1.  **Identify User Groups:** Begin by querying the system's user management module to retrieve a list of all defined user groups.  This should include the group name and a unique identifier for each group.
2.  **Retrieve Permissions:** For each user group identified in step 1, query the system's permission management module to retrieve the list of permissions currently assigned to that group.  This should include the permission name and a description of what the permission allows.
3.  **Generate Report:** Compile the information gathered in steps 1 and 2 into a structured report. The report should include:
    *   Group Name
    *   Group ID
    *   List of Assigned Permissions (Name and Description)
4.  **Output Report:** Present the generated report in a human-readable format (e.g., a formatted text file, a table).  Prioritize clarity and ease of understanding.  Consider sorting the report by group name for easier navigation.
5.  **Error Handling:** If any errors occur during the process (e.g., inability to access user group information, permission data unavailable), log the error and continue processing other groups if possible.  Report any unrecoverable errors at the end of the audit.

**Example Output (Text Format):**

```
--- Permission Group Audit Report ---

Group Name: Administrators
Group ID: 1
Permissions:
  - Name: System.Administer
    Description: Allows full administrative control over the system.
  - Name: User.Manage
    Description: Allows management of user accounts.

Group Name: Editors
Group ID: 2
Permissions:
  - Name: Content.Create
    Description: Allows creation of new content.
  - Name: Content.Edit
    Description: Allows editing of existing content.

Group Name: Viewers
Group ID: 3
Permissions:
  - Name: Content.Read
    Description: Allows viewing of content.
```

**Notes:**

*   The specific modules and APIs used to access user group and permission information will depend on the system architecture.
*   Consider adding a timestamp to the report to indicate when the audit was performed.
*   This skill assumes the nanobot has the necessary permissions to access user group and permission data.
```