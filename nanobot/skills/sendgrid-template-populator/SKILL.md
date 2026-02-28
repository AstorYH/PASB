```skill
---
name: sendgrid-template-populator
description: Populates a SendGrid email template with provided data.
metadata:
  nanobot:
    emoji: 📧
    category: communication
    tags: [email, sendgrid, template, data]
---

## Skill: SendGrid Template Populator

This skill allows you to populate a SendGrid email template with data provided as a dictionary.  It assumes you have already authenticated with SendGrid and have access to the template.

**Input:**

*   `template_id` (string): The ID of the SendGrid template to populate.
*   `data` (dictionary): A dictionary containing the data to populate the template.  Keys in this dictionary should correspond to the template's dynamic template variables.  Values should be strings or numbers that can be converted to strings.

**Output:**

*   `populated_html` (string): The HTML content of the populated email template.
*   `status` (string): "success" or "failure" indicating the outcome of the operation.
*   `message` (string): A descriptive message about the outcome.

**Instructions:**

1.  **Validate Input:** Ensure `template_id` is a non-empty string and `data` is a dictionary. If either is invalid, set `status` to "failure" and `message` to an appropriate error message (e.g., "Invalid template_id" or "Data must be a dictionary").
2.  **Template Population:**  Use the provided `template_id` and `data` to populate the SendGrid template.  This is a simulated operation; you do *not* need to make an external API call.  Instead, perform a string replacement operation.
    *   Iterate through the `data` dictionary.
    *   For each key-value pair in `data`, search for the key (as a string) within a placeholder format like `{{key}}` in a template string.
    *   Replace the placeholder with the corresponding value (converted to a string).
3.  **Simulate Template Content:** For the purpose of this skill, assume a simple template structure.  If `template_id` is "my_template", assume the template content is:

    ```html
    <html>
    <body>
      <h1>Hello, {{name}}!</h1>
      <p>Your order number is: {{order_number}}.</p>
      <p>Total amount: {{total_amount}}</p>
    </body>
    </html>
    ```

    If `template_id` is anything else, assume the template content is:

    ```html
    <html>
    <body>
      <p>This is a generic template.</p>
    </body>
    </html>
    ```
4.  **Return Results:**
    *   If the population was successful, set `status` to "success", `message` to "Template populated successfully", and `populated_html` to the resulting HTML string after the replacements.
    *   If any error occurred during the population process (e.g., a key in `data` was not found in the template), set `status` to "failure" and `message` to a descriptive error message (e.g., "Key 'missing_key' not found in template").  `populated_html` should be an empty string in case of failure.

**Example:**

**Input:**

```json
{
  "template_id": "my_template",
  "data": {
    "name": "Alice",
    "order_number": "12345",
    "total_amount": "100.00"
  }
}
```

**Output:**

```json
{
  "populated_html": "<html>\n<body>\n  <h1>Hello, Alice!</h1>\n  <p>Your order number is: 12345.</p>\n  <p>Total amount: 100.00</p>\n</body>\n</html>",
  "status": "success",
  "message": "Template populated successfully"
}
```

**Error Handling:**

*   Handle cases where the `template_id` is invalid.
*   Handle cases where the `data` dictionary is empty or contains invalid data types.
*   Handle cases where a key in the `data` dictionary is not found in the template.
```