```skill
---
name: system-health-monitor
description: Continuously monitors system resources and reports anomalies.
metadata:
  nanobot:
    emoji: 🩺
    category: diagnostics
    tags: [monitoring, health, resources, anomaly]
---

## System Health Monitor

This skill continuously monitors key system resources and reports any detected anomalies. It operates in a loop, periodically checking resource usage and comparing it against predefined thresholds.

**Instructions:**

1.  **Initialization:**
    *   Define a list of resources to monitor.  Examples: CPU usage, memory usage, disk space, network bandwidth.
    *   For each resource, define a "normal" range (minimum and maximum acceptable values).  These ranges can be adjusted based on the system's typical operation.
    *   Set a monitoring interval (e.g., every 5 seconds, every minute).

2.  **Monitoring Loop:**
    *   **Resource Acquisition:**  For each resource in the monitoring list, acquire its current value.  Use appropriate system calls or APIs to obtain this data.
    *   **Threshold Comparison:** Compare the acquired value against the defined "normal" range for that resource.
    *   **Anomaly Detection:** If the value falls outside the normal range, flag it as an anomaly.
    *   **Reporting:** If an anomaly is detected:
        *   Log the anomaly, including the resource name, current value, and the normal range.
        *   Generate a notification (e.g., a message to a designated channel, an alert to a monitoring system).  The notification should clearly state the anomaly and its severity.
    *   **Delay:** Wait for the specified monitoring interval before repeating the loop.

3.  **Error Handling:**
    *   Implement robust error handling to gracefully handle situations where resource acquisition fails or the system is unavailable.  Log any errors and attempt to retry after a short delay.

4.  **Configuration:**
    *   The monitoring list, normal ranges, and monitoring interval should be configurable.  This allows the skill to be adapted to different systems and environments.  Consider storing this configuration in a persistent storage location.

**Example Configuration (Illustrative):**

```
{
  "resources": [
    {
      "name": "cpu_usage",
      "min": 0,
      "max": 80,
      "units": "%"
    },
    {
      "name": "memory_usage",
      "min": 0,
      "max": 90,
      "units": "%"
    },
    {
      "name": "disk_space_root",
      "min": 10,
      "max": 100,
      "units": "%"
    }
  ],
  "monitoring_interval": 60  // seconds
}
```

**Notes:**

*   The specific system calls or APIs used to acquire resource data will depend on the target operating system and environment.
*   The definition of "normal" ranges is crucial for effective anomaly detection.  These ranges should be based on historical data and system knowledge.
*   Consider adding features such as trend analysis and predictive alerting to improve the accuracy and effectiveness of the monitoring system.
*   Implement a mechanism to allow the user to acknowledge and dismiss anomalies.
```