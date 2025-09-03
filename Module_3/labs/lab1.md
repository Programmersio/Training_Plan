# Lab 1 – Static Analysis & Code Fixing

## Objectives

This lab introduces you to static analysis tools as a first line of defence against bugs and vulnerabilities.  You will generate or select a piece of AI‑created code, run a variety of static checks (linters, type checkers, security scanners) against it, interpret the results and fix the issues.  By the end of this lab you should be comfortable iterating between prompt refinement and code improvements based on static feedback.

## Prerequisites

* Visual Studio Code with the GitHub Copilot extension enabled under your organisation’s licence.
* The training repository cloned locally.  Open the `training_repo/python_examples` folder in VS Code.
* Python 3.11 with `pytest`, `flake8`, `pylint`, `mypy` and `bandit` installed (run `pip install flake8 pylint mypy bandit` if necessary).
* Familiarity with basic Python functions and unit testing.

## Step‑By‑Step Instructions

### 1. Generate or select a target function

1. In `python_examples/data_processing.py`, locate a `TODO` function (e.g. `calculate_student_statistics`) or pick one of your own unfinished functions.
2. Craft a detailed docstring describing the desired behaviour and press **Enter** to let Copilot generate the code.  Alternatively, use Roo Code’s Ask mode to produce the function.
3. Accept the suggestion if it roughly meets your requirements or iterate on the prompt until you are satisfied.

### 2. Run linters and type checkers

1. Open a terminal in the root of the training repository.
2. Run `flake8 python_examples/data_processing.py` and `pylint python_examples/data_processing.py`.  Observe any warnings about unused imports, poor naming, complexity or style violations.  Use the warnings to improve the generated code.
3. Run `mypy python_examples/data_processing.py` to perform static type checking.  If types are missing or mismatched, update the function signature and internal variables to satisfy the type checker.

### 3. Perform security scanning

1. Run `bandit -r python_examples` to scan all Python files for common security issues.  Pay attention to findings such as use of unsafe functions, hard‑coded secrets or dangerous file operations.
2. Fix the reported issues by editing the code.  For example, if Bandit warns about `subprocess` without sanitising inputs, refactor the code to validate inputs or avoid using shell commands.

### 4. Validate with tests

1. Run `pytest tests` to execute the unit tests for your module.  If tests fail, adjust your code accordingly.
2. Repeat the static checks (`flake8`, `pylint`, `mypy`, `bandit`) until no high‑severity issues remain and all tests pass.

## Reflection Questions

1. Which static analysis tool generated the most useful feedback?  Did any of the tools produce false positives?  How did you decide what to fix?
2. How did refining your prompt or adding type annotations influence the quality of Copilot’s suggestions?
3. Did Bandit uncover any security issues that were not obvious from the code alone?  How did you remediate them?

## Expected Outcomes

By completing this lab you will:

* Understand how to run linters, type checkers and security scanners on AI‑generated code.
* Gain experience interpreting and prioritising static analysis findings.
* Improve AI suggestions by refining prompts and adding type information.
* Implement secure, well‑structured functions that pass unit tests and static checks.