# Prompt Engineering Training Plan

Large‑language models (LLMs) usefulness depends entirely on the **prompts** you provide. Prompt engineering is the practice of crafting clear, precise instructions that guide an AI model toward the desired output.  This training plan teaches developers how to design effective prompts based on sound computer‑science principles.  It revisits first‑year topics like algorithms, data structures and problem decomposition, and demonstrates how these concepts improve your prompts.  Whether you are new to AI or looking to refine your skills, this guide will help you harness the full potential of Copilot and RooCode.

---

## A]  Why Prompt Engineering Matters

When you ask a model to “write some code,” you leave it to guess what you need.  If you specify your goal, inputs, expected outputs, constraints and examples, you narrow the possibilities and increase accuracy.  Poorly written prompts lead to incorrect, incomplete or inefficient code; clear prompts result in reliable, maintainable solutions.  The principles of prompt engineering apply across languages and tools.  They are especially important when working with enterprise projects where security, performance and readability are critical.

### 1.  Algorithmic Context

Programming tasks are built on algorithms and data structures.  In first‑year computer‑science courses you learn patterns like linear search, binary search, sorting algorithms and recursion.  You also learn to choose between lists, dictionaries, stacks, queues, trees and graphs.  When writing prompts, refer to these patterns explicitly: *“Implement a binary search algorithm”* or *“Use a hash map keyed by user ID”*.  This helps the model understand the performance requirements and data relationships.

### 2.  Clarity and Detail

Ambiguity is the enemy of prompt engineering.  Avoid vague terms like “improve,” “better” or “clean up.”  Instead specify what you want to change and why.  For example: *“Refactor this function to reduce its time complexity from O(n²) to O(n log n)”* or *“Rewrite this code to follow PEP 8 style guidelines.”*  Provide the relevant code or function signature so the model has context.  If you need documentation, specify the format (docstring, JSDoc, Markdown) and include examples.

### 3.  Iterative Refinement

Prompt engineering is not a one‑shot process.  After receiving a response from the model, review the output.  If it contains mistakes or omissions, adjust your prompt by adding constraints or examples.  Repeat until the output meets your requirements.  Keep a record of effective prompts to reuse and share with teammates.

---

## B]  Anatomy of a Well‑Structured Prompt

A well‑structured prompt typically includes these elements:

1. **Role or Perspective** – Define the persona or expertise you want the model to adopt.  Example: *“Act as a senior Python developer specialising in data processing.”*
2. **Task Description** – Clearly state what you want the model to do.  Use verbs like *implement*, *refactor*, *explain*, *document*, *test*, *summarise*.
3. **Inputs** – Describe the input types, formats and any relevant constraints.  Example: *“The function receives a list of strings where each string is a comma‑separated list of values.”*
4. **Outputs** – Describe the expected output type and structure.  Example: *“Return a dictionary with keys `mean`, `median` and `mode` mapped to floats.”*
5. **Algorithmic Constraints** – Mention performance, memory or algorithm requirements.  Example: *“Use merge sort for O(n log n) time complexity”* or *“Do not use recursion to avoid stack overflow.”*
6. **Examples** – Provide sample inputs and outputs, or templates for formatting.  Example: show a function signature with a docstring so the model mimics your style.
7. **Style Instructions** – Specify coding style, naming conventions and documentation guidelines.  Example: *“Use snake_case for variables and include type hints.”*

Here is an example of a well‑structured prompt:

> *You are a Python developer.  Implement a function `validate_password(password: str) -> bool` that checks whether a password is at least 8 characters long, contains an uppercase letter, a lowercase letter, a digit and a special character.  Return `True` if the password is valid, `False` otherwise.  Include a PEP 257 docstring and two example calls in a comment.*

This prompt defines the role, task, input, output, constraints and format, leaving little room for misinterpretation.

---

## C]  Principles for Effective Prompting

Use these principles to design prompts that yield accurate and useful results:

### 1.  Be Specific

Specify what you want the model to do and how it should do it.  For example, *“Generate a list of prime numbers up to 100 using the Sieve of Eratosthenes”* is better than *“Write a prime generator.”*  Include relevant constraints like time complexity or memory usage.

### 2.  Decompose Complex Tasks

Breaking large problems into smaller tasks improves the quality of the output and makes it easier to debug.  For instance, when building a web service, separate prompts for data models, API endpoints, input validation and tests.  This mirrors algorithmic decomposition: solve subproblems and compose the results.

### 3.  Provide Examples

Demonstrate the expected input and output format.  If you want the model to produce a JSON response, include a sample JSON.  For diagrams, provide a small Mermaid snippet.  Examples act as a template the model can emulate.

### 4.  Ask for Explanations

When you need to understand code or make improvements, ask the model to explain what the code does and why.  For example: *“Explain how this function calculates the Fibonacci sequence and suggest two optimisations.”*  Explanations reveal the model’s reasoning and help you identify errors or inefficiencies.

### 5.  Use Chat Interfaces for Exploration

Tools like Copilot Chat and ChatGPT are ideal for brainstorming and iterative prompting.  You can ask for clarifications, request alternative implementations or explore different design choices.  This interactive approach is particularly useful when working on unfamiliar tasks.

---

## D]  Training Exercises

Here is a curated collection of prompts you can use with GitHub Copilot, RooCode or other AI coding assistants. They are grouped by category and correspond to the examples and exercises in this repository.  Feel free to modify the prompts to better fit your codebase.

### Python – Data Processing

1. Implement Statistics

Use the following prompt to implement the `calculate_student_statistics` function:

    You are a Python developer.  Implement the function `calculate_student_statistics` in `python_examples/data_processing.py`.  It should take a list of numeric scores and return a tuple of (average, median, maximum).  The average should be rounded to two decimal places.  Raise a `ValueError` if the list is empty.

2. Normalise Scores

Implement `normalise_scores` in `python_examples/data_processing.py`:
    
      Given a list of scores and an optional target, scale the scores proportionally so that the highest score equals the target.  Preserve the original order.  If the list is empty, return an empty list.  If the maximum is zero, return a list of zeros.

3. Group by Grade

Implement the `group_by_grade` function in `python_examples/data_processing.py`:
    
     Group numeric scores into letter grades (A: 90–100, B: 80–89, C: 70–79, D: 60–69, F: <60) and return a dictionary mapping each grade to its list of scores.  Exclude empty grades.

### Python – File I/O

1. Parse CSV Content

Implement `parse_csv_content` in `python_examples/file_io.py`: 

    The function takes a CSV string with a header and returns a list of dictionaries keyed by column names.  Strip whitespace, ignore empty lines, pad missing fields with `None` and name extra fields `extra_1`, `extra_2`, etc.

2. Load CSV File

Implement `load_csv_file` in `python_examples/file_io.py`:

    Given a file path, read the file content and pass it to `parse_csv_content`.  If the file does not exist, raise `FileNotFoundError`.

3. Summarise Log File

Implement `summarise_log_file` in `python_examples/file_io.py`: 

    Read a log file and return a dictionary with `line_count` (non‑empty lines), `error_count` (lines containing "ERROR" case-insensitive) and `warnings` (unique warning messages after the prefix "WARNING:").

### Python – API Client

1. Implement GET Method

Implement the `get` method of `ApiClient` in `python_examples/api_client.py`:

    Build the URL from `base_url` and `path`, include headers and query parameters, send a GET request using the `requests` library, raise an exception on non‑2xx status codes and return the parsed JSON response.

2. Implement POST Method

Implement the `post` method of `ApiClient` in `python_examples/api_client.py`:  

    Accept a JSON body dictionary, send it as a POST request to the given `path`, handle errors and return the parsed JSON response.  Consider adding retry logic for transient errors.

### Python – Model Classes

1.  Describe Book

Implement the `describe` method of the `Book` class in `python_examples/model_script.py`:  

    It should return a string in the format `"<title>" by <Author Name> (ISBN: <isbn>)`.

2.  Library Methods

Implement the methods `add_book`, `remove_book`, `search_by_title`, `search_by_author` and `list_books` in the `Library` class (`python_examples/model_script.py`) :

    Ensure case-insensitive searching and proper handling of missing ISBNs.

### Java – Code Migration

Legacy to Modern Java

Migrate the class in `java_migration/legacy_java/Example.java` to Java 17.  

    Use generics, streams and Optional to modernise the code.  Create a corresponding test class using JUnit to verify the behaviour.  Compare your result with `java_migration/modern_java/Example.java`.

### Documentation & Diagrams

Generate Documentation and Diagram

In `python_examples/model_script.py`:

    Generate Markdown documentation with docstrings for the `Author`, `Book` and `Library` classes.  Include a Mermaid diagram showing the relationships among these classes, with `Author` having a one‑to‑many relationship with `Book`, and `Library` containing multiple `Book` instances.


    Create a README for the Student Performance Dashboard described in `requirements/BRD.md`.  Include an overview of the project, setup instructions, API endpoints and a Mermaid diagram illustrating the data flow from ingestion to report generation.

---

## E]  Additional Resources

* **OpenAI Prompt Engineering Guide** – [https://platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering) – Official guide with examples and best practices.
* **GitHub Copilot Prompt Guide** – [https://github.blog/2023-09-12-how-to-write-better-prompts-for-github-copilot/](https://github.blog/2023-09-12-how-to-write-better-prompts-for-github-copilot/) – Tips for crafting prompts specifically for Copilot.


Videos:

| Topic                       | Video Title                                           | Link                                                              | Description                                       |
|-----------------------------|-------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------|
| Prompt Engineering Basics   | *Prompt Engineering for Beginners*                   | [Watch](https://youtu.be/riO3e-FBieA?si=86gIO74zk2tYrjSW)               | Introduction to prompt design and common pitfalls. |
| Advanced Prompt Techniques  | *Advanced Prompt Engineering with GPT-4*             | [Watch](https://youtu.be/-XivIt_5oSw?si=agLozvFqrGiLT4Oz)               | Covers complex tasks, multi‑step prompts and more. |
| Demo    | *Master the core principles of prompt engineering with GitHub Copilot*             | [Watch](https://youtu.be/hh1nOX14TyY?si=flrngVtmrDbwFYEv)               | Shows iterative prompting to build a real project. |

---

## F]  Summary

Prompt engineering is a critical skill for working with AI coding assistants.  By grounding your prompts in algorithmic thinking, providing clear objectives and constraints, and iteratively refining your instructions, you can guide models like Copilot and RooCode to produce high‑quality code, tests, documentation and diagrams.  Use the exercises and resources in this plan to practise and improve.  As you gain experience, share effective prompts with your colleagues to build a collective knowledge base.