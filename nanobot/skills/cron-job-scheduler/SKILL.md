```skill
---
name: cron-job-scheduler
description: Schedules and executes tasks at specified intervals.
metadata:
  nanobot:
    emoji: ⏰
    category: utility
    tags: [scheduling, automation, recurring]
---

## Cron Job Scheduler

This skill allows the nanobot to schedule tasks to be executed at specific times or intervals, mimicking a cron job scheduler.

**Instructions:**

1.  **Define the Task:** Clearly specify the task to be executed. This can be another nanobot skill, a sequence of actions, or a simple command.  The task should be expressed in a format the nanobot understands (e.g., a skill name, a list of actions).
2.  **Define the Schedule:**  Use a standard cron expression (5 fields: minute hour day_of_month month day_of_week) to define the schedule.  For example:
    *   `0 0 * * *` - Execute at midnight every day.
    *   `0 12 * * 1-5` - Execute at noon every weekday.
    *   `*/5 * * * *` - Execute every 5 minutes.
3.  **Persistence:** The schedule and task definition must be stored persistently.  The nanobot should use its internal storage or a designated persistent memory location.
4.  **Execution:** The nanobot should monitor the current time against the defined schedule. When a match occurs, the task is executed.
5.  **Error Handling:** Implement error handling to catch and log any errors that occur during task execution.  Consider retrying failed tasks a limited number of times before giving up.
6.  **Management:** Provide commands or actions to:
    *   Add a new scheduled task.
    *   List all scheduled tasks.
    *   Modify an existing scheduled task.
    *   Delete a scheduled task.

**Example:**

To schedule the `data-backup` skill to run every day at 2:00 AM:

1.  **Task:** `data-backup`
2.  **Schedule:** `0 2 * * *`

The nanobot would store this information persistently and then check the time every minute. When the time reaches 2:00 AM, it would execute the `data-backup` skill.

**Considerations:**

*   **Time Synchronization:** Ensure the nanobot's internal clock is synchronized with a reliable time source.
*   **Resource Management:**  Scheduled tasks should not consume excessive resources, especially if they are running frequently.
*   **Concurrency:**  Handle potential concurrency issues if multiple scheduled tasks need to access the same resources.
*   **Idempotency:** Ideally, scheduled tasks should be idempotent, meaning they can be executed multiple times without causing unintended side effects. This is especially important for tasks that modify data.
```