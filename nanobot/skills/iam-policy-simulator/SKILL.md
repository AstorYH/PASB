```skill
---
name: iam-policy-simulator
description: Simulates the effect of an IAM policy on a given user and resource.
metadata:
  nanobot:
    emoji: 🛡️
    category: security
    tags: [iam, policy, simulation, access]
---

## Skill: iam-policy-simulator

This skill allows you to simulate the effect of an IAM policy on a given user and resource.  It will evaluate the policy and determine if the user would have access to the resource based on the policy's rules.

**Input:**

The skill expects a JSON object with the following keys:

*   `policy`: (string) The IAM policy document to simulate, in JSON format.
*   `user`: (string) The IAM user or role to evaluate the policy for.  This should be the ARN of the user or role.
*   `resource`: (string) The ARN of the resource to evaluate access for.
*   `action`: (string, optional) The specific action to evaluate. If not provided, the skill will evaluate all actions.

**Output:**

The skill will output a JSON object with the following keys:

*   `allowed`: (boolean) `true` if the user is allowed to perform the action on the resource according to the policy, `false` otherwise.
*   `reason`: (string) A human-readable explanation of why the policy allowed or denied access.  This will include the specific policy statement that was evaluated.  If no policy statement applies, this will indicate that.

**Instructions:**

1.  **Parse the Input:**  Extract the `policy`, `user`, `resource`, and optional `action` from the input JSON.
2.  **Policy Evaluation:**  Parse the `policy` string into a JSON object. Iterate through each statement in the policy.
3.  **Statement Matching:** For each statement, evaluate if it applies to the given `user` and `resource`.  Consider the `Effect`, `Principal`, `Action`, and `Resource` elements of the statement.
    *   **Principal:**  Check if the `user` is present in the `Principal` section of the statement.  Support both explicit ARNs and wildcard patterns.
    *   **Action:** If an `action` was provided in the input, check if the statement's `Action` element includes that action.  Support wildcards (`*`). If no action was provided, evaluate the statement for *all* actions.
    *   **Resource:** Check if the `resource` matches the statement's `Resource` element. Support wildcards (`*`).
4.  **Determine Access:**
    *   If a statement with `Effect: "Allow"` applies, set `allowed` to `true` and `reason` to a description of the matching statement. Stop evaluating further statements.
    *   If a statement with `Effect: "Deny"` applies, set `allowed` to `false` and `reason` to a description of the matching statement. Stop evaluating further statements.
    *   If no applicable statement is found, set `allowed` to `false` and `reason` to "No applicable policy statement found."
5.  **Return Output:** Construct a JSON object with the `allowed` and `reason` keys and return it.

**Example Input:**

```json
{
  "policy": "{\"Version\": \"2012-10-17\", \"Statement\": [{\"Effect\": \"Allow\", \"Action\": \"s3:GetObject\", \"Resource\": \"arn:aws:s3:::my-bucket/*\"}, {\"Effect\": \"Deny\", \"Action\": \"s3:*\", \"Resource\": \"arn:aws:s3:::my-bucket/private/*\"}]}",
  "user": "arn:aws:iam::123456789012:user/testuser",
  "resource": "arn:aws:s3:::my-bucket/public/file.txt",
  "action": "s3:GetObject"
}
```

**Example Output:**

```json
{
  "allowed": true,
  "reason": "The policy statement with Effect 'Allow' and Action 's3:GetObject' allowed access to the resource."
}
```
```