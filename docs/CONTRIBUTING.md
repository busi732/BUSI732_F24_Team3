# Introduction

This document is meant to provide general guidance on how to contribute to this repository, to maintain legibility, order, efficiency, and accurate tracking of actions performed. 
# Contributing Workflow
The following steps should be adhered to when making a contribution to the repository:
1. Clone the repository and navigate to it by running the following commands:
     ```bash
     git clone https://github.com/busi732/BUSI732_F24_Team3.git
     cd BUSI732_F24_Team3
     ```
2. Create a new branch. Make sure to follow the naming conventions outlined in this document. To create and switch to a new branch:
    ```bash
    git checkout main
    git pull origin main  # Make sure your local 'main' branch is up to date
    git checkout -b <branch-name>
    ```
3. Implement the required changes or improvements in the codebase. Test your changes locally to ensure they work as expected.
4. Stage all changes for commit, and then commit them to the branch:
    ```bash
    git add .
    git commit -m "Clear and concise message here"
5. Push your changes to the remote repository:
    ```bash
    git push origin <branch-name>
    ```
6. Create a pull request (PR) in GitHub by navigating to the remote repository.
  - Click "Compare & Pull Request" to open a new PR.
  - Provide a detailed description of your changes, and make sure to review all changes for correctness.
  - Submit your PR
7. Await PR Review: On a round-robin basis, other Team members will review PRs individually. There will be **two (2)** reviewers per PR.
8. Once the PR has been reviewed and approved, merge the PR with the main branch.
  - Note: Always use the "Squash & Merge" option.
9. After the changes have been merged, delete the branch both locally and remotely.
  - Locally:
  ```bash
  git branch -d <branch-name>
  ```
  - Remotely:
  ```bash
  git push origin --delete <branch-name>
  ```
  
Ensure your local repository remains up-to-date:
```bash
git checkout main
git pull origin main
```

# Branch Naming Conventions

## General Guidelines
- **Use lowercase letters:** Branch names should be in lowercase to maintain consistency and avoid confusion (e.g., `feature/login-page` rather than `Feature/Login-Page`).
- **Use hyphens to separate words:** Separate words with hyphens (`-`) instead of underscores (`_`) or camelCase (e.g., `bugfix/user-login` rather than `bugfix/user_login` or `BugFixUserLogin`).
- **Be descriptive and concise:** The branch name should clearly indicate the purpose of the branch. Avoid vague or overly general names.
- **Avoid special characters:** Do not use special characters such as spaces, slashes (other than `/`), or other punctuation marks in the branch name.
- **Use forward slashes to denote hierarchy:** Branch names should use slashes (`/`) to create a clear hierarchy (e.g., `feature/login-page`, `bugfix/checkout-error`).

## Branch Type Prefixes
Branch names should start with a specific type prefix to indicate the purpose of the branch. The prefix helps distinguish between different kinds of work and assists with organizing branches in the repository.

### Common Prefixes:
`feature/`
- For new features or enhancements.

`bugfix/`
- For bug fixes or issue resolutions.

`hotfix/`
- For critical fixes that need to be applied immediately to the production environment.

`chore/`
- For routine maintenance tasks, such as refactoring, cleaning up code, or updating dependencies.

`test/`
- For testing purposes or experimenting with new code that is not yet ready for production.

`docs/`
- For updates to documentation files (README, Wiki, etc.).

`refactor/`
- For non-functional changes to the codebase that improve structure, readability, or performance but do not add new features or fix bugs.

`wip/` (Work in Progress)
- Indicate that the branch is a work in progress, and the changes are not yet ready for merging.

### General Tips
- If applicable, it’s helpful to include the issue or ticket number in the branch name. This provides a direct link between the code change and the tracking system.
- Always use Pull Requests (PRs) for merging branches. When naming your PRs, try to follow the same convention as your branch names for consistency.
- Branch names should generally be short, ideally under 50 characters.
