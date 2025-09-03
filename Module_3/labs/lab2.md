# Lab 2 – Manual & Peer Code Review

## Objectives

This lab emphasises the human element of code quality.  You will practise conducting a manual review of AI‑generated code, either alone or with a peer.  The goal is to identify logic errors, style issues, maintainability concerns and security risks that automated tools might miss.  You will also learn how to communicate constructive feedback and iterate on the code based on review comments.

## Prerequisites

* Git installed and configured on your machine.
* The training repository cloned locally and a remote repository or collaboration platform (e.g. GitHub or Azure DevOps) set up for pull requests.
* Completion of Module 2 or equivalent experience generating code with Copilot or Roo Code.

## Step‑By‑Step Instructions

### 1. Prepare a feature branch

1. Choose a feature to implement or refine.  For example, complete the `Library` class in `python_examples/model_script.py` or refactor a function you generated in Lab 1.
2. Create a new Git branch for your changes: `git checkout -b feature/code‑review‑exercise`.
3. Use Copilot or Roo Code to generate the implementation.  Make sure to commit your work with a clear commit message, e.g. `git commit -am "Add initial Library implementation"`.

### 2. Open a pull request

1. Push your branch to your remote repository: `git push origin feature/code‑review‑exercise`.
2. Open a pull request (PR) or merge request on your platform.  Include a description of the feature and any relevant context or constraints.

### 3. Conduct the review

1. **Assign a reviewer.**  If working with a colleague, ask them to review your PR.  Otherwise, simulate the process yourself by viewing the diff and adding comments.
2. **Review for correctness.**  Check that the code meets the requirements, handles edge cases and contains appropriate error handling.
3. **Review for readability.**  Evaluate naming, formatting, structure and consistency with the project’s style guide.  Consider whether the code could be simplified or decomposed into smaller functions.
4. **Review for security.**  Look for missing input validation, hard‑coded secrets, unsafe file operations and insecure dependencies.  Refer to the vulnerabilities list in the training pack【846912144979599†L188-L201】【846912144979599†L247-L256】.
5. **Add comments.**  Use line‑level comments to suggest improvements.  Be specific and constructive.  For example, ask questions (“Should this be parameterised?”) or propose refactoring (“Consider extracting this loop into a helper function”).

### 4. Address feedback and iterate

1. Respond to each comment in the PR.  If you agree with the feedback, make the requested changes and push an update to your branch.
2. If you disagree, explain your rationale and discuss with the reviewer.  You may need to adjust your approach or refine the AI prompt to generate a better solution.
3. Repeat the review cycle until the code meets quality standards and all comments are resolved.

### 5. Merge and clean up

1. Once approved, merge the PR into the main branch.  Squash commits if appropriate and delete the feature branch.
2. Reflect on the review process.  Consider what issues you found manually versus those caught by static analysis or tests.

## Reflection Questions

1. What types of issues did you or your reviewer identify that automated tools had not flagged?  How did you address them?
2. Did the AI‑generated code follow your project’s style guidelines?  If not, what specific improvements did you make?
3. How did collaborating with a peer influence the quality of the final code?  What communication strategies were most effective?

## Expected Outcomes

By completing this lab you will:

* Gain experience using pull requests and diffs to organise and discuss changes.
* Develop a critical eye for logic, style and security issues in AI‑generated code.
* Practise giving and receiving constructive feedback and iterating on code accordingly.
* Understand how manual review complements static analysis and testing.