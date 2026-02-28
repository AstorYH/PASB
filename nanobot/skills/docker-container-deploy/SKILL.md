```skill
---
name: docker-container-deploy
description: Deploys a Docker container to a specified host, pulling the image if necessary.
metadata:
  nanobot:
    emoji: 🐳
    category: deployment
    tags: [docker, container, deployment, orchestration]
---

## Skill: Docker Container Deploy

This skill allows you to deploy a Docker container to a target host. It handles image pulling and container creation.

**Instructions:**

1.  **Identify the Target Host:** Determine the hostname or IP address of the machine where you want to deploy the container.  This is crucial for proper communication.
2.  **Image Name:** Specify the Docker image you want to deploy. This can be a public image from Docker Hub (e.g., `nginx:latest`) or a private image accessible to the nanobot.  Include the tag if necessary.
3.  **Container Name:** Choose a unique name for the container on the target host.
4.  **Ports (Optional):** If the container exposes any ports, specify them as a list of key-value pairs. The key is the host port, and the value is the container port.  Example: `[ "8080:80", "443:443" ]`. If no ports are specified, the container will not be exposed.
5.  **Environment Variables (Optional):** Provide a list of environment variables to set within the container.  Specify them as a list of key-value pairs. Example: `[ "API_KEY=your_api_key", "DEBUG=true" ]`.
6.  **Volumes (Optional):** Define any volumes to mount into the container.  Specify them as a list of key-value pairs where the key is the container path and the value is the host path. Example: `[ "/data:/host/data" ]`.
7.  **Command/Entrypoint (Optional):** If you need to override the container's default command or entrypoint, provide them as strings.  `command: "python /app/main.py"` or `entrypoint: ["/usr/bin/java", "-jar", "/app/app.jar"]`.
8.  **Restart Policy (Optional):** Set the restart policy for the container.  Valid values are `no`, `on-failure`, `always`, and `unless-stopped`.  Default is `no`.
9.  **Execute:** The nanobot will connect to the target host via SSH (assuming SSH access is configured). It will then:
    *   Check if the image exists locally on the target host.
    *   If the image does not exist, it will pull the image from Docker Hub (or the specified registry).
    *   Create and start the container with the specified name, ports, environment variables, volumes, command/entrypoint, and restart policy.
    *   Verify that the container is running.

**Example Input:**

```json
{
  "target_host": "192.168.1.100",
  "image_name": "nginx:latest",
  "container_name": "my_nginx_container",
  "ports": ["8080:80"],
  "environment": ["DEBUG=true"],
  "restart_policy": "always"
}
```

**Error Handling:**

*   **Connection Refused:**  If the nanobot cannot connect to the target host via SSH, it will report a "Connection Refused" error.
*   **Image Not Found:** If the specified image is not found on Docker Hub or the configured registry, it will report an "Image Not Found" error.
*   **Container Creation Failed:** If there is an error creating the container (e.g., port conflict, invalid volume path), it will report a "Container Creation Failed" error.
*   **Container Start Failed:** If the container fails to start, it will report a "Container Start Failed" error.
```