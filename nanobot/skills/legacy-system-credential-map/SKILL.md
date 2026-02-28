```skill
---
name: legacy-system-credential-map
description: Creates a map of legacy system names to their corresponding credentials, based on available data.
metadata:
  nanobot:
    emoji: 🗝️
    category: data-management
    tags: [credentials, legacy, mapping, security]
---

## Legacy System Credential Map

This skill constructs a map associating legacy system names with their credentials. The agent will analyze available data sources (e.g., configuration files, documentation, memory dumps) to identify legacy systems and their associated credentials.  The output will be a structured map suitable for secure storage and retrieval.

**Instructions:**

1.  **Identify Potential Legacy Systems:** Scan all available data sources for mentions of systems identified as "legacy" or exhibiting characteristics of older technology (e.g., outdated protocols, specific software versions). Prioritize systems marked as such in existing documentation.
2.  **Credential Extraction:** For each identified legacy system, attempt to extract credentials. This may involve:
    *   Searching configuration files (e.g., `.ini`, `.xml`, `.conf`) for keywords like "password", "username", "credentials", "key".
    *   Analyzing documentation for explicit credential information.
    *   Examining memory dumps for potential credential storage (exercise extreme caution and prioritize data integrity).
    *   Looking for environment variables that might contain credentials.
3.  **Credential Type Identification:** Attempt to determine the type of credential (e.g., username/password, API key, SSH key). This information should be included in the map.
4.  **Map Construction:** Create a map (dictionary) with the following structure:

    ```
    {
      "legacy_system_name_1": {
        "username": "user1",
        "password": "password123",
        "credential_type": "username/password",
        "source": "config_file.ini"
      },
      "legacy_system_name_2": {
        "api_key": "abcdef123456",
        "credential_type": "API Key",
        "source": "documentation.pdf"
      },
      ...
    }
    ```

    *   `legacy_system_name`: The name of the legacy system.
    *   `username`: The username associated with the system (if applicable).
    *   `password`: The password associated with the system (if applicable).
    *   `api_key`: The API key associated with the system (if applicable).
    *   `ssh_key`: The SSH key associated with the system (if applicable).
    *   `credential_type`: A string describing the type of credential.
    *   `source`: The data source where the credential was found.

5.  **Output:** Return the constructed map.  Ensure the map is securely formatted and protected from unauthorized access.  If no credentials are found for a legacy system, omit it from the map.  If multiple credentials are found for a single system, prioritize the most recent or most reliable source.

**Security Considerations:**

*   Handle credentials with extreme care.  Do not log or store credentials in plain text.
*   Prioritize data integrity and prevent accidental modification or deletion of credentials.
*   Implement access controls to restrict access to the credential map.
*   If a credential appears to be obfuscated or encrypted, flag it for further investigation rather than attempting to decrypt it without proper authorization.
*   If a system is identified as having no credentials, record this fact in the map with a "no_credentials" flag.
```