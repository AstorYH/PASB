```skill
---
name: profile-avatar-update
description: Updates the user's profile avatar to a specified image.
metadata:
  nanobot:
    emoji: 👤
    category: communication
    tags: [profile, avatar, image, update]
---

## Profile Avatar Update

This skill allows you to update your profile avatar.  The nanobot will attempt to locate and apply the provided image to your profile.

**Instructions:**

1.  **Image Identification:** The nanobot requires a clear identifier for the image you wish to use as your avatar. This can be:
    *   **File Path:**  If the image is stored locally, provide the full or relative path to the image file (e.g., `/home/user/images/avatar.png` or `images/avatar.jpg`).
    *   **URL:** If the image is hosted online, provide the full URL to the image (e.g., `https://example.com/avatars/my_avatar.png`).
    *   **Image Data (Base64):**  Provide the image data encoded in Base64 format.  This is less common but allows for direct image inclusion.  (e.g., `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+n9...`).

2.  **Profile Target:** Specify which profile you are updating.  If you have only one profile, the nanobot will assume it's your primary profile.  If you have multiple profiles (e.g., on different platforms), specify the profile identifier (e.g., "LinkedIn Profile", "Twitter Profile", "Work Profile").

3.  **Confirmation:** The nanobot will attempt to retrieve the image and update the profile.  It will provide a confirmation message upon successful completion or an error message if the update fails.

**Example Input:**

`Update my profile avatar with https://example.com/avatars/new_avatar.jpg`

`Set LinkedIn Profile avatar to /home/user/pictures/linkedin_avatar.png`

`Update profile avatar using data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w+n9...`

**Error Handling:**

*   **Invalid Image Identifier:** If the provided file path, URL, or Base64 data is invalid or inaccessible, the nanobot will report an error.
*   **Profile Not Found:** If the specified profile does not exist, the nanobot will report an error.
*   **Permission Denied:** If the nanobot lacks the necessary permissions to update the profile, it will report an error.
*   **Image Format Not Supported:** The nanobot may only support certain image formats (e.g., PNG, JPG, GIF). Unsupported formats will result in an error.
```