# RooCode Training Plan

This document provides a thorough training plan for using **RooCode**, an open‑source AI coding assistant that runs locally in your editor. RooCode allows you to generate code, refactor existing projects, write documentation, create diagrams and automate tasks, all without sending your code to a remote server. Because RooCode is privacy‑first and open source, it is ideal for organisations that prefer to retain control over their source code. This plan guides developers through installation, configuration, and advanced usage of RooCode. It also revisits fundamental computer‑science concepts to help you craft clear, algorithmic prompts. Whether you are a seasoned engineer or a first‑year student reacquainting yourself with algorithms, this guide will equip you to get the most out of RooCode.

---

## A]  Purpose & Audience

This plan is written for **programmers.ai** developers — local, remote and offshore — who will use RooCode in day‑to‑day delivery. The goals are to:
- Install RooCode in VS Code and connect it to an approved AI provider (OpenAI, Azure OpenAI, or a local model).
- Understand agentic capabilities and when to use each RooCode mode.
- Apply algorithmic thinking to produce clear, testable prompts.
- Practise with hands‑on exercises that mirror common engineering work.

> **Reminder:** As with Copilot, RooCode’s results depend on the quality of your prompts and the context you provide. Treat it like a junior pair‑programmer: be explicit, review outputs, iterate.

---

## B]  Prerequisites & Environment

1) **Visual Studio Code**
- Install the latest VS Code: <https://code.visualstudio.com/>

2) **Git**
- Required for cloning the training repo and working in branches.

### Windows
- Download **Git for Windows**: <https://git-scm.com/download/win>
- Run the installer (default options are fine).
- Verify in a terminal: `git --version`

### Linux
- Update packages: `sudo apt update`
- Install: `sudo apt install git` (use the package manager for your distro if different)
- Verify: `git --version`

### macOS
- With Homebrew: `brew install git`
- Verify: `git --version`

3) **API Provider Access**
- One of the following, per your project’s policy:
  - **Azure OpenAI** credentials (endpoint, key, API version, deployment name)
  - **OpenAI** API key
  - **Local model** runtime (e.g., Ollama) reachable on your machine or network

> **Security note:** Use organisation‑approved keys only. Never paste secrets into code files; store them in VS Code settings or environment variables.

---

## C]  Installing & Enabling RooCode

### 1) Install the Extension
- Open VS Code.
- Press `Ctrl+Shift+X` to open Extensions.
- Search for **“Roo Code”** and install from the **Visual Studio Marketplace**: <https://marketplace.visualstudio.com/items?itemName=Roo-Code.Roo-Code>
- Alternative registries: **Open VSX** <https://open-vsx.org/extension/roo-code/roo-code>
- **Manual (VSIX):** download the latest release from GitHub <https://github.com/RooCodeInc/Roo-Code/releases> → Extensions panel **…** → **Install from VSIX…**

### 2) Configure an AI Provider
Open **Settings** (`Ctrl+,`) and search for **“RooCode”**. Set:

- **RooCode: Api Provider** → one of `OpenAI`, `AzureOpenAI`, or `Custom` (for local/HTTP providers).
- **RooCode: Api Key** / **Endpoint** / **Deployment** / **Model** depending on provider.
- Example configs:
  - **OpenAI:** provider `OpenAI`, set key, model (e.g. `gpt-4o`).
  - **Azure OpenAI:** provider `AzureOpenAI`; set endpoint URL, key, API version (e.g., `2024-12-01-preview`), and deployment name.
  - **Local (Ollama/custom):** provider `Custom`; set base URL (e.g., `http://localhost:11434/api`) and model name (`llama3`, `mistral-large`, etc.).

> Restart VS Code after configuration so RooCode picks up changes.

### 3) Verify & Basic Commands
- RooCode icon appears in the Activity Bar.
- Open the Command Palette (`Ctrl+Shift+P`) and try:
  - **“Roo Code: Run”** — execute a prompt against the current file/selection.
  - **“Roo Code: Architect”** — scaffold projects or modules.
  - **“Roo Code: Doc”** — generate docstrings/Markdown/PR summaries.
  - **“Roo Code: Ask”** — ask questions of the codebase.
  - **“Roo Code: Debug”** — propose fixes from an error/stack trace.
  - **“Roo Code: Orchestrator”** — multi‑step automation across files/commands (advanced).

> If prompts fail, double‑check provider settings and network access. For local models, ensure the runtime is running (e.g., `ollama serve`).

---

## D]  Using RooCode Effectively (Agentic Workflows)

RooCode supports agent‑style multi‑step work. Treat each mode like a capability you can chain:

### Code Mode
**When:** Implement a function, refactor a block, add tests.
**How:** Select code or place cursor → `Roo Code: Run` → describe the change precisely.  
**Tips:** Specify algorithm, constraints (time/space), style (PEP 8), and edge cases. Provide function signatures or examples.

### Architect Mode
**When:** New project/module/service scaffolding.
**How:** `Roo Code: Architect` → describe folders, files, frameworks, tests, linters.  
**Tips:** List concrete endpoints, models, and configuration files you want generated.

### Doc Mode
**When:** Writing docstrings, READMEs, PR descriptions, Mermaid diagrams.  
**How:** `Roo Code: Doc` → ask for standardized formats (PEP 257, Google/Numpy docstrings) and include diagrams.

### Ask Mode
**When:** You need to find logic or map the codebase.  
**How:** `Roo Code: Ask` → questions like “Where is rate‑limiting implemented?” or “Which modules import `ApiClient`?”

### Debug Mode
**When:** You have an exception/trace and want a proposed fix.  
**How:** `Roo Code: Debug` → paste the error; ask for minimal diffs and tests to reproduce.

### Orchestrator Mode (Advanced)
**When:** Multi‑file edits, running tests, updating deps, generating release notes.  
**How:** `Roo Code: Orchestrator` → review steps; approve changes incrementally.

> **Review everything.** Never auto‑apply sweeping edits without reading diffs and running tests.

---

## E]  Training Exercises (with the training repository)

Open the companion repository `training_repo_final` in VS Code. All files referenced below already exist in the repo.

1) **CSV Parsing (Python) — `python_examples/file_io.py`**  
   Prompt RooCode to implement `parse_csv_content`. Be explicit about splitting lines, handling quotes, trimming whitespace, padding missing fields with `None`, and naming extra fields `extra_1`, `extra_2`, …

2) **Student Statistics (Python) — `python_examples/data_processing.py`**  
   Implement `calculate_student_statistics`, `normalise_scores`, `group_by_grade`. Ask for docstrings, type hints, and complexity notes. Verify edge cases (empty list, zeros, negative scores).

3) **HTTP Client (Python) — `python_examples/api_client.py`**  
   Implement `get` and `post`. Request robust error handling, timeouts, and (optionally) retries. Ask RooCode to propose unit tests for common failures.

4) **Library Model (Python) — `python_examples/model_script.py`**  
   Implement `Author`, `Book`, and `Library` methods (`describe`, `add_book`, `remove_book`, `search_by_title`, `search_by_author`, `list_books`). Emphasise list comprehensions and clean property handling. Generate tests.

5) **Java Migration — `java_migration/legacy_java/Example.java` → `modern_java/Example.java`**  
   Use `Ask` or `Orchestrator` to migrate code with generics/streams/Optional. Compare the output with `modern_java/Example.java`. Request a JUnit test to lock behaviour.

> After each exercise, **run tests** (see `/tests`). Record what prompt phrasing produced the best results, and iterate.

---

## F]  Additional Resources

- **RooCode Documentation:** <https://docs.roocode.com>
- **RooCode GitHub (releases/VSIX):** <https://github.com/RooCodeInc/Roo-Code>
- **Intro/How‑to (video):** RooCode v3.3 UPDATE — <https://www.youtube.com/watch?v=PE-0P6SAZYc>
- **Feature overview (video):** Roo Code is AMAZING — <https://www.youtube.com/watch?v=r5T3h0BOiWw>
- **Local models:** Ollama — <https://ollama.com>

---

## G]  Summary

By following this plan, **programmers.ai** developers can install and configure RooCode with OpenAI, Azure OpenAI, or a custom/local model; use mode‑specific workflows (Code, Architect, Doc, Ask, Debug, Orchestrator); and apply algorithmic prompting to generate code, refactor legacy projects, write documentation, and create diagrams. Always review generated output for correctness, security and style, commit with meaningful messages, and capture successful prompts in a shared prompt library.
