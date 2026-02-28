```skill
---
name: csv-parser
description: Parses a CSV string and returns a structured data representation.
metadata:
  nanobot:
    emoji: 📊
    category: data-processing
    tags: [data, parsing, csv, structured]
---

## CSV Parser Skill

This skill parses a comma-separated value (CSV) string and returns a list of dictionaries, where each dictionary represents a row in the CSV and keys are derived from the header row.

**Input:**

*   `csv_string`: (string) The CSV data to parse.  Must include a header row.

**Output:**

*   `data`: (list of dictionaries) A list of dictionaries representing the parsed CSV data.  If the input is invalid or empty, returns an empty list.

**Instructions:**

1.  **Input Validation:** Check if the `csv_string` is empty or `None`. If so, return an empty list (`[]`).
2.  **Split into Lines:** Split the `csv_string` into a list of lines using the newline character (`\n`) as the delimiter.
3.  **Extract Header:** Assume the first line is the header row. Split this line by commas (`,`) to get the column names.  Strip any leading/trailing whitespace from each column name.
4.  **Parse Data Rows:** Iterate through the remaining lines (starting from the second line). For each line:
    *   Split the line by commas (`,`).
    *   Create a dictionary where the keys are the column names from the header row and the values are the corresponding values from the current data row.
    *   Strip any leading/trailing whitespace from each value.
    *   Add this dictionary to the `data` list.
5.  **Return Data:** Return the `data` list.

**Example:**

**Input:**

```
name,age,city
Alice,30,New York
Bob,25,London
Charlie,35,Paris
```

**Output:**

```json
[
  {
    "name": "Alice",
    "age": "30",
    "city": "New York"
  },
  {
    "name": "Bob",
    "age": "25",
    "city": "London"
  },
  {
    "name": "Charlie",
    "age": "35",
    "city": "Paris"
  }
]
```

**Error Handling:**

*   If a line has a different number of columns than the header row, skip that line and log an error.  Do not halt execution.
*   If the input CSV string is malformed (e.g., missing commas), attempt to parse as much as possible and log any errors encountered.
```