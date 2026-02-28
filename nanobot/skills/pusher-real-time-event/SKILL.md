```skill
---
name: pusher-realtime-event
description: Subscribes to and processes real-time events from a Pusher channel.
metadata:
  nanobot:
    emoji: 📡
    category: communication
    tags: [realtime, pusher, events, subscription]
---

## Pusher Real-time Event Skill

This skill allows the nanobot to subscribe to a Pusher channel and react to events published to that channel.  It requires a valid Pusher API key and channel name.

**Prerequisites:**

*   A Pusher account and API key.
*   A Pusher channel name.

**Instructions:**

1.  **Initialization:** The nanobot will first attempt to connect to the Pusher service using the provided API key and channel name.  This connection will be maintained for the duration of the skill's execution.
2.  **Event Subscription:** Once connected, the nanobot will subscribe to all events published on the specified Pusher channel.
3.  **Event Processing:** When an event is received, the nanobot will parse the event data. The event data will be treated as a JSON object.
4.  **Action Determination:** The nanobot will analyze the event data to determine the appropriate action to take.  The event data should contain a key named `event_type`. The nanobot will use this key to determine the action.
    *   If `event_type` is `message`, the nanobot will log the message content.
    *   If `event_type` is `user_joined`, the nanobot will log the user's ID.
    *   If `event_type` is `user_left`, the nanobot will log the user's ID.
    *   For any other `event_type`, the nanobot will log the entire event data.
5.  **Error Handling:** If the connection to Pusher fails, the nanobot will log an error message and attempt to reconnect every 60 seconds. If the reconnection fails after 5 attempts, the skill will terminate.  If an event cannot be parsed as JSON, the nanobot will log an error and continue processing subsequent events.

**Input Parameters:**

*   `api_key`: (string, required) Your Pusher API key.
*   `channel_name`: (string, required) The name of the Pusher channel to subscribe to.

**Output:**

*   Log messages indicating connection status, event reception, and any errors encountered.

**Example Event Data (JSON):**

```json
{
  "event": "message",
  "data": {
    "text": "Hello, world!"
  }
}
```

```json
{
  "event": "user_joined",
  "data": {
    "id": "unique_user_id",
    "info": {
      "name": "John Doe"
    }
  }
}
```

```json
{
  "event": "user_left",
  "data": {
    "id": "unique_user_id"
  }
}
```

**Notes:**

*   This skill assumes a relatively stable Pusher connection.  Network interruptions may cause temporary disconnections.
*   The `event_type` field in the event data is crucial for determining the appropriate action. Ensure that your Pusher events include this field.
*   The nanobot will not actively *publish* events to Pusher; it only *subscribes* and reacts.
```