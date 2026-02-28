```skill
---
name: dns-record-lookup
description: Queries a DNS server to retrieve the IP address associated with a given domain name.
metadata:
  nanobot:
    emoji: 🌐
    category: network
    tags: [dns, network, lookup, domain]
---

## Skill: dns-record-lookup

This skill allows you to look up the IP address associated with a domain name using DNS resolution.

**Instructions:**

1.  **Input:** You will receive a domain name as input (e.g., "example.com").
2.  **DNS Query:** Initiate a DNS query for the provided domain name.  Specifically, request an "A" record, which maps a hostname to an IPv4 address.
3.  **Response Handling:**
    *   **Success:** If the DNS query is successful and returns an IP address, report the IP address.
    *   **Failure:** If the DNS query fails (e.g., domain not found, server unreachable), report "DNS lookup failed."
4.  **Output:**  Provide the IP address found, or the error message "DNS lookup failed." if no IP address is found.

**Example:**

*   **Input:** `google.com`
*   **Output:** `142.250.185.142` (or a similar valid IP address for google.com)

*   **Input:** `nonexistentdomain.invalid`
*   **Output:** `DNS lookup failed.`
```