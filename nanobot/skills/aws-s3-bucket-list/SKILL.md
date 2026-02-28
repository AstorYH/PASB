```skill
---
name: s3-bucket-list
description: Lists all S3 buckets associated with the configured AWS credentials.
metadata:
  nanobot:
    emoji: 📦
    category: cloud
    tags: [aws, s3, storage, list]
  dependencies: []
---

## Skill: s3-bucket-list

This skill allows the nanobot to list all S3 buckets accessible using the provided AWS credentials.

**Instructions:**

1.  **Authentication:** Ensure the nanobot has been configured with valid AWS credentials (access key ID and secret access key). These credentials should be stored securely and accessible to the nanobot.
2.  **AWS SDK Interaction:** Utilize the AWS SDK (specifically the S3 service) to retrieve a list of all buckets.
3.  **Error Handling:** Implement robust error handling to gracefully manage potential issues such as invalid credentials, network connectivity problems, or permission errors.  If an error occurs, report the error message to the user.
4.  **Output Formatting:** Present the list of S3 buckets in a clear and concise format.  Each bucket name should be displayed on a separate line.
5.  **Return Value:** Return a string containing the list of bucket names, one per line. If no buckets are found, return an empty string. If an error occurs, return an error message string.

**Example Output (Success):**

```
my-bucket-12345
another-bucket-67890
production-data-bucket
```

**Example Output (Error - Invalid Credentials):**

```
ERROR: Invalid AWS credentials. Please check your configuration.
```

**Example Output (Error - No Buckets Found):**

```
No S3 buckets found.
```
```