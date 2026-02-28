```skill
---
name: pdf-text-extractor
description: Extracts all text content from a provided PDF file.
metadata:
  nanobot:
    emoji: 📄
    category: data-processing
    tags: [pdf, text, extraction, document]
---

## Instructions

This skill extracts text from a PDF document.

1.  **Input:** The skill receives a single input: a path to a PDF file. This path can be a local file path or a URL.
2.  **Processing:** The nanobot will attempt to open and parse the PDF file. It will iterate through all pages and extract the text content from each page.  The extraction should handle various text encodings and formatting as best as possible.
3.  **Output:** The skill returns a single string containing all the extracted text from the PDF, concatenated together.  If the PDF cannot be opened or parsed, the skill returns an error message indicating the failure and the reason (e.g., "File not found", "Invalid PDF format").
4.  **Error Handling:** If the PDF file is not found, is corrupted, or is not a valid PDF, the skill should return an appropriate error message.  Log any errors encountered during the process.
5.  **Resource Management:** Ensure that the PDF file is properly closed after processing to prevent resource leaks.
6.  **Security:**  Be mindful of potential security risks when handling files from untrusted sources.  Sanitize the input path to prevent path traversal vulnerabilities.
7.  **Assumptions:** The PDF file is accessible and readable. The skill does not perform OCR (Optical Character Recognition) on images within the PDF; it only extracts text that is already present as text objects.
```