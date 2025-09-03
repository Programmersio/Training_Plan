# Lab 3 – Security & Dependency Scanning

## Objectives

This lab focuses on identifying and remediating security issues and dependency risks in AI‑generated code.  You will learn how to use security scanners to detect common vulnerabilities, audit your project’s dependencies and fix problems.  By the end of this lab you should be confident applying security best practices to AI‑generated code.

## Prerequisites

* Python 3.11 with `bandit` and `pip‑audit` (or `safety` / `pip‑checker`) installed.  Install via `pip install bandit pip‑audit`.
* The training repository cloned locally.
* Completion of Lab 1 or familiarity with your AI‑generated functions.

## Step‑By‑Step Instructions

### 1. Scan for code‑level vulnerabilities with Bandit

1. From the root of the training repository, run `bandit -r python_examples` to recursively scan all Python files.
2. Review the results.  Bandit reports issues such as use of insecure random functions, hard‑coded passwords, dangerous file operations and shell injection vulnerabilities.
3. For each finding:
   - Understand why it is flagged.  Consult the Bandit documentation if needed.
   - Modify the code to eliminate or mitigate the vulnerability.  For example, replace `eval` with safe parsing, parameterise shell commands or move secrets into environment variables.
4. Re‑run Bandit until high‑severity issues are resolved.

### 2. Audit your dependencies

1. Run `pip‑audit` in the root of your repository to identify known vulnerabilities in your installed packages.  Alternatively, if `pip‑audit` is not available, use `safety check` or another software composition analysis (SCA) tool.
2. Examine the report.  It will highlight packages with publicly disclosed CVEs and recommend upgraded versions.
3. Update your `requirements.txt` or `pyproject.toml` accordingly.  Use `pip install --upgrade package==<safe_version>` to apply fixes.
4. Re‑run `pip‑audit` to ensure that no vulnerabilities remain.

### 3. Verify package names and sources

1. Inspect any external dependencies suggested by AI tools.  Ensure the package names exist on trusted repositories (e.g. PyPI) and are not hallucinations【846912144979599†L247-L256】.
2. If you encounter an unfamiliar package, research it before installing.  Check the maintainers, license and downloads.  Consider substituting with a well‑known library.
3. Document the rationale for each dependency in your project’s `README` or internal documentation.

### 4. Test and document

1. Run `pytest tests` to ensure that your changes did not break existing functionality.
2. Add or update docstrings and comments to explain why changes were necessary, particularly when refactoring AI‑generated code to fix security issues.
3. Commit the changes with a message like `Fix Bandit findings and update vulnerable dependencies`.

## Reflection Questions

1. Which vulnerabilities were most common in your AI‑generated code?  Were there any surprising findings?
2. How did you verify that packages suggested by the AI actually exist and are trustworthy?
3. Did updating dependencies introduce any breaking changes?  How did you manage them?

## Expected Outcomes

By completing this lab you will:

* Gain familiarity with Bandit and SCA tools for identifying security vulnerabilities in code and dependencies.
* Learn to verify package names and avoid hallucinated or malicious dependencies.
* Understand how to upgrade dependencies safely and document security fixes.
* Integrate security scanning into your development workflow and ensure that AI‑generated code meets enterprise standards.