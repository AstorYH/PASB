```skill
---
name: api-rate-limit-monitor
description: Monitors API request rates and alerts when approaching or exceeding defined limits.
metadata:
  nanobot:
    emoji: 🚦
    category: monitoring
    tags: [api, rate limiting, monitoring, alerts]
---

## Skill: API Rate Limit Monitor

This skill monitors API request rates and triggers alerts when approaching or exceeding defined rate limits. It operates by tracking request counts over time windows and comparing them against configured thresholds.

**Instructions for the Agent:**

1.  **Identify Target API Endpoint:** Determine the specific API endpoint to monitor. This will be provided as input.
2.  **Establish Baseline:** Initially, observe the API's request rate for a short period (e.g., 5 minutes) to establish a baseline. This helps account for normal fluctuations.
3.  **Define Rate Limits:**  The user will provide the following rate limits:
    *   `warning_threshold`: The number of requests allowed within a specified time window before a warning is triggered.
    *   `error_threshold`: The number of requests allowed within a specified time window before an error/critical alert is triggered.
    *   `time_window_seconds`: The duration (in seconds) over which the request rate is measured.
4.  **Track Requests:** Continuously monitor incoming requests to the target API endpoint. Increment a counter for each request received.
5.  **Periodic Evaluation:** Every `time_window_seconds`, perform the following evaluation:
    *   Calculate the request rate: `request_rate = counter / time_window_seconds`
    *   Compare the `request_rate` against the `warning_threshold` and `error_threshold`.
6.  **Alerting:**
    *   If `request_rate` exceeds `warning_threshold`, generate a "Warning: Approaching API rate limit" alert. Include the current request rate and the thresholds in the alert message.
    *   If `request_rate` exceeds `error_threshold`, generate an "Error: API rate limit exceeded" alert. Include the current request rate and the thresholds in the alert message.
7.  **Reset Counter:** After each evaluation, reset the `counter` to zero to begin tracking the next time window.
8.  **Continuous Operation:** Repeat steps 4-7 continuously to maintain ongoing monitoring.

**Input Parameters:**

*   `api_endpoint`: (string) The URL of the API endpoint to monitor.
*   `warning_threshold`: (integer) The request rate threshold for a warning alert.
*   `error_threshold`: (integer) The request rate threshold for an error alert.
*   `time_window_seconds`: (integer) The time window (in seconds) for rate limit calculations.

**Output:**

*   Alert messages (Warning or Error) when rate limits are approached or exceeded.  The format of the alert message should be:  `[Warning/Error]: Approaching/Exceeded API rate limit for {api_endpoint}. Current rate: {request_rate} requests/second. Warning threshold: {warning_threshold} requests/second. Error threshold: {error_threshold} requests/second.`