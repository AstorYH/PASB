```skill
---
name: powershell-logic-runner
description: Executes a provided PowerShell script and returns the output.
metadata:
  nanobot:
    emoji: 💻
    category: execution
    tags: [powershell, script, execution, logic]
---

## PowerShell Logic Runner

This skill allows the nanobot to execute a PowerShell script and return the results.  Use this to perform complex logic, data manipulation, or system interactions that are best handled by PowerShell.

**Input:**

*   `script`: (string, required) The PowerShell script to execute.  This should be a complete, valid PowerShell script.
*   `arguments`: (string, optional) Arguments to pass to the PowerShell script.  These will be appended to the end of the script.

**Output:**

*   `output`: (string) The standard output of the executed PowerShell script.  This will include any error messages generated during execution.
*   `error`: (string, optional)  If an error occurred during execution, this field will contain the error message.

**Instructions:**

1.  **Receive Input:** The nanobot will receive the `script` and optional `arguments` as input.
2.  **Construct Command:** Combine the `script` and `arguments` into a single string representing the complete PowerShell command.
3.  **Execute PowerShell:** Execute the PowerShell command using the `powershell.exe` interpreter.  Capture both standard output and standard error.
4.  **Parse Output:**
    *   If the execution was successful (no errors), set the `output` field to the standard output. Set `error` to null.
    *   If an error occurred, set the `error` field to the standard error. Set `output` to null.
5.  **Return Results:** Return the `output` and `error` fields to the caller.

**Example:**

**Input:**

```json
{
  "script": "Get-Process | Where-Object {$_.CPU -gt 10} | Select-Object Name, CPU",
  "arguments": ""
}
```

**Possible Output:**

```json
{
  "output": "Name          CPU\n----          ---\nchrome        15.2\nnotepad       12.5",
  "error": null
}
```

**Error Handling:**

*   If the `script` is missing, return an error indicating that the script is required.
*   If the PowerShell execution fails for any reason, capture the error message and return it in the `error` field.
*   Ensure the script is properly escaped to prevent injection vulnerabilities.  (This is a critical security consideration.)
```