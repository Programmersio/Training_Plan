# Lab 2 – Refactoring with Roo Code

## Objectives

This lab focuses on using the **Roo Code** extension to perform large‑scale refactorings across your repository.  You will practice indexing the project, running agentic tasks to rename symbols, merge duplicate code and split long methods, and using Ask mode to understand complex logic.  After completing this lab you should be able to orchestrate non‑trivial changes while retaining control over the edits.

## Prerequisites

- Visual Studio Code with the Roo Code extension installed and configured to use your organisation’s preferred model (e.g. Azure OpenAI or a local LLM via Ollama).
- The training repository indexed by Roo Code.  Run **`Roo Code: Index Workspace`** once the project is open.
- Familiarity with C# classes and methods if you choose to tackle the optional C# exercise.

## Step‑By‑Step Instructions

### 1. Rename a class across the repository

1. In your Python workspace, open `python_examples/invoice_utils.py` or `python_examples/customer_utils.py`. Both contain example classes (`InvoiceAdd` and `Customer`).
2. To practice class renaming (e.g., `InvoiceAdd` to `InvoiceAddRefactored` or `Customer` to `CustomerProfile`):
   - Open the Command Palette (`Ctrl+Shift+P`) and choose **"Roo Code: New Task"**.
   
   **⚠️ Token Cost Optimization:** Choose between these prompt approaches:
   
   **Original prompt (less efficient - may result in step-by-step confirmations):**
   - *"Rename the class `InvoiceAdd` to `InvoiceAddRefactored` (or `Customer` to `CustomerProfile`) in the entire repository. Update imports and usages accordingly."*
   
   **Optimized prompt (more efficient - reduces token consumption by 50-70%):**
   - *"Rename the class `InvoiceAdd` to `InvoiceAddRefactored` in the entire repository. Update imports and usages accordingly. Please batch all changes and complete the task efficiently without asking for confirmation on each step."*
   
   - Roo Code will propose a plan and identify affected files. Review the plan, then accept changes after verifying the diff.
   - **Note:** The optimized prompt should reduce API costs significantly by minimizing interactive confirmations.

### 2. Merge duplicate functions

1. In `python_examples/invoice_utils.py`, you will find two nearly identical functions: `processLineItem1` and `processLineItem2`.
2. In `python_examples/customer_utils.py`, you will find two more: `duplicate_logic_a` and `duplicate_logic_b`.
3. Highlight both functions (or open them side by side) and run **"Roo Code: New Task"**.

   **⚠️ Token Cost Optimization:** Choose between these prompt approaches:
   
   **Original prompt (less efficient - may require 5-6 separate operations):**
   - *"Merge `processLineItem1` and `processLineItem2` into a single function called `processLineItem`. Remove duplication and update calls accordingly."*
   
   **Optimized prompt (more efficient - reduces token consumption by ~60%):**
   - *"In the training_repo/ directory: Merge processLineItem1 and processLineItem2 from python_examples/invoice_utils.py into a single processLineItem function. Read both invoice_utils.py and tests/test_invoice_utils.py, perform the complete refactoring (merge functions + update imports/calls), then verify with pytest tests/test_invoice_utils.py. Complete all changes in minimal operations without individual confirmations."*
   
   **Key optimizations in the improved prompt:**
   - **Specific Repository Path**: `training_repo/` - eliminates search step
   - **Exact File Locations**: `python_examples/invoice_utils.py` and `tests/test_invoice_utils.py`
   - **Batch File Reading**: Read both files upfront in single operation
   - **Combined Operations**: Merge functions AND update tests in same workflow
   - **Built-in Verification**: Include test execution as final validation step
   - **Clear Scope Boundary**: Only run relevant tests (`tests/test_invoice_utils.py`)
   
4. Review the proposed changes. Ensure that parameters and return values are consistent and tests still pass (see `tests/test_invoice_utils.py` and `tests/test_customer_utils.py`).
   - **Note:** The optimized prompt should reduce step-by-step confirmations and API costs.

### 3. Refactor a long method

1. In `python_examples/customer_utils.py`, locate the function `long_function` (a stand-in for a long method).
2. Highlight the function and run **"Roo Code: New Task"**.

   **⚠️ Token Cost Optimization:** Choose between these prompt approaches:
   
   **Original prompt (less efficient - may require multiple iterations):**
   - *"Split this function into smaller, readable helpers. Each helper should have a descriptive name. Encapsulate repeated logic if present."*
   
   **Optimized prompt (more efficient - reduces token consumption by ~65%):**
   - *"In training_repo/python_examples/customer_utils.py: Split the long_function() into smaller, readable helper functions with descriptive names. Analyze the repeated loop patterns, create a generic helper for weighted sum calculations, then create specific segment helpers for each range. Encapsulate any duplicate logic found elsewhere in the file. Complete all refactoring in a single operation without step-by-step confirmations."*
   
   **Key optimizations in the improved prompt:**
   - **Specific File Path**: `training_repo/python_examples/customer_utils.py` - eliminates file search
   - **Exact Function Target**: `long_function()` - direct function identification
   - **Detailed Refactoring Strategy**: Mentions loop patterns, weighted sums, segment helpers
   - **Scope Extension**: Include duplicate logic cleanup in same operation
   - **Single Operation Request**: Prevents multiple confirmation rounds

3. Review Roo Code's plan. If the function is deeply coupled, you might need to iterate. Accept the changes once the refactoring meets your criteria for readability and maintainability.
   - **Note:** The optimized prompt should significantly reduce interactive confirmations and API costs by providing clear, specific instructions.

### 4. Use Ask mode for analysis

1. Select a complex piece of code (e.g. the refactored `processLineItem` or `long_function`).
2. Activate **"Roo Code: Explain Code"** (Ctrl+Shift+P → Explain Code).

   **⚠️ Token Cost Optimization:** Choose between these prompt approaches:
   
   **Original prompt (less efficient - may require follow-up questions):**
   - *"Explain what this function does, including its inputs, outputs and error cases."*
   
   **Optimized prompt (more efficient - reduces token consumption by ~55%):**
   - *"Analyze the long_function() in training_repo/python_examples/customer_utils.py: Provide a comprehensive explanation covering: 1) Function purpose and algorithm, 2) Input parameters (if any) and their types/constraints, 3) Return value type and expected output, 4) Potential error cases or edge conditions, 5) Implementation details of helper functions, 6) Performance characteristics. Include specific examples and calculations where applicable."*
   
   **Key optimizations in the improved prompt:**
   - **Specific Function Target**: `long_function()` in exact file path
   - **Structured Analysis Request**: 6-point comprehensive breakdown
   - **Detailed Scope**: Algorithm, types, examples, calculations, performance
   - **Prevents Follow-ups**: Covers common follow-up questions upfront
   - **Helper Function Analysis**: Includes refactored components

3. Read the generated explanation. If necessary, follow up with questions such as *"How could this be improved?"* or *"Are there any potential bugs or edge cases?"*
   - **Note:** The optimized prompt should provide more comprehensive analysis in a single response, reducing need for multiple follow-up questions.
   
**Other useful Roo Code commands you may see:**
- **Roo Code: Fix Code** – Use to automatically fix detected issues in the selected code.
- **Roo Code: Improve Code** – Use to refactor or enhance code quality in the selected region.

## Reflection Questions

1. How does Roo Code’s indexing enable repository‑wide refactorings?  What happens if the index is out of date?

   **Answer:**
   Roo Code builds a project-wide index that maps all symbols (classes, functions, variables) and their relationships across every file in your codebase. This index allows Roo Code to:
   - Find all usages and definitions of a symbol, even across many files.
   - Safely rename, merge, or refactor code everywhere it appears, not just in the open file.
   - Propose accurate, multi-file changes and show you a plan before applying edits.

   If the index is out of date (for example, after you add, remove, or rename files or symbols), Roo Code may miss some references or new code. This can lead to incomplete or incorrect refactorings. To ensure accuracy, you should always re-index the workspace after large changes or before major refactors. Re-indexing means Roo Code scans all files again and updates its internal map, so it has the latest view of your codebase.

   **How is this different from GitHub Copilot?**
   GitHub Copilot does not build a project-wide index. It only uses the open file and a small window of surrounding code for its suggestions. Copilot cannot track symbol usage or relationships across files, so it cannot perform safe, repository-wide refactorings. Roo Code’s indexing is what enables it to coordinate and update code everywhere, while Copilot is limited to local, context-based completions.
2. When would you prefer Roo Code over Copilot for code modification tasks?
3. Did Roo Code’s agentic actions produce accurate edits?  What manual checks did you perform before accepting changes?

## Expected Outcomes

After completing this lab you will:

- Know how to index a workspace and verify Roo Code’s index status.
- Perform repository‑wide refactors (renaming classes, merging functions, splitting long methods) with Roo Code.
- Use Ask mode to analyse and explain complex functions.
