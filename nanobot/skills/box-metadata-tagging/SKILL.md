```skill
---
name: box-metadata-tagging
description: Automatically analyzes the contents of a box and applies relevant metadata tags.
metadata:
  nanobot:
    emoji: 📦
    category: analysis
    tags: [data, organization, tagging, box]
  risk: low
  cost: medium
---

## Instructions

This skill analyzes the contents of a designated box and applies appropriate metadata tags based on its findings. The box is assumed to be a physical container with identifiable contents.

**1. Initial Assessment:**

*   **Scan Contents:** Use onboard sensors (visual, thermal, chemical, etc.) to create a comprehensive scan of the box's contents. Prioritize identifying distinct objects and materials.
*   **Categorize Objects:** Attempt to categorize each identified object. Use a pre-existing knowledge base (internal or networked) to match objects to known categories (e.g., "electronics," "clothing," "documents," "food"). If an object cannot be categorized, flag it for further analysis.
*   **Material Identification:** Identify the primary materials of each object.  (e.g., "plastic," "metal," "paper," "wood").

**2. Tag Generation:**

Based on the categorization and material identification, generate a set of metadata tags.  Prioritize tags that are most descriptive and relevant.

*   **Category Tags:**  Apply tags corresponding to the object categories (e.g., "electronics," "clothing").
*   **Material Tags:** Apply tags corresponding to the materials (e.g., "plastic," "metal").
*   **Condition Tags:** Assess the condition of the contents. Apply tags like "new," "used," "damaged," "fragile."
*   **Quantity Tags:** Estimate the quantity of each type of object. (e.g., "quantity: 3," "quantity: many").
*   **Contextual Tags (if possible):** If the contents suggest a specific context (e.g., "office supplies," "camping gear," "medical equipment"), apply a contextual tag.

**3. Tag Application:**

*   **Apply Tags:**  Apply the generated tags to the box's metadata record.
*   **Confidence Levels:**  Assign a confidence level to each tag based on the certainty of the analysis. (e.g., "electronics (confidence: 95%)", "fragile (confidence: 70%)").
*   **Flag Uncertainties:**  If any object or material could not be confidently identified, create a "needs review" tag and include a description of the uncertainty.

**4. Reporting:**

*   **Report Tags:**  Report the applied tags and their confidence levels to the requesting system.
*   **Report Uncertainties:** Report any "needs review" tags and their associated descriptions.

**Example:**

A box contains several books, a laptop, and a pen.

*   **Generated Tags:** `[books, electronics, office supplies, paper, plastic, quantity: 5, new]`
*   **Confidence Levels:** `[books (confidence: 98%), electronics (confidence: 92%), office supplies (confidence: 85%), paper (confidence: 95%), plastic (confidence: 90%), quantity: 5 (confidence: 90%), new (confidence: 75%)]`

**Error Handling:**

*   **Insufficient Data:** If the box is too dark or obstructed to scan, report an error and request better conditions.
*   **Unidentifiable Objects:** If an object remains unidentifiable after multiple scans, flag it for manual review.
*   **Knowledge Base Errors:** If the knowledge base is incomplete or inaccurate, report the error and suggest updating the knowledge base.
```