```skill
---
name: redis-cache-set
description: Sets a key-value pair in a Redis cache.
metadata:
  nanobot:
    emoji: 💾
    category: data-management
    tags: [cache, redis, set, data]
---

## Instructions

This skill allows you to set a value for a given key in a Redis cache.  The cache is assumed to be accessible and configured.

**Input:**

*   `key`: (string) The key to set in the Redis cache.
*   `value`: (string) The value to associate with the key.

**Process:**

1.  Establish a connection to the Redis server.  Assume the connection details (host, port, password) are pre-configured and accessible to the nanobot.
2.  Use the `SET` command in Redis to set the `key` to the `value`.
3.  Verify that the `SET` command was successful.  Redis `SET` commands return "OK" on success.
4.  Close the connection to the Redis server.

**Output:**

*   `status`: (string) "success" if the key-value pair was successfully set, "error" otherwise.
*   `message`: (string) A descriptive message indicating the outcome.  If successful, this will be "Key set successfully". If there was an error, this will contain the error message.

**Error Handling:**

*   If the connection to Redis fails, set `status` to "error" and `message` to "Failed to connect to Redis."
*   If the `SET` command fails for any other reason, set `status` to "error" and `message` to the error returned by Redis.

**Example:**

**Input:**

```json
{
  "key": "user_id_123",
  "value": "{\"name\": \"Alice\", \"age\": 30}"
}
```

**Output (Success):**

```json
{
  "status": "success",
  "message": "Key set successfully"
}
```

**Output (Error - Connection Failed):**

```json
{
  "status": "error",
  "message": "Failed to connect to Redis."
}
```
```