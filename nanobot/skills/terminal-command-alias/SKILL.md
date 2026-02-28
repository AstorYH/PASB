```skill
---
name: terminal-command-alias
description: Creates a temporary alias for a terminal command.
metadata:
  nanobot:
    emoji: 🐚
    category: utility
    tags: [terminal, command, alias, shortcut]
---

## Terminal Command Alias

This skill allows you to create a temporary alias for a terminal command, making it easier to execute frequently used commands or complex command sequences. The alias will only exist for the duration of the current session.

**Instructions:**

1.  **Receive Input:** The skill expects a single input string containing the alias and the command to be aliased, separated by an equals sign (`=`). For example: `alias_name=command_to_execute`.
2.  **Parse Input:** Extract the alias name (the part before the `=`) and the command to execute (the part after the `=`).
3.  **Construct Alias Command:** Create a shell command that defines the alias. This will be in the form `alias alias_name='command_to_execute'`.
4.  **Execute Alias Command:** Execute the constructed alias command in the current shell environment. This will create the alias.
5.  **Confirmation:** Report success to the user, confirming the alias has been created and providing the alias name.  For example: "Alias 'alias_name' created for 'command_to_execute'."
6.  **Session-Specific:**  The alias is temporary and will be lost when the current terminal session ends.  Do not attempt to persist the alias.

**Example:**

*   **Input:** `ll=ls -l`
*   **Action:** The skill creates the alias `ll` that executes `ls -l`.
*   **Output:** "Alias 'll' created for 'ls -l'."

**Error Handling:**

*   If the input is not in the expected format (e.g., missing `=` or empty alias name), report an error: "Invalid input format. Please use 'alias_name=command_to_execute'."
*   If the command execution fails (e.g., due to syntax errors in the command), report an error: "Error creating alias: [error message]."
```