```skill
---
name: graphql-introspection
description: Queries a GraphQL endpoint to discover its schema and available operations.
metadata:
  nanobot:
    emoji: 🔍
    category: data-analysis
    tags: [graphql, schema, introspection, data]
  dependencies: []
---

## Skill: graphql-introspection

This skill allows the nanobot to query a GraphQL endpoint and retrieve its schema. This schema information can then be used for further analysis, planning, or interaction with the GraphQL API.

**Instructions:**

1.  **Identify the GraphQL Endpoint:** Determine the URL of the GraphQL endpoint you wish to introspect. This will be provided as input.
2.  **Construct the Introspection Query:** The nanobot will automatically construct a standard GraphQL introspection query. This query requests the `__schema` object, which contains information about all types, fields, directives, and queries available in the schema.
3.  **Execute the Query:** Send the introspection query to the specified GraphQL endpoint.
4.  **Parse the Response:** Parse the JSON response from the GraphQL server.
5.  **Extract Schema Information:** Extract the relevant schema information from the parsed response. This includes:
    *   Types (e.g., Query, Mutation, Subscription, custom types)
    *   Fields for each type
    *   Arguments for each field
    *   Directives
    *   Query type
    *   Mutation type
    *   Subscription type
6.  **Return Schema Data:** Return the extracted schema data in a structured format (e.g., a JSON object or a dictionary).  The format should be easily parsable by other nanobot skills.  Consider returning a simplified representation if the full schema is too large.

**Input:**

*   `graphql_endpoint` (string): The URL of the GraphQL endpoint to introspect.  Example: `https://example.com/graphql`

**Output:**

*   A JSON object representing the GraphQL schema.  The structure of this object will depend on the specific implementation, but should include information about types, fields, and directives.  If the introspection query fails, return an error message.

**Error Handling:**

*   If the GraphQL endpoint is unreachable, return an error message indicating a network error.
*   If the GraphQL server returns an error, return the error message from the server.
*   If the introspection query fails to parse, return an error message indicating a parsing error.
```