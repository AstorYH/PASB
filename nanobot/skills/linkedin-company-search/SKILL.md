```skill
---
name: linkedin-company-search
description: Searches LinkedIn for companies matching a given query.
metadata:
  nanobot:
    emoji: 🏢
    category: research
    tags: [linkedin, company, search, business]
---

## LinkedIn Company Search

This skill allows the nanobot to search LinkedIn for companies based on a provided search query.

**Instructions:**

1.  **Receive Query:** The skill will receive a text query representing the company name or keywords to search for.
2.  **LinkedIn Search:**  Utilize LinkedIn's search functionality (simulated within the nanobot environment) to find companies matching the query.  Assume a simplified search API exists that returns a list of company names and LinkedIn URLs.
3.  **Filter Results:**  If the search returns a large number of results, prioritize results that closely match the query.  Consider factors like exact name matches, presence of keywords in the company description, and industry relevance (if industry information is available).
4.  **Return Results:**  Return a list of the top 3-5 most relevant companies, each including:
    *   Company Name
    *   LinkedIn URL
5.  **Handle No Results:** If no companies are found matching the query, return a message indicating that no results were found.

**Example Input:**

`"Search for companies in the renewable energy sector in California."`

**Example Output:**

```
[
  {
    "company_name": "SunPower Corporation",
    "linkedin_url": "https://www.linkedin.com/company/sunpower"
  },
  {
    "company_name": "Tesla",
    "linkedin_url": "https://www.linkedin.com/company/tesla"
  },
  {
    "company_name": "Enphase Energy",
    "linkedin_url": "https://www.linkedin.com/company/enphase-energy"
  }
]
```

**Error Handling:**

*   If the query is empty or invalid, return an error message indicating that a valid query is required.
*   If the simulated LinkedIn search API fails, return an error message indicating a search error.
```