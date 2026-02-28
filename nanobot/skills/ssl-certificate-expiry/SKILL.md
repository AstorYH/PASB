```skill
---
name: ssl-certificate-expiry
description: Checks the expiration date of an SSL certificate and reports its status.
metadata:
  nanobot:
    emoji: 🔒
    category: security
    tags: [ssl, certificate, expiry, security, monitoring]
---

## Skill: SSL Certificate Expiry

This skill checks the expiration date of an SSL certificate for a given domain and reports whether it's nearing expiration or has already expired.

**Instructions:**

1.  **Input:** The skill requires a single input parameter: `domain`. This should be a valid domain name (e.g., "example.com").
2.  **Certificate Retrieval:** The nanobot will attempt to retrieve the SSL certificate associated with the provided `domain`. This involves querying DNS records and establishing a secure connection to the domain.
3.  **Expiration Date Extraction:** Once the certificate is retrieved, the nanobot will extract the "Not After" date, which represents the certificate's expiration date.
4.  **Date Comparison:** The nanobot will compare the expiration date with the current date.
5.  **Status Reporting:** Based on the comparison, the nanobot will report one of the following statuses:
    *   **"Valid":** The certificate is currently valid (not expired and not within the warning period).
    *   **"Warning":** The certificate is nearing expiration (within a configurable warning period, default 30 days).
    *   **"Expired":** The certificate has already expired.
6.  **Output:** The skill will output a string representing the certificate's status.

**Example:**

*   **Input:** `domain = example.com`
*   **Possible Outputs:**
    *   `Valid`
    *   `Warning`
    *   `Expired`

**Error Handling:**

*   If the domain is invalid or unreachable, the skill will output "Error: Domain unreachable."
*   If the SSL certificate cannot be retrieved, the skill will output "Error: Certificate retrieval failed."
*   If there's an issue parsing the certificate data, the skill will output "Error: Certificate parsing error."
```