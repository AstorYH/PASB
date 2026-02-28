```skill
---
name: sso-link
description: Generates a single sign-on (SSO) link for a given service and user.
metadata:
  nanobot:
    emoji: 🔗
    category: authentication
    tags: [security, login, link]
---

## Skill Instructions

This skill generates a Single Sign-On (SSO) link.  The link will be constructed based on the provided service identifier and user identifier.  The exact format of the SSO link will depend on the service, and this skill assumes a standard format.

**Input:**

*   `service`: (string) The identifier of the service to generate the SSO link for (e.g., "google", "microsoft", "salesforce").
*   `user`: (string) The identifier of the user for whom the SSO link is being generated (e.g., email address, username).

**Output:**

*   `link`: (string) The generated SSO link.  If the service is not recognized, the output will be an error message.

**Logic:**

1.  **Service Recognition:** Check the `service` input against a predefined list of supported services.
2.  **Link Generation:** Based on the recognized `service`, construct the SSO link using a predefined template.  The template will include the `user` input.
3.  **Error Handling:** If the `service` is not recognized, return an error message indicating that the service is not supported.

**Supported Services and Link Templates (Example):**

*   `google`: `https://accounts.google.com/ServiceLogin?oemid=XXXXXXXX&hl=en&continue=https://mail.google.com` (Replace XXXXXXXX with a placeholder or a dynamic value if possible)
*   `microsoft`: `https://login.microsoftonline.com/XXXXXXXX/oauth2/authorize?client_id=YYYYYYYY&response_type=code&redirect_uri=ZZZZZZZZ&scope=openid` (Replace XXXXXXXX, YYYYYYYY, and ZZZZZZZ with placeholders or dynamic values)
*   `salesforce`: `https://login.salesforce.com/apex/login?un=${user}&so=005XXXXXXXXXXXXXXX` (Replace XXXXXXXX with a placeholder or dynamic value)

**Note:**  The actual SSO link format is highly service-specific and may require additional parameters. This skill provides a simplified example.  The placeholders should be replaced with appropriate values based on the specific service's SSO implementation.  Dynamic value generation is beyond the scope of this skill, but could be added in a future iteration.
```