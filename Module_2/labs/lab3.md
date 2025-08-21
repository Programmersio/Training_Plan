# Lab 3 – Prompt Engineering Drills

## Duration

**Estimated time:** 50–60 minutes.

## Objectives

This lab develops your prompt engineering skills.  You will practice writing detailed instructions for AI models, specifying inputs, outputs and algorithms, and iterating based on the results.  You will also experiment with documentation and diagram generation to accompany your code.

## Prerequisites                                            

- Completion of Lab 1 and Lab 2.
- Understanding of basic data structures and algorithms (binary search, grouping functions).
- The training repository open in VS Code.

## Step‑By‑Step Instructions

### 1. Implement binary search with a prompt

1. In any Python file, write a comment describing the following task:

   > *Act as a senior Python developer.  Implement a function `binary_search(nums: list[int], target: int) -> int` that returns the index of `target` in the sorted list `nums`, or `-1` if not found.  Use a binary search algorithm with O(log n) time complexity.  Include type hints and docstrings.  Handle empty lists by returning -1.*

2. Hit **Enter** to trigger Copilot (or Roo Code).  Review the generated code and ensure it uses a proper binary search loop with low/high pointers.
3. Accept or refine the implementation until it matches the requirements.

### 2. Group scores by grade

1. Open **`python_examples/data_processing.py`** again.  At the bottom, create a new function `group_by_grade`.
2. Write a prompt specifying the task:

   > *Group numeric scores into letter grades (A 90–100, B 80–89, C 70–79, D 60–69, F < 60) and return a dictionary mapping each grade to its list of scores.  Exclude empty grade categories.  Include a docstring and type hints.*

3. Generate the code and verify that it iterates through the list, assigns each score to the correct bucket, and omits empty lists from the output.
4. Optional: Modify the prompt to add a separate category for perfect scores (100) or adjust the boundaries.  Observe how the output changes.

### 3. Generate documentation and diagrams

1. Open **`python_examples/model_script.py`**, which defines the classes `Author`, `Book` and `Library`.
2. Use Copilot or Roo Code to generate Markdown documentation and a Mermaid diagram:

   - Write a prompt: *“Generate Markdown documentation for the classes `Author`, `Book` and `Library`.  Include a summary of each class and a Mermaid diagram showing the relationships.  Use nodes for the classes and arrows for references.”*
   - Accept the generated output and copy it into a new file (`docs/models.md`).
3. Inspect the diagram text (e.g. `graph TD; Author-->Book; Book-->Library`) and preview it in a Mermaid renderer if desired.

### 4. Create a README for the Student Performance Dashboard

1. Open **`requirements/BRD.md`**, which contains a business requirements document for the Student Performance Dashboard.
2. Write a prompt: *“Create a README for the Student Performance Dashboard.  Summarise the project, list setup instructions, describe the API endpoints and include a simple Mermaid diagram showing the data flow from ingestion to report generation.”*
3. Run the prompt using Copilot Chat or Roo Code.  Review the generated README and commit it to `README.md` in the repository.

## Reflection Questions

1. How did defining roles (e.g. “senior Python developer”) influence the results?
2. What additional detail improved the accuracy of the binary search implementation?
3. When generating documentation, how specific did your prompt need to be to produce a useful diagram?

## Expected Outcomes

Upon finishing this lab you will:

- Be able to write precise prompts that specify algorithms, constraints and outputs.
- Implement functions such as binary search and group_by_grade using AI assistance.
- Generate Markdown documentation and Mermaid diagrams from code and business requirements.
