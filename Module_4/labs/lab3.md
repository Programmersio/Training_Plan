## Lab 3 – Flaky Test Detection & Debugging

### Objective

Identify, reproduce and fix flaky tests.  You’ll learn why tests can pass and fail unpredictably—often due to timing, race conditions or environment differences—and practise strategies to stabilise them.  Flaky tests are surprisingly common: one study found that **50 % of test failures are caused by flakiness**【927012084993884†L79-L82】, and Capgemini’s World Quality Report notes that **50 % of automation time is spent repairing broken tests**【927012084993884†L132-L136】.  Unreliable tests can delay releases by 20–25 %【927012084993884†L137-L140】.  Your goal is to reduce these costs by making your test suite trustworthy.

### Setup

1. Ensure `pytest` is installed along with `pytest-rerunfailures` and `pytest-randomly` for running tests multiple times.  Install them if necessary:

   ```bash
   pip install pytest-rerunfailures pytest-randomly
   ```

2. Prepare or locate a test that is likely to be flaky.  You can intentionally create one in the `tests/` directory—for example, a function that relies on time or randomness:

   ```python
   import time
   import random

   def unstable_increment(x):
       # Fails randomly and depends on timing
       time.sleep(random.choice([0.01, 0.02]))
       if random.random() < 0.3:
           return x + 2  # incorrect value 30 % of the time
       return x + 1

   def test_unstable_increment():
       assert unstable_increment(1) == 2
   ```

### Steps

1. **Run the test repeatedly**:
   - Use `pytest` with the `--count` flag (from `pytest-repeat`) or loop the test manually to expose flakiness.  For example:

     ```bash
     pytest -q --count=20 tests/test_unstable_increment.py
     ```

   - Observe that the test intermittently fails.  Flakiness is manifested by passes and failures without code changes【927012084993884†L86-L89】.

2. **Analyse the cause**:
   - Identify why the test is unstable.  In this example, the randomness and variable sleep times create non‑deterministic behaviour.  In real code, flakiness might stem from race conditions, external API calls, or shared state【927012084993884†L90-L119】.
   - Use logging or print statements to reveal ordering issues or intermittent values.  For concurrency problems, consider adding locks or synchronisation primitives.

3. **Stabilise the test**:
   - Remove randomness or control it with fixed seeds.  Inject dependencies so you can mock time or random values.  For the example above:

     ```python
     def test_stable_increment(monkeypatch):
         monkeypatch.setattr(random, "random", lambda: 0.0)
         monkeypatch.setattr(random, "choice", lambda x: 0.01)
         assert unstable_increment(1) == 2
     ```

   - Where external services are involved, use mocks or service simulators.  For asynchronous code, await operations properly and avoid arbitrary sleeps.

4. **Leverage AI for debugging**:
   - Ask your AI coding assistant to explain why the test is flaky and suggest fixes.  Provide the test code and failure pattern as context.  Evaluate the suggestions and apply them where appropriate.

5. **Re‑run the tests**:
   - After applying fixes, run the test repeatedly again.  It should now pass consistently.  Measure how long the suite takes to run and ensure it remains performant.
   - If you still see intermittent failures, continue investigating.  Use tools like `pytest-rerunfailures` to automatically retry flaky tests and highlight persistent problems.

6. **Document your findings**:
   - In your reflection, describe the root cause of the flakiness, how you fixed it and any AI prompts that were particularly helpful.  Note the time saved by using AI to debug and stabilise the test suite.

### Deliverables

- A fixed version of the flaky test, committed to the repository.
- A write‑up detailing the debugging process, root cause analysis, and lessons learned about flakiness.