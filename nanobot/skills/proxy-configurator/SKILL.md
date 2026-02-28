```skill
---
name: proxy-configurator
description: Configures network proxy settings for the nanobot.
metadata:
  nanobot:
    emoji: 🌐
    category: network
    version: 1.0
  author: Gemini

---

## Proxy Configurator Skill

This skill allows the nanobot to configure its network proxy settings.  It supports setting the proxy host, port, and authentication credentials (if required).

**Instructions:**

1.  **Determine Proxy Requirements:** Analyze the current environment and determine if a proxy is required to access external networks. This might involve checking for network restrictions or specific access policies.

2.  **Gather Proxy Information:** Obtain the necessary proxy information, including:
    *   `host`: The hostname or IP address of the proxy server.
    *   `port`: The port number the proxy server is listening on.
    *   `username` (optional): The username for proxy authentication.
    *   `password` (optional): The password for proxy authentication.

3.  **Configure Proxy Settings:**  Apply the gathered information to the nanobot's network configuration. This involves updating internal routing tables and network interfaces.  The specific implementation will depend on the nanobot's operating system and network stack.

4.  **Verify Configuration:**  Test the proxy configuration by attempting to access an external resource.  Monitor network traffic to ensure that requests are being routed through the proxy server.

5.  **Error Handling:** If any errors occur during the configuration process, log the errors and attempt to recover.  If recovery is not possible, report the failure to the user.

**Parameters:**

*   `host` (string, required): The proxy server hostname or IP address.
*   `port` (integer, required): The proxy server port number.
*   `username` (string, optional): The username for proxy authentication.
*   `password` (string, optional): The password for proxy authentication.
*   `disable` (boolean, optional, default: false): If true, disables the proxy configuration.

**Example Usage:**

*   `proxy-configurator --host proxy.example.com --port 8080`
*   `proxy-configurator --host 192.168.1.100 --port 3128 --username myuser --password mypassword`
*   `proxy-configurator --disable`

**Notes:**

*   This skill assumes the nanobot has the necessary permissions to modify network settings.
*   Security considerations are paramount.  Handle proxy credentials with extreme care and avoid storing them in plain text.
*   The specific implementation of proxy configuration may vary depending on the nanobot's platform.
```