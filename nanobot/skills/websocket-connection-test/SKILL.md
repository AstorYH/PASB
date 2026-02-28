```skill
---
name: websocket-connection-test
description: Verifies a connection to a specified WebSocket endpoint.
metadata:
  nanobot:
    emoji: 📡
    category: network
    tags: [network, websocket, connection, test]
---

## Websocket Connection Test

This skill attempts to establish a WebSocket connection to a given endpoint and reports the result.

**Instructions:**

1.  **Endpoint:** You will be provided with a WebSocket endpoint URL. This is the address you will attempt to connect to.
2.  **Connection Attempt:** Initiate a WebSocket connection to the provided endpoint.
3.  **Success/Failure:**
    *   If the connection is successfully established (even briefly), report "Success: WebSocket connection established.".
    *   If the connection fails (e.g., due to network errors, invalid URL, server unavailability), report "Failure: Could not establish WebSocket connection.".  Include any error messages received during the connection attempt in the report.
4.  **Timeout:** Implement a timeout mechanism (e.g., 5 seconds) to prevent indefinite waiting if the connection cannot be established. If the timeout is reached, report "Failure: Connection timeout.".
5.  **No Data Transmission:** This skill only tests the connection itself; do *not* attempt to send or receive any data. The goal is solely to verify the ability to connect.

**Example Input:**

`ws://echo.websocket.org`

**Expected Output (Success):**

`Success: WebSocket connection established.`

**Expected Output (Failure - Invalid URL):**

`Failure: Could not establish WebSocket connection. Error: Invalid URL format.`

**Expected Output (Failure - Timeout):**

`Failure: Connection timeout.`
```