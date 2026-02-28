```skill
---
name: directory-service-search
description: Searches a directory service for information based on a given query.
metadata:
  nanobot:
    emoji: 🔍
    category: information-retrieval
    tags: [search, directory, information, query]
---

## Skill: Directory Service Search

This skill allows the nanobot to query a directory service (e.g., LDAP, Active Directory, a custom database) to retrieve information based on a provided search query.  The directory service is assumed to be accessible and configured.

**Instructions:**

1.  **Receive Query:** The skill receives a query string and optionally, a search scope (e.g., "base", "subtree", "whole"). If no scope is provided, default to "subtree".
2.  **Determine Directory Service:**  The nanobot must know which directory service to query. This information should be pre-configured (e.g., stored in a configuration file or environment variable).  Assume the directory service is accessible via a standard protocol (LDAP, etc.).
3.  **Construct Search Request:** Based on the query string and scope, construct a search request appropriate for the directory service. This may involve translating the query string into a specific query language (e.g., LDAP filter).
4.  **Execute Search:** Execute the search request against the directory service.
5.  **Process Results:** Parse the results returned by the directory service.
6.  **Format Output:** Format the results into a human-readable format.  Prioritize presenting key information (e.g., name, email, phone number) clearly. If no results are found, report "No results found."
7.  **Return Results:** Return the formatted results to the user.

**Example Queries:**

*   `"Find John Smith"`
*   `"Find all users in the Sales department"`
*   `"Find the email address for jane.doe@example.com"`
*   `"Find all computers with the name 'Server1' scope:whole"`

**Error Handling:**

*   If the directory service is unavailable, return "Directory service unavailable."
*   If the query is invalid, return "Invalid query."
*   If an error occurs during the search, return "Search failed: [error message]."
```