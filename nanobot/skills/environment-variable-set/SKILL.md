```skill
---
name: environment-variable-set
description: Sets a specified environment variable to a given value.
metadata:
  nanobot:
    emoji: ⚙️
    category: system
    tags:
      - environment
      - configuration
      - system
  dependencies: []
---

## Instructions

This skill allows you to set environment variables.  Environment variables are key-value pairs that provide configuration information to running processes.  This skill modifies the environment of the nanobot itself.

**Input:**

The input to this skill is a JSON object with the following structure:

```json
{
  "variable_name": "string",
  "variable_value": "string"
}
```

*   `variable_name`: The name of the environment variable to set.  This *must* be a string.
*   `variable_value`: The value to assign to the environment variable. This *must* be a string.

**Process:**

1.  Parse the input JSON object.
2.  Extract the `variable_name` and `variable_value` from the parsed JSON.
3.  Set the environment variable with the specified name to the specified value.  This will affect subsequent skill executions and any internal processes the nanobot uses.
4.  Confirm the setting of the environment variable.

**Output:**

The output of this skill is a simple confirmation message:

```json
{
  "status": "success",
  "message": "Environment variable '{variable_name}' set to '{variable_value}'."
}
```

**Error Handling:**

*   If the input is not valid JSON, return an error:

    ```json
    {
      "status": "error",
      "message": "Invalid JSON input."
    }
    ```

*   If `variable_name` or `variable_value` are missing from the JSON, return an error:

    ```json
    {
      "status": "error",
      "message": "Missing 'variable_name' or 'variable_value' in input."
    }
    ```

*   If `variable_name` or `variable_value` are not strings, return an error:

    ```json
    {
      "status": "error",
      "message": "'variable_name' and 'variable_value' must be strings."
    }
    ```

**Example:**

**Input:**

```json
{
  "variable_name": "MY_API_KEY",
  "variable_value": "abcdef123456"
}
```

**Output:**

```json
{
  "status": "success",
  "message": "Environment variable 'MY_API_KEY' set to 'abcdef123456'."
}
```
```