```skill
---
name: smartsheet-sheet-snapshot
description: Captures a complete snapshot of a Smartsheet sheet, including all data and formatting, for later analysis or archival.
metadata:
  nanobot:
    emoji: 📸
    category: data-management
    tags: [smartsheet, data, snapshot, archive, backup]
---

## Smartsheet Sheet Snapshot

This skill allows the nanobot to create a complete snapshot of a Smartsheet sheet. The snapshot will include all rows, columns, data, formatting (e.g., conditional formatting, number formats), and sheet-level settings.  The resulting snapshot will be stored as a structured data object (e.g., JSON or a similar format) within the nanobot's memory.

**Instructions:**

1.  **Identify the Smartsheet Sheet:** The nanobot needs to know *which* Smartsheet sheet to snapshot. This will be provided as input.  The input should be a Smartsheet sheet ID (a long alphanumeric string).  Example: `1234567890abcdefg`.
2.  **Access Smartsheet API:** The nanobot will use its internal Smartsheet API access (assumed to be pre-configured).
3.  **Retrieve Sheet Data:** Using the provided sheet ID, the nanobot will query the Smartsheet API to retrieve all data associated with the sheet. This includes:
    *   Column definitions (names, data types, formats)
    *   Row data (all cells and their values)
    *   Conditional formatting rules
    *   Number formats
    *   Sheet-level settings (e.g., sharing permissions, grid settings)
4.  **Structure the Snapshot:** The retrieved data will be structured into a consistent format. A JSON format is recommended, but the specific format can be adjusted based on the nanobot's capabilities and the intended use of the snapshot.  The JSON structure should clearly represent the sheet's columns, rows, and formatting.
5.  **Store the Snapshot:** The structured snapshot data will be stored within the nanobot's memory.  The nanobot should provide a mechanism for accessing or exporting this snapshot data later.
6.  **Confirmation:** Upon successful completion, the nanobot will confirm the snapshot creation and provide the storage location (or a reference to the stored data).

**Input:**

*   `sheet_id`: (String) The Smartsheet sheet ID to snapshot.

**Output:**

*   `snapshot_id`: (String) A unique identifier for the created snapshot.
*   `storage_location`: (String)  A reference to where the snapshot data is stored within the nanobot's memory.
*   `status`: (String) "success" or "failure"

**Error Handling:**

*   If the provided `sheet_id` is invalid, return `status: failure` and an error message indicating the invalid sheet ID.
*   If there are issues accessing the Smartsheet API, return `status: failure` and an error message describing the API error.
*   If there are issues structuring or storing the snapshot data, return `status: failure` and an error message describing the problem.
```