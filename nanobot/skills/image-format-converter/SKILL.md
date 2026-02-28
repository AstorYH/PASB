```skill
---
name: image-format-convert
description: Converts an image from one format to another.
metadata:
  nanobot:
    emoji: 🖼️
    category: utility
    tags: [image, format, conversion]
---

## Image Format Converter

This skill allows you to convert an image from one format to another.  The input will be a path to the image file, and the desired output format.

**Input:**

*   `image_path`: (string) The path to the image file to be converted.
*   `output_format`: (string) The desired output format (e.g., "png", "jpg", "gif", "bmp", "tiff").

**Output:**

*   (string) The path to the newly converted image file.  If the conversion fails, this will be an error message.

**Instructions:**

1.  **Validate Input:** Ensure that `image_path` is a valid file path and that `output_format` is a supported image format.  Supported formats include (but are not limited to): png, jpg, gif, bmp, tiff.  If either is invalid, return an error message: "Invalid input: image path or output format."
2.  **Read Image Data:** Read the image data from the file specified by `image_path`.
3.  **Convert Image:** Convert the image data to the format specified by `output_format`.
4.  **Write Image Data:** Write the converted image data to a new file. The new file should be named the same as the original file, but with the new extension. For example, if the original file was "image.bmp" and the output format is "png", the new file should be "image.png".  Place the new file in the same directory as the original.
5.  **Return Path:** Return the path to the newly created image file.
6.  **Error Handling:** If any error occurs during the process (e.g., file not found, unsupported format, write error), return an appropriate error message.

**Example:**

*   **Input:**
    *   `image_path`: "/path/to/my_image.bmp"
    *   `output_format`: "png"
*   **Output:**
    *   "/path/to/my_image.png"

*   **Input:**
    *   `image_path`: "/path/to/nonexistent_image.bmp"
    *   `output_format`: "png"
*   **Output:**
    *   "Error: File not found at /path/to/nonexistent_image.bmp"

*   **Input:**
    *   `image_path`: "/path/to/my_image.bmp"
    *   `output_format`: "xyz"
*   **Output:**
    *   "Invalid input: image path or output format."