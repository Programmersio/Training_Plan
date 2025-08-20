# Training Exercises

This document summarises the exercises for the Copilot, RooCode and prompt‑engineering training.  Each exercise references files in this repository.  Follow the instructions in the training plans for detailed guidance on prompt design, algorithm selection and reviewing AI output.

## Exercise 1  Calculate Student Statistics (Python)

**File:** `python_examples/data_processing.py`

**Steps:**

1. Open the function `calculate_student_statistics`.
2. Read the docstring to understand the requirements: compute average, median and maximum.
3. Use Copilot or RooCode to implement the function.
4. Ask the AI to generate unit tests in `tests/test_data_processing.py`.
5. Run the tests and iterate on your prompt until all tests pass.

## Exercise 2  Normalise and Group Scores (Python)

**Files:** `python_examples/data_processing.py`

Implement `normalise_scores` and `group_by_grade` following the docstrings.  Provide examples of inputs and expected outputs in your prompts.  Write additional tests covering edge cases such as empty lists and zero maximum values.

## Exercise 3  Parse CSV and Summarise Logs (Python)

**Files:** `python_examples/file_io.py`

1. Use Copilot/RooCode to implement `parse_csv_content` according to its specification.
2. Implement `load_csv_file` to read a file and call `parse_csv_content`.
3. Create or use the provided log file for `summarise_log_file` and implement the summary logic.
4. Write tests in `tests/test_file_io.py` and refine your prompts until the tests pass.

## Exercise 4  Build an API Client (Python)

**File:** `python_examples/api_client.py`

Implement the `get` and `post` methods of the `ApiClient` class.  Ensure proper error handling and JSON serialisation.  Write unit tests that mock the `requests` library to simulate API responses.

## Exercise 5  Model Classes and Relationships (Python)

**File:** `python_examples/model_script.py`

1. Implement the `describe` method of the `Book` class.
2. Implement `add_book`, `remove_book`, `search_by_title`, `search_by_author` and `list_books` in the `Library` class.
3. Use prompt engineering to generate docstrings and a Mermaid diagram showing how `Author`, `Book` and `Library` relate.

## Exercise 6  Java Code Migration

**Files:** `java_migration/legacy_java/Example.java` and `java_migration/modern_java/Example.java`

1. Examine the legacy Java code, which uses raw collections and manual loops.
2. Ask Copilot’s Agents or RooCode’s Orchestrator Mode to migrate the code to Java 17, using generics, the Stream API and Optional where appropriate.
3. Compare your result with the provided modern version.  Write JUnit tests to verify that the behaviour is preserved.

## Exercise 7  Design the Student Performance Dashboard

**File:** `requirements/BRD.md`

Read the business requirements and use prompt engineering to scaffold a new Python or Java project that satisfies the functional and non‑functional requirements.  Ask Copilot or RooCode to:

1. Create data models for students, grades and attendance records.
2. Implement API endpoints as described.
3. Generate unit tests and Markdown documentation.
4. Produce a Mermaid diagram illustrating the data flow from ingestion to report generation.

## Reporting and Reflection

After completing each exercise, write a short summary of what prompts worked, what didn’t and how you iterated.  Share your reflections with your team so everyone learns from each other’s experience.