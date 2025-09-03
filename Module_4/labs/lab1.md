## Lab 1 – AI‑Generated Unit Tests

### Objective

Generate a comprehensive suite of unit tests for an existing function using your AI coding assistant.  You will prompt the agent to analyse the function’s logic, create tests that exercise normal and edge‑case behaviour, and then refine those tests based on code coverage and correctness.  This lab demonstrates how AI can accelerate test creation by analysing your code and requirements【226484627048419†L133-L138】 and discovering edge cases humans might overlook【226484627048419†L150-L154】.

### Setup

1. **Select a target function**: Navigate to the `training_repo/python_examples` directory in your workspace.  Choose a function that doesn’t yet have unit tests (e.g. `invoice_utils.py:calculate_discount`, `customer_utils.py:categorise_customer` or any other).  Read through the implementation and its docstring to understand its expected behaviour.
2. **Create a new test file**: In the `tests` directory, create a new file called `test_<function_name>.py` (e.g. `test_calculate_discount.py`).  Add the necessary imports for the function you are testing and for `pytest`.
3. **Install coverage tools**: Make sure `pytest` and `pytest-cov` are installed.  If not, run:

   ```bash
   pip install pytest pytest-cov
   ```

### Steps

1. **Baseline run**: Write one simple test by hand that calls the function with a typical input and asserts the expected output.  Run the test using:

   ```bash
   pytest --cov=training_repo/python_examples --cov-report=term-missing
   ```

   Note the baseline coverage and any lines not executed.

2. **Generate tests with AI**:
   - Open your AI coding tool (GitHub Copilot, Roo Code or similar) and ask it to generate unit tests for the selected function.  Provide the function’s signature and docstring as context.  Encourage the agent to cover normal cases, boundary values and error scenarios.  Remind it to include descriptive test names and assertions.
   - Review the generated tests for correctness.  Do they exercise the full range of input conditions?  Are the assertions valid?  Modify prompts as needed to improve the quality of the suggestions.

3. **Review and refine**:
   - Save the generated tests into your test file.  Run them with `pytest`.  If tests fail, debug whether the failure is due to the test or the function.  Adjust test inputs or the function implementation as appropriate.
   - Identify any missing scenarios (e.g. negative values, zero values, extreme strings).  Ask your AI tool to write additional tests or add them manually.  Ensure the tests remain deterministic (no randomness or side effects).

4. **Measure coverage**:
   - Run `pytest --cov` again and observe the coverage report.  Your goal is to achieve at least **95 % line coverage** for the target module.  If you fall short, identify uncovered lines and write additional tests to execute them.

5. **Document your prompts and results**: In your lab report or reflection, record the prompts you used to generate tests and summarise any modifications you made.  Note how AI improved your test creation speed and coverage【226484627048419†L133-L138】.

6. **Commit your work**: Commit the new test file and any changes to the function.  Use a descriptive commit message such as “Add AI‑generated unit tests for calculate_discount”.

### Deliverables

- A new test file in `tests/` with AI‑generated (and refined) unit tests.
- A brief summary of your prompts, iterations and final coverage results to be included in the Module 4 reflection.