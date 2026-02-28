```skill
---
name: jwt-parse
description: Parses a JSON Web Token (JWT) and extracts its header, payload, and signature.
metadata:
  nanobot:
    emoji: 🔑
    category: security
    tags: [jwt, token, security, parsing]
---

## Skill: jwt-parse

This skill parses a JSON Web Token (JWT) and returns its components.  It assumes the JWT is a properly formatted string.

**Input:**

*   `jwt_string`: (string) The JWT string to parse.

**Output:**

*   `header`: (string) The Base64URL encoded JWT header.
*   `payload`: (string) The Base64URL encoded JWT payload.
*   `signature`: (string) The JWT signature.
*   `is_valid`: (boolean) True if the JWT appears to be structurally valid (header, payload, and signature present), false otherwise.  **Note:** This skill does *not* verify the signature's authenticity or the claims within the payload. It only checks for structural validity.

**Instructions:**

1.  **Input Validation:** Check if the `jwt_string` input is a string. If not, return `is_valid: false` and empty strings for header, payload, and signature.
2.  **Splitting the Token:** Split the `jwt_string` into three parts based on the "." delimiter.  If the string does not contain exactly two ".", return `is_valid: false` and empty strings for header, payload, and signature.
3.  **Assigning Parts:** Assign the three parts to the variables `header_encoded`, `payload_encoded`, and `signature`.
4.  **Structural Validity Check:** Check if all three variables (`header_encoded`, `payload_encoded`, `signature`) are non-empty strings. If any are empty, set `is_valid: false` and return.
5.  **Output:** Set `header` to `header_encoded`, `payload` to `payload_encoded`, and `signature` to `signature`. Set `is_valid` to `true`.
6.  **Return:** Return the `header`, `payload`, `signature`, and `is_valid` values.

**Example:**

**Input:**

```json
{
  "jwt_string": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaXN0cmluZyIsImV4cCI6MTY4OTc3MzQ0MH0.some_signature"
}
```

**Output:**

```json
{
  "header": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
  "payload": "eyJzdWIiOiJkaXN0cmluZyIsImV4cCI6MTY4OTc3MzQ0MH0",
  "signature": "some_signature",
  "is_valid": true
}
```

**Error Handling:**

*   If the input is not a string, return `is_valid: false`.
*   If the JWT string is not properly formatted (doesn't contain two "."), return `is_valid: false`.
*   If any of the header, payload, or signature parts are missing, return `is_valid: false`.
```