```skill
---
name: soap-request-formatter
description: Formats unstructured data into a valid SOAP request string.
metadata:
  nanobot:
    emoji: 🧼
    version: 1.0
    category: communication
    tags: [soap, request, formatting, xml]
---

## Skill Instructions

This skill takes unstructured data and transforms it into a properly formatted SOAP request string.  The input will be a dictionary-like structure representing the data to be included in the SOAP request.  You must construct a valid XML string adhering to basic SOAP envelope, header (optional), and body structure.

**Input:**

A dictionary containing the data for the SOAP request.  The dictionary will have the following keys (though not all may be present):

*   `soapAction`: (string) The SOAP action to include in the request.  This is *required*.
*   `header`: (dictionary, optional) A dictionary containing key-value pairs for the SOAP header.  If not provided, omit the header section.
*   `body`: (string) The XML content for the SOAP body.  This is *required*.

**Output:**

A string containing the complete, formatted SOAP request.

**Formatting Rules:**

1.  **Envelope:** The request *must* be enclosed within a `<soapenv:Envelope>` tag.  Assume `xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"`.
2.  **Header (Optional):** If a `header` dictionary is provided in the input, create a `<soapenv:Header>` section.  For each key-value pair in the `header` dictionary, create a corresponding XML element within the header.  For example, if `header = {"To": "http://example.com", "From": "nanobot@example.com"}` then the header section should be:

    ```xml
    <soapenv:Header>
      <To>http://example.com</To>
      <From>nanobot@example.com</From>
    </soapenv:Header>
    ```
3.  **Body:** The `body` string from the input *must* be placed within a `<soapenv:Body>` tag.
4.  **SOAP Action:** The `soapAction` from the input *must* be included in the HTTP headers (not in the XML itself).  This skill does *not* handle HTTP header creation; it only formats the XML.
5.  **XML Validity:** The generated XML *must* be well-formed.  Ensure proper tag nesting and closing.

**Example:**

**Input:**

```python
{
  "soapAction": "http://example.com/soap/action",
  "header": {
    "To": "http://example.com",
    "From": "nanobot@example.com"
  },
  "body": "<ns1:MyRequest xmlns:ns1=\"http://example.com\"><ns1:Parameter>Value</ns1:Parameter></ns1:MyRequest>"
}
```

**Output:**

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <To>http://example.com</To>
    <From>nanobot@example.com</From>
  </soapenv:Header>
  <soapenv:Body>
    <ns1:MyRequest xmlns:ns1="http://example.com">
      <ns1:Parameter>Value</ns1:Parameter>
    </ns1:MyRequest>
  </soapenv:Body>
</soapenv:Envelope>
```

**Error Handling:**

*   If `soapAction` or `body` are missing from the input, return an error message: "Error: Missing required fields (soapAction or body)."
*   If the input is not a dictionary, return an error message: "Error: Input must be a dictionary."
```