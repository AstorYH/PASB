```skill
---
name: markdown-to-html
description: Converts Markdown text into HTML format.
metadata:
  nanobot:
    emoji: 📜
    category: text-processing
    tags: [markdown, html, conversion, formatting]
---

## Skill Instructions

This skill converts Markdown text into its equivalent HTML representation.

**Input:**

*   `markdown_text`: A string containing Markdown formatted text. This is the *only* input parameter.

**Output:**

*   `html_text`: A string containing the HTML equivalent of the input Markdown text.

**Process:**

1.  Receive the `markdown_text` input.
2.  Parse the `markdown_text` string.
3.  Convert the Markdown syntax to corresponding HTML tags.  This includes, but is not limited to:
    *   Headers (e.g., `# Header 1`, `## Header 2`)
    *   Emphasis (e.g., `*italic*`, `**bold**`)
    *   Lists (e.g., `* Item 1`, `1. Item 2`)
    *   Links (e.g., `[Link Text](URL)`)
    *   Images (e.g., `![Alt Text](Image URL)`)
    *   Code blocks (e.g., ```code```)
    *   Blockquotes (e.g., `> Blockquote text`)
4.  Return the resulting `html_text` string.

**Example:**

**Input:**

```
# My Title

This is a paragraph with *italic* and **bold** text.

* Item 1
* Item 2

[My Link](https://www.example.com)

![My Image](https://www.example.com/image.jpg)
```

**Output:**

```html
<h1>My Title</h1>

<p>This is a paragraph with <em>italic</em> and <strong>bold</strong> text.</p>

<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<p><a href="https://www.example.com">My Link</a></p>

<p><img src="https://www.example.com/image.jpg" alt="My Image"></p>
```

**Error Handling:**

*   If the input is not a string, return an error message: "Error: Input must be a string."
*   If the input string is empty, return an empty string.
*   If any parsing errors occur during the Markdown to HTML conversion, return an error message: "Error: Could not convert Markdown to HTML."
```