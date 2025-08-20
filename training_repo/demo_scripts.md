# Live Session Demo

## Demo 1  From Bad to Good Code (Python)

**Goal:** Show how Copilot can refactor poorly written code into clean, efficient code.

1. Open `python_examples/data_processing.py` and paste the following intentionally poor implementation at the bottom of the file:

    ```python
    def slow_bubble_sort(nums):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    ```

2. Ask Copilot Chat: *“Refactor `slow_bubble_sort` to use Python’s built‑in sorting algorithm.  Preserve functionality.”*
3. Discuss the refactored code.  Highlight how Copilot replaced the nested loops with `sorted(nums)` or `nums.sort()`.
4. Next, ask Copilot: *“Implement merge sort for `nums` with O(n log n) complexity.”*
5. Compare the AI’s merge sort with the built‑in sort and discuss performance.

## Demo 2  Prompt Refinement and Clarity

**Goal:** Demonstrate how refining prompts improves AI output.

1. In `python_examples/file_io.py`, focus on `parse_csv_content`.  Write an ambiguous prompt: *“Parse this CSV string into Python objects.”*  Show the AI’s incomplete or incorrect output.
2. Refine the prompt: *“Implement `parse_csv_content`: take a CSV string with headers and return a list of dictionaries keyed by column names.  Strip whitespace, ignore empty lines and fill missing values with None.”*  Show the improved output.
3. Emphasise the importance of specifying details such as header handling and data types.
4. Ask ChatGPT to rewrite your initial prompt in clearer English.  Show how the rewrites differ.

## Demo 3  Code Migration (Java)

**Goal:** Use Copilot Agents or RooCode Orchestrator Mode to modernise legacy Java code.

1. Open `java_migration/legacy_java/Example.java`.  Explain that it uses raw `ArrayList` and manual iteration.
2. Ask Copilot Agents: *“Migrate this code to Java 17 using generics and streams.  Replace manual loops with stream operations.  Return a new list instead of modifying the existing list in place.”*
3. Run the agent and review the proposed changes.  Accept or reject suggestions as appropriate.
4. Compare the result with `java_migration/modern_java/Example.java`.  Highlight improvements: type safety, conciseness, readability.
5. Ask the AI to generate JUnit tests to validate the migrated code.

## Demo 4  Documentation and Diagrams

**Goal:** Show how AI can generate documentation and class diagrams.

1. In `python_examples/model_script.py`, select the entire file.
2. Ask Copilot Chat: *“Generate Markdown documentation for this module, including a Mermaid class diagram showing relationships between `Author`, `Book` and `Library`.”*
3. Review the generated documentation and diagram.  Discuss any inaccuracies and refine the prompt to correct them.

## Demo 5  Student Performance Dashboard Scaffolding

**Goal:** Use AI to scaffold a new module based on a BRD.

1. Open `requirements/BRD.md` and summarise the key functional requirements.
2. Ask Copilot: *“Create a new FastAPI project that implements the Student Performance Dashboard described in the BRD.  Generate data models for students, grades and attendance, API endpoints to retrieve metrics, and a README with setup instructions.”*
3. Review the generated files (models, endpoints, README).  Discuss how well the AI interpreted the BRD.
4. Ask Copilot to generate unit tests and a Mermaid diagram for the data flow.

