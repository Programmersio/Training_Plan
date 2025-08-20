# Lab 2 – Refactoring with Roo Code

## Objectives

This lab focuses on using the **Roo Code** extension to perform large‑scale refactorings across your repository.  You will practice indexing the project, running agentic tasks to rename symbols, merge duplicate code and split long methods, and using Ask mode to understand complex logic.  After completing this lab you should be able to orchestrate non‑trivial changes while retaining control over the edits.

## Prerequisites

- Visual Studio Code with the Roo Code extension installed and configured to use your organisation’s preferred model (e.g. Azure OpenAI or a local LLM via Ollama).
- The training repository indexed by Roo Code.  Run **`Roo Code: Index Workspace`** once the project is open.
- Familiarity with C# classes and methods if you choose to tackle the optional C# exercise.

## Step‑By‑Step Instructions

### 1. Rename a class across the repository

1. In your Python workspace, assume there is a class called `InvoiceAdd` used throughout the codebase.  To rename it to `InvoiceAddRefactored` across all files:
   - Open the Command Palette (`Ctrl+Shift+P`) and choose **“Roo Code: Run”**.
   - When prompted, describe the task: *“Rename the class `InvoiceAdd` to `InvoiceAddRefactored` in the entire repository.  Update imports and usages accordingly.”*
   - Roo Code will propose a plan and identify affected files.  Review the plan, then accept changes after verifying the diff.

### 2. Merge duplicate functions

1. Suppose there are two functions, `processLineItem1` and `processLineItem2`, which contain nearly identical code.  Highlight both functions (or open them side by side) and run **“Roo Code: Run”**.
2. Provide a prompt: *“Merge `processLineItem1` and `processLineItem2` into a single function called `processLineItem`.  Remove duplication and update calls accordingly.”*
3. Review the proposed changes.  Ensure that parameters and return values are consistent and tests still pass.

### 3. Refactor a long method

1. In a C# file (optional for Python learners), identify the 500‑line method `AddNoise` in `noise_handler.cs`.
2. Highlight the method and run **“Roo Code: Run”** with the prompt: *“Split this method into smaller, readable functions.  Each helper should have a descriptive name.  Encapsulate repeated logic into private methods or a separate class.”*
3. Review Roo Code’s plan.  If the method is deeply coupled, you might need to iterate.  Accept the changes once the refactoring meets your criteria for readability and maintainability.

### 4. Use Ask mode for analysis

1. Select a complex piece of code (e.g. the refactored `processLineItem` function).
2. Activate **“Roo Code: Ask”** (Ctrl+Shift+P → Ask).  Ask: *“Explain what this function does, including its inputs, outputs and error cases.”*
3. Read the generated explanation.  If necessary, follow up with questions such as *“How could this be improved?”* or *“Are there any potential bugs or edge cases?”*

## Reflection Questions

1. How does Roo Code’s indexing enable repository‑wide refactorings?  What happens if the index is out of date?
2. When would you prefer Roo Code over Copilot for code modification tasks?
3. Did Roo Code’s agentic actions produce accurate edits?  What manual checks did you perform before accepting changes?

## Expected Outcomes

After completing this lab you will:

- Know how to index a workspace and verify Roo Code’s index status.
- Perform repository‑wide refactors (renaming classes, merging functions, splitting long methods) with Roo Code.
- Use Ask mode to analyse and explain complex functions.
