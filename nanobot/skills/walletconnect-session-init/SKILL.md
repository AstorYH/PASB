```skill
---
name: walletconnect-session-init
description: Initializes a WalletConnect session with a provided URI.
metadata:
  nanobot:
    emoji: 🔗
    category: communication
    tags: [walletconnect, blockchain, session]
---

## Instructions

This skill initializes a WalletConnect session.

1.  **Receive Input:** The skill expects a single input parameter: `uri`. This parameter is a string representing the WalletConnect URI.  This URI contains all the necessary information to connect to a WalletConnect-enabled application.

2.  **Parse URI:**  Parse the provided `uri` string.  Extract the relevant information, including the chain ID, the application's address, and any other necessary parameters.  Assume the URI is well-formed and contains all required information.

3.  **Initiate Connection:** Attempt to establish a WalletConnect connection using the parsed URI. This involves creating a WalletConnect peer and attempting to connect to the specified address.

4.  **Handle Connection Status:**
    *   **Success:** If the connection is successfully established, report a success status.  The success message should indicate that the WalletConnect session has been initialized.
    *   **Failure:** If the connection fails (e.g., due to network issues, invalid URI, or the application not being available), report a failure status. The failure message should indicate that the WalletConnect session initialization failed and provide a brief explanation of the failure (if available).

5.  **Output:** The skill should output a status message indicating success or failure.  No further data needs to be returned.

**Example Input:**

```json
{
  "uri": "wc:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

**Example Success Output:**

```json
{
  "status": "success",
  "message": "WalletConnect session initialized."
}
```

**Example Failure Output:**

```json
{
  "status": "failure",
  "message": "Failed to initialize WalletConnect session.  Connection timed out."
}
```

**Error Handling:**

*   If the `uri` parameter is missing, report a failure status with a message indicating that the `uri` parameter is required.
*   If the `uri` parameter is not a string, report a failure status with a message indicating that the `uri` parameter must be a string.
*   Handle any exceptions that may occur during the connection process and report a failure status with an appropriate error message.