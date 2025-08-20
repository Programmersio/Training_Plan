# Lab 4 – Static & Dynamic Review

## Objectives

In this lab you will practise reviewing and validating AI‑generated code using static analysis tools, unit tests and manual code review.  You will learn how to combine automated checks with human judgement to ensure the correctness, security and maintainability of your code.

## Prerequisites

- Completion of Labs 1–3.
- A working Python environment with `pytest` and a linter installed (e.g. `flake8` or `pylint`).
- Access to the training repository containing your AI‑generated code from earlier labs.

## Step‑By‑Step Instructions

### 1. Run a linter

1. In the root of the training repository, run your preferred linter on the Python files.  For example:

   ```bash
   flake8 python_examples
   ```

2. Examine the output.  Fix any issues related to unused imports, variable naming, unreachable code or security warnings.  Re‑run the linter until it reports no errors or only acceptable warnings.

### 2. Evaluate test coverage

1. Ensure that unit tests exist for the functions `calculate_student_statistics`, `normalise_scores`, `group_by_grade`, `binary_search` and the API client methods.
2. Run `pytest --cov=python_examples` to generate a coverage report.  Analyse which lines remain untested.
3. If coverage is below 80%, write additional tests in the `tests` directory.  Use assertions to check edge cases (e.g. empty lists, negative values, invalid inputs).

### 3. Review code manually

1. Open each AI‑generated function and read it line by line.  Consider the following checklist:
   - **Correctness**: Does the code handle all specified inputs?  Are there off‑by‑one errors or unchecked conditions?
   - **Readability**: Are variable names meaningful?  Is the control flow easy to follow?
   - **Error handling**: Does the code raise appropriate exceptions and avoid silent failures?
   - **Security**: Does the API client validate URLs, sanitise inputs and avoid injection risks?
2. Document any issues or improvements.  Make the necessary edits and re‑run tests and linters.

### 4. Reflect on dynamic vs static review

1. Compare the static linter output with the dynamic test results.  Did any errors slip through one type of check but not the other?
2. Consider how AI suggestions might introduce subtle bugs (e.g. under‑handled exceptions or performance issues).  Discuss strategies for catching these early.

## Reflection Questions

1. Which issues were caught by the linter that the unit tests missed, and vice versa?
2. What manual improvements did you make to the AI‑generated code?  Were they primarily stylistic or functional?
3. How will you integrate static and dynamic review into your daily workflow when using AI tools?

## Expected Outcomes

By the end of this lab you will:

- Run static linters and interpret their warnings on AI‑generated code.
- Measure and improve test coverage with `pytest --cov`.
- Perform manual code reviews focusing on correctness, readability and security.
- Appreciate the complementary benefits of static and dynamic analysis.
