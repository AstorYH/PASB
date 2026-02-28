```skill
---
name: zip-archive-creator
description: Creates a compressed ZIP archive of specified files or directories.
metadata:
  nanobot:
    emoji: 📦
    category: data-management
    tags: [archive, compression, zip, data]
---

## Skill: zip-archive-creator

This skill allows the nanobot to create a ZIP archive containing the files and/or directories you specify.

**Instructions:**

1.  **Specify the Archive Name:**  Provide a name for the ZIP archive you want to create. This will be the filename of the resulting ZIP file (e.g., `my_archive.zip`).
2.  **Specify Files/Directories to Archive:**  List the files and/or directories you want to include in the archive.  You can provide a single file, multiple files, or a directory.  Use absolute or relative paths as appropriate.  Wildcards (e.g., `*.txt`) are supported for selecting multiple files within a directory.
3.  **Compression Level (Optional):** You can optionally specify the compression level.  Valid values are:
    *   `store`: No compression (fastest).
    *   `fast`: Fastest compression, smallest reduction in size.
    *   `normal`: Default compression level (balance of speed and size).
    *   `maximum`: Best compression, slowest.
    If no compression level is specified, `normal` will be used.
4.  **Output Location (Optional):** Specify the directory where the ZIP archive should be created. If no output location is specified, the archive will be created in the current working directory.

**Example Input:**

```
create zip archive named "documents.zip" containing "report.txt", "images/".  Use compression level "fast".  Output to "/backup/".
```

**Breakdown of Example:**

*   `create zip archive named "documents.zip"`:  This tells the nanobot to create a ZIP archive named "documents.zip".
*   `containing "report.txt", "images/"`: This specifies that "report.txt" and the directory "images/" should be included in the archive.
*   `Use compression level "fast"`: This sets the compression level to "fast".
*   `Output to "/backup/"`: This specifies that the archive should be created in the "/backup/" directory.

**Error Handling:**

*   If the specified archive name already exists, the nanobot will attempt to overwrite it unless explicitly prevented by a safety protocol.
*   If any of the specified files or directories do not exist, the nanobot will report an error and not create the archive.
*   If there are permission issues accessing the files or directories, the nanobot will report an error.
```