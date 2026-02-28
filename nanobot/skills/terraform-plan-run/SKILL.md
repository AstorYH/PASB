```skill
---
name: terraform-plan-run
description: Executes a Terraform plan to preview infrastructure changes.
metadata:
  nanobot:
    emoji: 🚀
    category: infrastructure
    tags: [terraform, infrastructure, planning, preview]
---

## Terraform Plan Run

This skill executes a Terraform plan to preview infrastructure changes.  It assumes a Terraform project is already set up and initialized.

**Instructions:**

1.  **Navigate to the Terraform Project Directory:**  The nanobot must first navigate to the directory containing the Terraform configuration files (e.g., `main.tf`, `variables.tf`, `outputs.tf`).  Use the `cd` command to change the current working directory.  The path to the directory will be provided as an input parameter.

2.  **Initialize Terraform (if necessary):** Check if Terraform is initialized. If not, run `terraform init`.  This downloads necessary providers and modules.  This step is optional and can be controlled by an input parameter.

3.  **Run Terraform Plan:** Execute the `terraform plan` command. This command generates an execution plan, showing the changes that Terraform will make to the infrastructure.

4.  **Output the Plan:** Capture the output of the `terraform plan` command. This output will contain a detailed description of the proposed changes.  Present this output to the user.

**Input Parameters:**

*   `terraform_directory` (string, required): The absolute path to the Terraform project directory.  Example: `/home/user/terraform/my-project`
*   `init` (boolean, optional, default: `false`): Whether to run `terraform init` before running the plan.  Set to `true` if the project hasn't been initialized or if you want to ensure it's up-to-date.

**Output:**

*   `plan_output` (string): The complete output of the `terraform plan` command.  This will include a summary of the changes, as well as detailed descriptions of each resource that will be added, modified, or destroyed.

**Error Handling:**

*   If the `terraform_directory` does not exist, return an error indicating that the directory could not be found.
*   If the `terraform plan` command fails (e.g., due to syntax errors in the Terraform configuration), capture the error message and return it to the user.
*   If `terraform init` fails, return an error indicating the initialization failed.

**Example:**

```
Input:
  terraform_directory: /home/user/terraform/my-project
  init: true

Execution:
  cd /home/user/terraform/my-project
  terraform init
  terraform plan

Output:
  plan_output: "...\n+ resource "aws_instance" "example" {...\n...\n"
```
```