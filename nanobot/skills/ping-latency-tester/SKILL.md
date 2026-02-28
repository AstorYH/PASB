```skill
---
name: ping-latency-tester
description: Measures the round-trip time (latency) to a specified network address.
metadata:
  nanobot:
    emoji: 📡
    category: network
    tags: [network, latency, ping, diagnostics]
---

## Instructions

This skill allows you to measure the latency to a given network address.  It simulates a "ping" operation.

**Input:**

*   `target_address` (string): The IP address or hostname to ping.  Example: "8.8.8.8" or "google.com".

**Process:**

1.  Attempt to establish a connection to the `target_address`.
2.  Send a small data packet to the `target_address`.
3.  Measure the time elapsed between sending the packet and receiving a response. This is the round-trip time (RTT).
4.  If no response is received within a reasonable timeout (e.g., 3 seconds), report a timeout error.

**Output:**

*   `latency` (float): The round-trip time in milliseconds (ms).  Report `null` if a timeout occurs.
*   `success` (boolean): `true` if the ping was successful, `false` if a timeout occurred.

**Error Handling:**

*   If the `target_address` is invalid (e.g., malformed IP address or non-existent hostname), report an "Invalid Address" error.
*   If a network error occurs during the connection attempt or data transmission, report a "Network Error" error.
*   If no response is received within the timeout period, report a "Timeout" error.

**Example:**

```
Input: target_address = "8.8.8.8"

Process:
1. Establish connection to 8.8.8.8
2. Send packet
3. Receive response after 25ms

Output:
latency: 25.0
success: true
```

```
Input: target_address = "nonexistent.example.com"

Process:
1. Attempt to connect to nonexistent.example.com - fails after timeout
2. Report timeout

Output:
latency: null
success: false
```
```
Input: target_address = "invalid_ip_address"

Output:
error: "Invalid Address"
```