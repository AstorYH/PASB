```skill
---
name: payload-schema-validator
description: Validates an incoming payload against a provided JSON schema.
metadata:
  nanobot:
    emoji: 🧪
    category: data-processing
    tags: [validation, schema, json]
  dependencies: []
---

## Skill: Payload Schema Validator

This skill validates an incoming payload against a provided JSON schema.  It's useful for ensuring data integrity and consistency before further processing.

### Input

The skill expects a single input parameter: `schema`. This parameter must be a string containing a valid JSON schema.

### Processing

1.  **Receive Schema:** The skill receives the `schema` string.
2.  **Parse Schema:** The skill parses the `schema` string into a JSON schema object.  If parsing fails, the skill immediately returns an error.
3.  **Receive Payload:** The skill receives the payload to be validated.
4.  **Validate Payload:** The skill validates the payload against the parsed JSON schema.
5.  **Return Result:** The skill returns a boolean value: `true` if the payload is valid according to the schema, and `false` otherwise.  If an error occurs during validation (e.g., invalid schema, unexpected data type), the skill returns an error.

### Output

The skill returns a single output parameter: `valid`. This parameter is a boolean value indicating whether the payload is valid according to the schema.

### Error Handling

*   **Invalid Schema:** If the provided `schema` string is not a valid JSON schema, the skill returns an error with the message "Invalid JSON schema".
*   **Validation Error:** If the payload does not conform to the schema, the skill returns an error with the message "Payload validation failed".
*   **Internal Error:** Any other unexpected errors during processing will result in a generic error message.

### Example

**Input:**

```json
{
  "schema": "{ \"type\": \"object\", \"properties\": { \"name\": { \"type\": \"string\" }, \"age\": { \"type\": \"integer\", \"minimum\": 0 } }, \"required\": [\"name\", \"age\"] }"
}
```

**Payload:**

```json
{
  "name": "Alice",
  "age": 30
}
```

**Output:**

```json
{
  "valid": true
}
```

**Input:**

```json
{
  "schema": "{ \"type\": \"object\", \"properties\": { \"name\": { \"type\": \"string\" }, \"age\": { \"type\": \"integer\", \"minimum\": 0 } }, \"required\": [\"name\", \"age\"] }"
}
```

**Payload:**

```json
{
  "name": "Bob"
}
```

**Output:**

```json
{
  "valid": false
}
```
```