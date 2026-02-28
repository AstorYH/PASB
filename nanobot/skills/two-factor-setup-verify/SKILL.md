```skill
---
name: two-factor-setup-verify
description: Verifies the successful setup of two-factor authentication on a target system.
metadata:
  nanobot:
    emoji: ✅
    category: security
    tags: [authentication, verification, two-factor]
---

## Two-Factor Setup Verify

This skill checks if two-factor authentication (2FA) is enabled and functioning correctly on a specified target system.  It attempts to trigger a 2FA challenge and verifies that a challenge is received and can be satisfied.

**Instructions:**

1.  **Identify Target:** Determine the system or account you want to verify. This could be a user account on a website, a service account, or a device.  The target needs to have a known 2FA mechanism (e.g., SMS, authenticator app, email).
2.  **Initiate 2FA Challenge:**  Attempt to trigger a 2FA challenge. This usually involves logging in and attempting an action that requires 2FA (e.g., changing a password, accessing a sensitive resource).  The method for triggering the challenge is highly dependent on the target system.  Look for options like "Login with 2FA," "Verify Account," or similar prompts.
3.  **Monitor for Challenge:**  Monitor the expected channels for the 2FA challenge. This could be:
    *   **SMS:** Check the mobile device associated with the account for an SMS message containing a code.
    *   **Authenticator App:** Open the authenticator app (e.g., Google Authenticator, Authy) and look for a code generated for the target account.
    *   **Email:** Check the email inbox associated with the account for an email containing a verification code.
4.  **Verify Challenge Received:** Confirm that a 2FA challenge was successfully received.  If no challenge is received within a reasonable timeframe (e.g., 60 seconds), the 2FA setup is likely incomplete or malfunctioning.  Report failure.
5.  **Satisfy Challenge (Simulated):**  Since we cannot directly input the code, *simulate* the successful satisfaction of the challenge.  Assume the code was correctly entered and the system accepted it.  This is a verification of the *process*, not the code itself.
6.  **Check for Successful Verification:** Observe the system's response after the simulated challenge satisfaction.  A successful verification will typically result in access being granted or the action being completed.
7.  **Report Result:**  Report whether the 2FA setup appears to be functioning correctly based on the observed system response.

**Success Criteria:**

*   A 2FA challenge is received within a reasonable timeframe.
*   The system indicates successful verification after the simulated challenge satisfaction.

**Failure Criteria:**

*   No 2FA challenge is received within a reasonable timeframe.
*   The system indicates a failed verification or an error related to 2FA.
*   The target system does not support 2FA.

**Notes:**

*   This skill *simulates* the verification process. It does not actually validate the security of the 2FA codes themselves.
*   The specific steps for triggering and verifying the 2FA challenge will vary depending on the target system.
*   Consider the potential for rate limiting or account lockout if the challenge is triggered repeatedly.
```