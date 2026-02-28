```skill
---
name: pypi-release-publish
description: Publishes a Python package to the Python Package Index (PyPI).
metadata:
  nanobot:
    emoji: 🚀
    category: deployment
    tags: [python, pypi, release, package]
  dependencies: []
---

## Skill: pypi-release-publish

This skill automates the process of publishing a Python package to PyPI.  It assumes the package is already built and ready for distribution.

**Instructions:**

1.  **Locate the `setup.py` file:** The nanobot will search the current directory and its subdirectories for a `setup.py` file. This file contains the package metadata (name, version, description, etc.).
2.  **Verify Package Information:** The nanobot will parse the `setup.py` file to extract the package name and version.  It will confirm that these values are valid.
3.  **Authenticate with PyPI:** The nanobot will attempt to authenticate with PyPI using environment variables. It expects the following environment variables to be set:
    *   `PYPI_USERNAME`: Your PyPI username.
    *   `PYPI_PASSWORD`: Your PyPI password or API token.
    If these are not set, the nanobot will report an authentication error and halt.
4.  **Build Distribution Packages:** The nanobot will use `setuptools` to build distribution packages (wheel and source distribution) using the command `python setup.py sdist bdist_wheel`.
5.  **Publish to PyPI:** The nanobot will use `twine` to upload the distribution packages to PyPI using the command `twine upload dist/*`.
6.  **Confirmation:** Upon successful publication, the nanobot will report a success message including the package name and version. If any errors occur during the process, the nanobot will report the error message and halt.

**Error Handling:**

*   **`setup.py` not found:**  If a `setup.py` file cannot be found, the nanobot will report an error.
*   **Authentication Failure:** If authentication with PyPI fails (due to incorrect username/password or missing environment variables), the nanobot will report an error.
*   **Build Failure:** If the package build process fails, the nanobot will report the error message.
*   **Upload Failure:** If the upload to PyPI fails, the nanobot will report the error message.

**Important Considerations:**

*   **Security:**  Storing your PyPI credentials directly in the environment is generally not recommended for production environments. Consider using a secrets management solution.
*   **Version Control:** Ensure your version control system is properly configured before publishing.
*   **Testing:** Thoroughly test your package before publishing to PyPI.
*   **`twine` Installation:** The nanobot assumes `twine` is installed. If not, the build process will fail.
*   **`setuptools` Installation:** The nanobot assumes `setuptools` is installed. If not, the build process will fail.
```