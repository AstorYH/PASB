```skill
---
name: product-hunt-daily-scrape
description: Scrapes the Product Hunt daily page and extracts information about the top products.
metadata:
  nanobot:
    emoji: 🚀
    category: data-gathering
    tags: [web, scraping, product-hunt, data]
---

## Product Hunt Daily Scrape

This skill scrapes the Product Hunt daily page and extracts key information about the top products.

**Instructions:**

1.  **Access Product Hunt:** Navigate to the Product Hunt daily page: `https://www.producthunt.com/`.
2.  **Identify Product Listings:** Locate the product listings on the page. These are typically displayed in a card-like format.
3.  **Extract Data:** For each product listing, extract the following information:
    *   **Product Name:** The name of the product.
    *   **Product Description:** A short description of the product.
    *   **Number of Upvotes:** The number of upvotes the product has received.
    *   **URL:** The URL of the product's page on Product Hunt.
    *   **Maker:** The name of the product's creator/company.
4.  **Format Output:** Structure the extracted data into a list of dictionaries (or similar data structure). Each dictionary should represent a single product and contain the extracted information.
5.  **Return Results:** Return the list of product dictionaries.

**Example Output:**

```json
[
  {
    "product_name": "Example Product 1",
    "product_description": "A fantastic new tool for...",
    "upvotes": 1234,
    "url": "https://www.producthunt.com/products/example-product-1",
    "maker": "Example Maker"
  },
  {
    "product_name": "Example Product 2",
    "product_description": "Solve your problems with...",
    "upvotes": 5678,
    "url": "https://www.producthunt.com/products/example-product-2",
    "maker": "Another Maker"
  }
]
```

**Error Handling:**

*   If the Product Hunt website is unavailable, return an error message indicating that the website could not be accessed.
*   If the page structure changes significantly, return an error message indicating that the scraping logic needs to be updated.
*   Handle potential errors during data extraction gracefully and log any issues encountered.
```