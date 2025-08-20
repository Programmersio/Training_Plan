# Lab 1 – Using GitHub Copilot

## Objectives

This lab introduces you to GitHub Copilot as an inline coding assistant.  You will learn how to generate code from detailed comments, review its output, and iterate on the results.  By the end of this lab you should be comfortable prompting Copilot for small functions and API clients, and running unit tests to validate the generated code.

## Prerequisites

- A working installation of Visual Studio Code with the GitHub Copilot extension enabled under your organisation’s licence.
- The training repository cloned locally.  Open the `training_repo/python_examples` folder in VS Code.
- Basic familiarity with Python functions, asynchronous programming and unit testing with `pytest`.

## Step‑By‑Step Instructions

### 1. Implement `calculate_student_statistics`

1. Open **`python_examples/data_processing.py`**.  Find the placeholder function `calculate_student_statistics` marked with a `TODO` comment.
2. Above the function signature, type a descriptive comment such as:

   ```python
   # Compute the average (rounded to two decimals), median and maximum score from a list of numbers.  Raise a ValueError if the list is empty.
   ```
3. Press **Enter** to allow Copilot to generate a suggestion.  Review the proposed code.  It should:
   - Check for an empty list and raise a `ValueError`.
   - Use Python’s built‑in `sorted` function (or an algorithm you described) to calculate the median.
   - Round the average to two decimal places.
4. Accept the suggestion using **Tab** if it meets the requirements.  Otherwise refine your comment and try again until you are satisfied.

### 2. Implement `normalise_scores`

1. Still in `data_processing.py`, locate the `normalise_scores` function placeholder.
2. Write a prompt that instructs Copilot to scale all scores so that the highest value equals a given target.  For example:

   ```python
   # Scale each score so that the largest score equals the target value (default 100).  Preserve the original order.  Return an empty list if input is empty; return a list of zeros if the maximum is zero.
   ```
3. Press **Enter** and review the generated code.  Ensure that it computes a scaling factor and handles edge cases properly.
4. Accept or refine as needed.

### 3. Implement API client methods

1. Open **`python_examples/api_client.py`**.  Find the `ApiClient` class with `get` and `post` methods marked as `TODO`.
2. Above each method signature, write a detailed comment for Copilot, such as:

   ```python
   # Use httpx to send an asynchronous GET request to the path appended to base_url.  Include optional headers and query parameters.  Raise for non‑2xx responses and return the parsed JSON.
   ```

   and

   ```python
   # Use httpx to send an asynchronous POST request with a JSON body to the path appended to base_url.  Include optional headers.  Raise on error and return the JSON response.  Consider retrying transient errors.
   ```
3. Observe the generated code and ensure it uses `async with httpx.AsyncClient()` and proper error handling.
4. Accept or refine the suggestions.

### 4. Run unit tests

1. Open a terminal and navigate to the root of the training repository.
2. Run the tests with `pytest tests`.  Verify that the tests for data processing and file I/O pass.  If any fail, adjust your code and rerun until all tests succeed.

## Reflection Questions

1. How did the level of detail in your comments influence the quality of Copilot’s suggestions?
2. Did you need to adjust the generated code?  What improvements did you make manually?
3. Would you consider Copilot a reliable starting point for these functions?  Why or why not?

## Expected Outcomes

By completing this lab you will:

- Understand how to craft comments that drive Copilot to generate the desired function implementation.
- Gain experience reviewing AI‑generated code and refining it manually.
- Implement basic data processing and API client functions and run unit tests successfully.
