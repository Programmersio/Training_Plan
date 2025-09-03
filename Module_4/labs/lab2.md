## Lab 2 – Integration & Self‑Healing Tests

### Objective

Create integration tests that span multiple modules of the training repository, then explore how AI‑powered test tools can update (“self‑heal”) those tests after you refactor the code.  You’ll practise writing high‑level tests that verify end‑to‑end behaviour, measure execution time, and optimise the suite to keep feedback loops fast【226484627048419†L169-L174】.  You’ll also witness self‑healing features that automatically adjust assertions when code signatures change【226484627048419†L185-L188】.

### Setup

1. **Identify a workflow**: Examine the functions in `training_repo/python_examples`.  A simple workflow might involve reading customer data, applying transformations and calculating an invoice.  For example:
   - `file_io.read_json(path)` reads a JSON file.
   - `customer_utils.categorise_customer(data)` classifies customers.
   - `invoice_utils.calculate_invoice(customer_data)` computes totals.

   Choose at least two functions that depend on each other.

2. **Create a test file**: In the `tests` directory, create `test_integration.py` (or similar).  Import the selected functions and any necessary support code.

3. **Prepare sample data**: Create a small JSON or Python dictionary representing typical input for your workflow.  This data should exercise various paths through the code (e.g. different customer tiers).

### Steps

1. **Write a baseline integration test**:
   - Manually write a test that executes the workflow end‑to‑end.  For instance, load the sample data, call `categorise_customer`, then `calculate_invoice`.  Assert that the final invoice contains expected values for different customer categories.
   - Run the test with `pytest` to verify that the workflow behaves as expected.

2. **Generate integration tests with AI**:
   - Use your AI coding assistant to generate additional integration tests.  Provide a description of the workflow and the sample data.  Ask the agent to vary input data and include edge cases (e.g. missing fields, extreme values).  Encourage it to structure tests clearly and use descriptive names.
   - Review the generated tests.  Ensure they cover different interaction scenarios and that the assertions reflect business rules.

3. **Introduce a refactor**:
   - Rename one of the functions or change its parameter order/return type (for example, rename `calculate_invoice` to `compute_invoice_total` and have it return a tuple instead of a dictionary).  Make sure to update the implementation and any calls in the workflow.
   - Observe that your integration tests now fail because of signature changes.

4. **Use self‑healing or regenerate tests**:
   - Many AI tools offer self‑healing tests that detect refactorings by analysing call graphs and code history【226484627048419†L185-L188】.  Ask your tool to update the failing tests automatically.  Alternatively, re‑prompt the agent to regenerate the integration tests given the new function signature.
   - Inspect the updated tests to ensure they still validate the correct behaviour.  Adjust manually if necessary.

5. **Optimise the test suite**:
   - Measure how long your integration tests take to run.  Use `pytest -q` or time the runs manually.  If execution is slow, group related assertions or reduce redundant test cases.
   - Experiment with AI‑assisted test selection: ask your tool to identify which tests need to run after small code changes【226484627048419†L169-L174】.  This helps keep feedback cycles fast.

6. **Commit your work**: Commit the integration tests, refactored code and updated tests.  Use clear commit messages detailing the workflow and the refactor.

### Deliverables

- Integration tests exercising the selected workflow, saved in the `tests/` directory.
- Refactored code demonstrating how self‑healing tests adjust to changes.
- A short write‑up (in your reflection) summarising your experience with self‑healing and optimisation.