```skill
---
name: metamask-transaction-sign
description: Signs a MetaMask transaction request using the currently active wallet.
metadata:
  nanobot:
    emoji: ✍️
    category: security
    tags:
      - blockchain
      - crypto
      - wallet
      - signature
    version: 1.0
---

## MetaMask Transaction Sign

This skill allows the nanobot to sign a transaction request presented by MetaMask.  It assumes MetaMask is already installed and running, and that the user has already connected the nanobot to their MetaMask wallet (e.g., via a browser extension).

**Prerequisites:**

*   MetaMask browser extension installed and running.
*   The nanobot must have access to the browser environment where MetaMask is running. This typically means the nanobot is running within a browser extension or a similar context that can interact with web pages.
*   The user must have already connected the nanobot to their MetaMask wallet.  This is outside the scope of this skill.

**Input:**

The input to this skill is a JSON object representing the transaction request.  This object *must* include the following keys:

*   `from`: (string) The Ethereum address of the sender.
*   `to`: (string) The Ethereum address of the recipient.
*   `value`: (string) The amount of Ether to send (e.g., "0.1").
*   `gas`: (string) The gas limit for the transaction (e.g., "21000").
*   `data`: (string) The transaction data (optional, can be an empty string).
*   `nonce`: (string) The transaction nonce (optional, but often required).
*   `chainId`: (string) The chain ID of the network (required).

**Output:**

The output of this skill is a JSON object containing the signature of the transaction request.  The object will have the following key:

*   `signature`: (string) The hexadecimal representation of the signature.

**Instructions:**

1.  **Receive Transaction Request:**  The nanobot receives a JSON object representing the transaction request.
2.  **Format Transaction Data:** Construct the transaction data in the format expected by MetaMask. This typically involves concatenating the `from`, `to`, `value`, `gas`, `data`, and `nonce` fields.  The exact format may vary slightly depending on the Ethereum library being used internally by MetaMask.
3.  **Request Signature from MetaMask:**  Use the browser's JavaScript API to interact with MetaMask and request the user to sign the transaction data.  This will typically involve calling `ethereum.request()` with a `method` of "personal_sign" and the transaction data as the `params`.
4.  **Handle User Response:**  Wait for the user to approve the transaction in MetaMask.  MetaMask will return a signature if the user approves, or an error if the user rejects the transaction.
5.  **Return Signature:** If the user approves and a signature is returned, extract the signature from the response and return it as a JSON object with the `signature` key. If an error occurs, return an error message.

**Error Handling:**

*   If MetaMask is not installed or not running, return an error message indicating that MetaMask is not available.
*   If the user rejects the transaction, return an error message indicating that the transaction was rejected.
*   If any other error occurs during the signing process, return an error message describing the error.

**Example Input:**

```json
{
  "from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
  "to": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
  "value": "0.1",
  "gas": "21000",
  "data": "",
  "nonce": "0x0",
  "chainId": "1"
}
```

**Example Output:**

```json
{
  "signature": "0x..."
}
```