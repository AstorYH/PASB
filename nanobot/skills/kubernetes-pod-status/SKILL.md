```skill
---
name: pod-status
description: Retrieves and reports the status of a Kubernetes Pod.
metadata:
  nanobot:
    emoji: 🚀
    category: monitoring
    tags:
      - kubernetes
      - pod
      - status
  dependencies: []
---

## Skill: pod-status

This skill allows the nanobot to query the status of a Kubernetes Pod.

### Instructions

1.  **Identify the Pod:** The user will provide the name of the Pod to check.  This will be passed as an argument named `pod_name`.
2.  **Access Kubernetes API:** Use the Kubernetes API to retrieve the Pod's status.  Assume the nanobot has the necessary credentials and access to the Kubernetes cluster.
3.  **Extract Status Information:**  From the API response, extract the following information:
    *   `phase`: The current phase of the Pod (e.g., Pending, Running, Succeeded, Failed, Unknown).
    *   `status`: A more detailed status string (e.g., "Running", "Error").
    *   `ready`: Boolean indicating if the Pod is ready to serve traffic.
    *   `restarts`: The number of times the Pod has been restarted.
    *   `conditions`: A list of conditions affecting the Pod (e.g., Ready, Initialized, Scheduled).  Report the status (True/False) of the "Ready" condition.
4.  **Report Status:**  Report the extracted information to the user in a clear and concise format.  For example:

    ```
    Pod Status for pod_name:
    Phase: Running
    Status: Running
    Ready: True
    Restarts: 2
    Ready Condition: True
    ```

    If the Pod is not found or an error occurs, report an appropriate error message. For example:

    ```
    Error: Pod pod_name not found.
    ```

### Arguments

*   `pod_name` (string): The name of the Kubernetes Pod to check.

### Return Value

A string containing the Pod's status information, or an error message if the Pod is not found or an error occurs.
```