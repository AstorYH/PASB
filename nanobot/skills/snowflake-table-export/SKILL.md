```skill
---
name: snowflake-table-export
description: Exports data from a Snowflake table to a specified file format and location.
metadata:
  nanobot:
    emoji: ❄️
    category: data-management
    tags: [snowflake, database, export, data]
  dependencies: []
---

## Snowflake Table Export Skill

This skill allows you to export data from a Snowflake table to a specified file format (CSV, JSON, Parquet) and location within Snowflake's internal stage or an external cloud storage location (e.g., AWS S3, Google Cloud Storage, Azure Blob Storage).

**Instructions:**

1.  **Authentication:** Ensure the nanobot has the necessary credentials to access the Snowflake account and the specified table. This typically involves providing a Snowflake user, password, and account identifier.  The nanobot will attempt to retrieve these from environment variables or a secure configuration store.

2.  **Table Identification:** Specify the Snowflake table to export. This includes the database name, schema name, and table name.

3.  **File Format:** Choose the desired file format for the exported data. Supported formats include:
    *   `CSV`: Comma-Separated Values
    *   `JSON`: JavaScript Object Notation
    *   `PARQUET`: Columnar storage format optimized for analytics.

4.  **File Location:** Define the location where the exported data will be stored. This can be:
    *   **Snowflake Internal Stage:** A location within Snowflake's storage.  Specify the stage name.
    *   **External Cloud Storage:**  Specify the cloud storage provider (e.g., `s3://bucket-name/path/to/data/`, `gcs://bucket-name/path/to/data/`, `azure://account-name.blob.core.windows.net/container-name/path/to/data/`).  Ensure the nanobot has the appropriate permissions to write to this location.

5.  **Export Command Construction:** The nanobot will construct a Snowflake `COPY INTO` command based on the provided parameters.  The command will include:
    *   The table to export from.
    *   The file format.
    *   The file location.
    *   Optional parameters like `FILE_FORMAT` (if not using the default), `OVERWRITE = TRUE/FALSE`, `MAX_FILE_SIZE`, and `COMPRESSION`.

6.  **Command Execution:** The nanobot will execute the constructed `COPY INTO` command against the Snowflake account.

7.  **Verification:** After execution, the nanobot will check the Snowflake query history to verify that the command completed successfully.  It will also attempt to list the files in the specified location to confirm that the data was exported.

**Parameters:**

*   `snowflake_account`: (string, required) The Snowflake account identifier (e.g., `myaccount.snowflakecomputing.com`).
*   `snowflake_user`: (string, required) The Snowflake user to connect with.
*   `snowflake_password`: (string, required) The Snowflake password for the user.
*   `database_name`: (string, required) The name of the Snowflake database.
*   `schema_name`: (string, required) The name of the Snowflake schema.
*   `table_name`: (string, required) The name of the Snowflake table.
*   `file_format`: (string, optional, default: `CSV`) The file format for the exported data (`CSV`, `JSON`, `PARQUET`).
*   `file_location`: (string, required) The location to store the exported data.  Must be a valid Snowflake stage name or a cloud storage URL.
*   `overwrite`: (boolean, optional, default: `TRUE`) Whether to overwrite existing files at the destination.
*   `max_file_size`: (string, optional) Maximum file size in MB.  Example: `1000`.
*   `compression`: (string, optional) Compression algorithm to use (e.g., `GZIP`, `BZIP2`, `BROTLI`).

**Example:**

To export the `customers` table from the `sales` database and `public` schema to an S3 bucket:

```json
{
  "snowflake_account": "myaccount.snowflakecomputing.com",
  "snowflake_user": "myuser",
  "snowflake_password": "mypassword",
  "database_name": "sales",
  "schema_name": "public",
  "table_name": "customers",
  "file_format": "CSV",
  "file_location": "s3://mybucket/exports/customers.csv",
  "overwrite": true
}
```