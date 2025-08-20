# Prompt Library

This file contains a curated collection of prompts you can use with GitHub Copilot, RooCode or other AI coding assistants.  They are grouped by category and correspond to the examples and exercises in this repository.  Feel free to modify the prompts to better fit your codebase.

## Python – Data Processing

### Implement Statistics

Use the following prompt to implement the `calculate_student_statistics` function:

    You are a Python developer.  Implement the function `calculate_student_statistics` in `python_examples/data_processing.py`.  It should take a list of numeric scores and return a tuple of (average, median, maximum).  The average should be rounded to two decimal places.  Raise a `ValueError` if the list is empty.

### Normalise Scores

    Implement `normalise_scores` in `python_examples/data_processing.py`.  Given a list of scores and an optional target, scale the scores proportionally so that the highest score equals the target.  Preserve the original order.  If the list is empty, return an empty list.  If the maximum is zero, return a list of zeros.

### Group by Grade

    Implement the `group_by_grade` function in `python_examples/data_processing.py`.  Group numeric scores into letter grades (A: 90–100, B: 80–89, C: 70–79, D: 60–69, F: <60) and return a dictionary mapping each grade to its list of scores.  Exclude empty grades.

## Python – File I/O

### Parse CSV Content

    Implement `parse_csv_content` in `python_examples/file_io.py`.  The function takes a CSV string with a header and returns a list of dictionaries keyed by column names.  Strip whitespace, ignore empty lines, pad missing fields with `None` and name extra fields `extra_1`, `extra_2`, etc.

### Load CSV File

    Implement `load_csv_file` in `python_examples/file_io.py`.  Given a file path, read the file content and pass it to `parse_csv_content`.  If the file does not exist, raise `FileNotFoundError`.

### Summarise Log File

    Implement `summarise_log_file` in `python_examples/file_io.py`.  Read a log file and return a dictionary with `line_count` (non‑empty lines), `error_count` (lines containing "ERROR" case-insensitive) and `warnings` (unique warning messages after the prefix "WARNING:").

## Python – API Client

### Implement GET Method

    Implement the `get` method of `ApiClient` in `python_examples/api_client.py`.  Build the URL from `base_url` and `path`, include headers and query parameters, send a GET request using the `requests` library, raise an exception on non‑2xx status codes and return the parsed JSON response.

### Implement POST Method

    Implement the `post` method of `ApiClient` in `python_examples/api_client.py`.  Accept a JSON body dictionary, send it as a POST request to the given `path`, handle errors and return the parsed JSON response.  Consider adding retry logic for transient errors.

## Python – Model Classes

### Describe Book

    Implement the `describe` method of the `Book` class in `python_examples/model_script.py`.  It should return a string in the format `"<title>" by <Author Name> (ISBN: <isbn>)`.

### Library Methods

    Implement the methods `add_book`, `remove_book`, `search_by_title`, `search_by_author` and `list_books` in the `Library` class (`python_examples/model_script.py`).  Ensure case-insensitive searching and proper handling of missing ISBNs.

## Java – Code Migration

### Legacy to Modern Java

    Migrate the class in `java_migration/legacy_java/Example.java` to Java 17.  Use generics, streams and Optional to modernise the code.  Create a corresponding test class using JUnit to verify the behaviour.  Compare your result with `java_migration/modern_java/Example.java`.

## Documentation & Diagrams

### Generate Documentation and Diagram

    In `python_examples/model_script.py`, generate Markdown documentation with docstrings and a Mermaid diagram showing the relationships among `Author`, `Book` and `Library`.  The diagram should depict classes as nodes and references as arrows.

    Create a README for the Student Performance Dashboard described in `requirements/BRD.md`.  Include an overview of the project, setup instructions, API endpoints and a Mermaid diagram illustrating the data flow from ingestion to report generation.