```skill
---
name: curl-command-generator
description: Generates a cURL command based on provided parameters.
metadata:
  nanobot:
    emoji: 💻
    version: 1.0
    category: utility
    tags: [network, http, command-line, generation]
---

## Instructions

This skill generates a cURL command string based on the parameters you provide.  You will provide a series of key-value pairs describing the desired cURL command.  The skill will then construct a valid cURL command string and output it.

**Input Parameters:**

The input should be a series of key-value pairs, each on a new line.  Valid keys are:

*   `url`: (Required) The URL to request.  Example: `https://www.example.com`
*   `method`: (Optional, default: `GET`) The HTTP method to use (e.g., `POST`, `PUT`, `DELETE`).
*   `header`: (Optional, repeatable)  HTTP header to include.  Use multiple `header:` lines for multiple headers. Example: `header: Content-Type: application/json`
*   `data`: (Optional) Data to send with the request (for POST, PUT, etc.).  Example: `data: {"key": "value"}`
*   `output`: (Optional, default: `stdout`) Where to send the output.  Options are `stdout` (print to console) or `file:<filename>` (save to a file).
*   `verbose`: (Optional, default: `false`)  Enable verbose output.  Set to `true` to enable.
*   `user`: (Optional) Username for authentication. Example: `user: myuser`
*   `password`: (Optional) Password for authentication. Example: `password: mypassword`
*   `proxy`: (Optional) Proxy server address. Example: `proxy: http://proxy.example.com:8080`

**Output:**

The skill will output a single string containing the generated cURL command.

**Examples:**

**Input:**

```
url: https://www.example.com
method: POST
header: Content-Type: application/json
data: {"key": "value"}
output: file:output.txt
verbose: true
```

**Output:**

```
curl -v -X POST --data '{"key": "value"}' -H "Content-Type: application/json" https://www.example.com > output.txt
```

**Input:**

```
url: https://api.example.com/resource
method: GET
user: myuser
password: mypassword
```

**Output:**

```
curl -u myuser:mypassword https://api.example.com/resource
```

**Error Handling:**

*   If the `url` parameter is missing, the skill will output an error message: "Error: URL is required."
*   If an invalid parameter is provided, the skill will output an error message: "Error: Invalid parameter: <parameter_name>."
*   If the `output` parameter is set to `file:<filename>` and the filename is invalid, the skill will output an error message: "Error: Invalid filename: <filename>."
```