```skill
---
name: bash-script-executor
description: Executes a provided Bash script within a sandboxed environment.
metadata:
  nanobot:
    emoji: 💻
    version: 1.0
    category: execution
    tags: [scripting, bash, execution, sandbox]
---

## Skill: Bash Script Executor

This skill allows the nanobot to execute a provided Bash script within a secure, sandboxed environment.  The script will be executed with limited permissions to prevent malicious code from harming the system.

**Input:**

*   `script`: (string, required) The Bash script to execute.  This should be a complete, valid Bash script.
*   `timeout`: (integer, optional, default: 60) The maximum execution time in seconds.  If the script exceeds this time, it will be terminated.
*   `capture_output`: (boolean, optional, default: true) Whether to capture the standard output and standard error of the script.

**Output:**

*   `result`: (string) The standard output of the script if `capture_output` is true and the script executes successfully.  If `capture_output` is false, this will be an empty string.
*   `error`: (string) The standard error of the script if `capture_output` is true and the script encounters an error.  If `capture_output` is false, this will be an empty string.
*   `return_code`: (integer) The return code of the script.  A return code of 0 indicates success.
*   `execution_time`: (float) The time taken to execute the script in seconds.

**Instructions:**

1.  **Sandbox Creation:** Create a temporary, isolated directory to serve as the execution sandbox.  This directory should have restricted permissions to prevent the script from accessing sensitive system files.
2.  **Script Storage:** Write the provided `script` to a temporary file within the sandbox directory.
3.  **Execution:** Execute the Bash script within the sandbox using the `bash` interpreter.  Set a timeout using the `timeout` command to prevent runaway scripts.
4.  **Output Capture:** If `capture_output` is true, capture the standard output and standard error of the script.
5.  **Return Code:** Obtain the return code of the script.
6.  **Execution Time:** Measure the total execution time.
7.  **Cleanup:** Delete the sandbox directory and all its contents.
8.  **Result Formatting:** Format the output as specified above, including the `result`, `error`, `return_code`, and `execution_time`.

**Error Handling:**

*   If the `script` input is missing, return an error indicating that the script is required.
*   If the `timeout` input is invalid (e.g., negative or non-integer), return an error.
*   If the script execution fails (e.g., due to syntax errors or permission issues), capture the error message and return it in the `error` field.
*   If the script exceeds the `timeout`, terminate the script and return an error indicating a timeout.

**Security Considerations:**

*   The sandbox environment is crucial for preventing malicious scripts from harming the system.
*   Limit the permissions of the sandbox to the bare minimum required for script execution.
*   Sanitize the `script` input to prevent command injection vulnerabilities.  (While this skill doesn't explicitly sanitize, it's a critical consideration for any real-world implementation).
*   The `timeout` parameter is essential for preventing denial-of-service attacks.
```