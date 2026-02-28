```skill
---
name: python-script-trigger
description: Executes a user-defined Python script within a sandboxed environment.
metadata:
  nanobot:
    emoji: 🐍
    category: execution
    tags: [scripting, python, automation]
  risk: medium # Potential for code execution vulnerabilities
---

## Python Script Trigger

This skill allows the nanobot to execute a Python script provided as input.  The script will be run within a sandboxed environment to mitigate potential security risks.

**Input:**

*   `script_content` (string): The Python code to execute.  This *must* be a complete, valid Python script.
*   `script_name` (string, optional): A descriptive name for the script (e.g., "data_processor.py").  Used for logging and debugging. Defaults to "unnamed_script.py".
*   `timeout` (integer, optional):  Maximum execution time in seconds. Defaults to 60 seconds.  If the script exceeds this time, it will be terminated.

**Output:**

*   `stdout` (string): The standard output of the executed script.
*   `stderr` (string): The standard error of the executed script.
*   `return_code` (integer): The return code of the executed script (0 for success, non-zero for failure).
*   `execution_time` (float): The time taken to execute the script, in seconds.

**Instructions:**

1.  **Sandboxing:** The provided `script_content` will be written to a temporary file (e.g., `/tmp/unnamed_script.py`).  This file will then be executed using a secure, sandboxed Python interpreter.  The sandbox will restrict access to the file system, network, and other sensitive resources.
2.  **Execution:** The script will be executed with the following command: `python /tmp/unnamed_script.py`.  The `script_name` will be used for logging purposes.
3.  **Timeout:**  A timeout mechanism will be implemented to terminate the script if it exceeds the specified `timeout` value.
4.  **Capture Output:**  The standard output (`stdout`) and standard error (`stderr`) streams of the script will be captured.
5.  **Return Code:** The return code of the script will be captured.
6.  **Report Results:** The `stdout`, `stderr`, `return_code`, and `execution_time` will be returned to the caller.

**Security Considerations:**

*   **Sandboxing is crucial:**  The sandboxed environment *must* be properly configured to prevent the script from accessing sensitive resources or causing harm to the system.
*   **Input Validation:**  While the script is sandboxed, it's still good practice to validate the `script_content` to prevent malicious input (e.g., excessively long scripts, scripts containing potentially harmful commands).
*   **Resource Limits:**  Consider imposing resource limits (e.g., memory usage, CPU time) on the sandboxed environment to prevent denial-of-service attacks.
*   **Avoid External Dependencies:**  The sandboxed environment should ideally have a minimal set of dependencies to reduce the attack surface.  If external dependencies are required, they should be carefully vetted and secured.

**Example:**

```
Input:
{
  "script_content": "print('Hello from Python!')\nimport sys\nsys.exit(1)",
  "script_name": "hello_world.py",
  "timeout": 10
}

Output:
{
  "stdout": "Hello from Python!\n",
  "stderr": "",
  "return_code": 1,
  "execution_time": 0.01
}
```
```