```skill
---
name: front-app-conversation-tag
description: Applies a tag to a front-end application conversation based on its content.
metadata:
  nanobot:
    emoji: 🏷️
    category: communication
    tags: [conversation, tagging, front-end, application]
---

## Skill: Front App Conversation Tag

**Goal:** Analyze a conversation related to a front-end application and apply a relevant tag to it for improved organization and searchability.

**Input:** A text string representing the conversation.

**Output:** A single string representing the tag applied to the conversation. If no suitable tag is found, output "unclassified".

**Instructions:**

1.  **Analyze the Conversation:** Carefully read the provided conversation text. Look for keywords and phrases that indicate the topic or nature of the discussion. Consider the context of a front-end application.
2.  **Tag Selection:** Based on your analysis, select the most appropriate tag from the following list. Prioritize more specific tags over general ones. If the conversation doesn't clearly relate to any of these tags, or is ambiguous, output "unclassified".

    *   `ui-ux`: For discussions about user interface and user experience.
    *   `component-library`: For conversations about reusable UI components.
    *   `accessibility`: For discussions related to accessibility concerns.
    *   `performance`: For conversations about front-end application performance.
    *   `styling`: For discussions about CSS, styling, or theming.
    *   `state-management`: For conversations about state management solutions (e.g., Redux, Vuex).
    *   `routing`: For conversations about navigation and routing within the application.
    *   `api-integration`: For conversations about integrating with backend APIs.
    *   `testing`: For discussions about front-end testing strategies.
    *   `deployment`: For conversations about deploying the front-end application.
    *   `bug-report`: If the conversation is clearly a bug report.
    *   `feature-request`: If the conversation is a request for a new feature.
    *   `general-discussion`: For general conversations about the front-end application that don't fit into other categories.

3.  **Output the Tag:** Return the selected tag as a string.

**Examples:**

*   **Input:** "The button's color doesn't match the brand guidelines. It should be #FF5733."
    **Output:** `styling`
*   **Input:** "We need to ensure the form is accessible to screen readers."
    **Output:** `accessibility`
*   **Input:** "How can we optimize the loading time of the dashboard?"
    **Output:** `performance`
*   **Input:** "I'm having trouble with the authentication flow."
    **Output:** `api-integration`
*   **Input:** "What's the best way to handle user input validation?"
    **Output:** `general-discussion`
*   **Input:** "The application is crashing when I click the submit button."
    **Output:** `bug-report`
*   **Input:** "Can we add a dark mode theme?"
    **Output:** `feature-request`
*   **Input:** "This is a general update on the project's progress."
    **Output:** `general-discussion`
*   **Input:** "The weather is nice today."
    **Output:** `unclassified`
```