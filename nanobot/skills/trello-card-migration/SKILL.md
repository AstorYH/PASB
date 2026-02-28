```skill
---
name: trello-card-migration
description: Migrates a Trello card from one board to another, updating its description and members as needed.
metadata:
  nanobot:
    emoji: 🗃️
    category: data-management
    tags: [trello, migration, board, card]
---

## Trello Card Migration Skill

This skill allows the nanobot to move a Trello card from a source board and list to a destination board and list, optionally updating the card's description and member assignments.

**Input:**

*   `source_board_id`: (string) The ID of the Trello board containing the card to be migrated.
*   `source_list_id`: (string) The ID of the list on the source board where the card currently resides.
*   `destination_board_id`: (string) The ID of the Trello board where the card should be moved.
*   `destination_list_id`: (string) The ID of the list on the destination board where the card should be placed.
*   `new_description`: (string, optional) A new description to set for the card. If omitted, the existing description is preserved.
*   `member_ids`: (list of strings, optional) A list of Trello member IDs to add to the card.  If omitted, existing members are preserved.

**Process:**

1.  **Verify Input:** Ensure all required input parameters (`source_board_id`, `source_list_id`, `destination_board_id`, `destination_list_id`) are provided and are valid Trello IDs.
2.  **Retrieve Card:** Use the `source_board_id` and `source_list_id` to identify and retrieve the Trello card.
3.  **Update Description (Optional):** If `new_description` is provided, update the card's description with the new value.
4.  **Update Members (Optional):** If `member_ids` is provided, add the specified members to the card.
5.  **Move Card:** Move the card from the source list to the destination list on the destination board.
6.  **Confirmation:** Report success or failure, including any error messages encountered.

**Output:**

*   `success`: (boolean) True if the card was successfully migrated, False otherwise.
*   `card_id`: (string) The ID of the migrated card.
*   `message`: (string) A human-readable message indicating the outcome of the operation (e.g., "Card migrated successfully", "Error: Invalid board ID").

**Error Handling:**

*   Handle invalid Trello IDs gracefully, providing informative error messages.
*   Handle cases where the card is not found on the source board or list.
*   Handle errors related to Trello API rate limits.
*   Log all errors for debugging purposes.

**Example:**

```
migrate_trello_card(
  source_board_id="YOUR_SOURCE_BOARD_ID",
  source_list_id="YOUR_SOURCE_LIST_ID",
  destination_board_id="YOUR_DESTINATION_BOARD_ID",
  destination_list_id="YOUR_DESTINATION_LIST_ID",
  new_description="This card has been migrated to a new board.",
  member_ids=["MEMBER_ID_1", "MEMBER_ID_2"]
)
```
```