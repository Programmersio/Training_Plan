# GitHub Copilot Training Plan

This document is a comprehensive training plan for developers which allow them to use **GitHub Copilot** effectively.  It explains how to set up Copilot through your organisation’s **( here: programmers.ai )** enterprise account, install it in **Visual Studio Code**, and make the most of its capabilities.  Unlike a quick start guide, this plan revisits foundational computer‑science concepts, such as algorithms, data structures, loops and recursion, so you can craft better prompts and understand the output.  Whether you are an experienced engineer or a first‑year student relearning the basics, this guide will help you collaborate with an AI coding assistant while preserving quality, readability and security.

---

## A]  Purpose

Offshore teams and remote developers can use the same instructions to set up Copilot on their machines and connect to the **Programmers.ai** organisation.  This ensures consistent configuration and governance across all locations.  

**Remember**: Copilot’s suggestions are contextual, so the more you know about your problem, the better you can guide the AI.

---

## B]  Prerequisites and Organisational Setup

Before using GitHub Copilot, ensure you meet these prerequisites:

1. **Enterprise Licence** – Copilot is provided through our organisation’s enterprise licence.  Do **not** purchase a personal subscription.  Make sure your GitHub account is part of the **Programmers.ai** organisational account so that billing and policies are centralised.

2. **GitHub Account** – If you don’t have a GitHub account, create one using your corporate email.  Ask your administrator to add your account to the Programmers.ai organisation.  All code should be committed under the organisation to maintain access control and compliance.

3. **Visual Studio Code** – Download the latest [VS Code](https://code.visualstudio.com/) for your operating system.  Copilot integrates seamlessly with VS Code.

4. **Git** – Install Git so you can clone repositories, create branches and push changes.

### Windows
- Download **Git for Windows**: https://git-scm.com/download/win  
- Run the installer (default options are fine).  
- Verify: `git --version`

### Linux
- Update packages: `sudo apt update`  
- Install: `sudo apt install git` (use your distro’s package manager if different)  
- Verify: `git --version`

### MacOS
- With Homebrew: `brew install git`  
- Verify: `git --version`

---

## C]  Installing and Enabling GitHub Copilot

This section walks you through installing the Copilot extension, authenticating via the organisation’s account and enabling suggestions.  It also introduces optional features like Copilot Chat and Agentic mode.

### 1.  Install the Copilot Extension

1. **Open VS Code**.
2. Press `Ctrl+Shift+X` (or click the Extensions icon) to open the Extensions pane.
3. In the search box, type **“GitHub Copilot”**.  Select the official extension and click **Install**.  Wait until installation completes and the Copilot icon appears in the status bar.

### 2.  Authenticate with the Organisation

1. After installation, a prompt will appear asking you to **Sign in to GitHub**.  Click **Sign In**.
2. Choose **“Continue with GitHub”** and enter your corporate credentials.  Complete any multi‑factor authentication.
3. When asked to authorise Copilot, confirm that the **Programmers.ai** organisation is listed and click **Authorize**.  This links your Copilot usage to the organisation’s licence.
4. Return to VS Code.  You should see a confirmation message that Copilot is active.

### 3.  Enable Suggestions and Agentic Mode

Copilot suggestions appear as faded code (ghost text) while you type.  To control when they appear:

1. Open the **Command Palette** (`Ctrl+Shift+P`) and run **“Copilot: Toggle Completions”** (or **Enable/Disable Completions** in some builds).
2. In **Settings** (File → Preferences → Settings), search for **“Inline Completions”** and set **Enable** to **On**.

**Agentic settings to know (search these in Settings):**
- `chat.agent.enabled` — enable/disable agent mode (requires recent VS Code).
- `chat.agent.maxRequests` — max background requests an agent can make.
- `github.copilot.chat.agent.runTasks` — allow agent to run workspace tasks.
- `chat.mcp.discovery.enabled` — discover MCP servers from other tools.
- `github.copilot.chat.agent.autoFix` — attempt automatic fixes on generated changes.
- `chat.tools.autoApprove` (experimental) — auto‑approve tool usage (keep **false** unless you know why).


**Agentic Mode** is an advanced feature that allows Copilot to perform multi‑step tasks, such as refactoring a file or migrating code between frameworks.  To enable it (if available to the organisation):
1. Open the Command Palette and run **“Copilot: Agents: Enable/Disable”** (names vary slightly by version). You can also use **“Copilot: Toggle Completions”**, **“Copilot: Open Completions Panel”**, **“Copilot: Explain This Code”**, and **“Copilot: Generate Tests”** to drive agentic workflows.
2. Ensure it’s **Enabled**.  When agent mode is active, you can instruct Copilot using high‑level tasks like “Migrate this ExpressJS API to FastAPI in Python” or “Convert this AngularJS component to React 18 with TypeScript.”  Copilot will propose changes and ask you to confirm before applying them.

### 4.  Install and Use Copilot Chat (Optional)

Copilot Chat is a separate extension that offers a chat interface similar to ChatGPT within VS Code.  To install and use it:

1. In the Extensions pane, search for **“GitHub Copilot Chat”** and click **Install**.
2. Open the Chat panel from the Activity Bar.  You can ask questions like “Explain what this function does,” “Refactor this code to use `async`/`await`,” or “Generate unit tests for this method.”  The chat will respond with explanations and code snippets.

---

## D]  Algorithmic Thinking and Prompt Crafting

To maximise Copilot’s usefulness, you need to think like a computer scientist.  This section revisits fundamental algorithms and data structures and shows how they inform prompt design.

### 1.  Decomposition and Control Flow

Breaking a problem into clear steps makes it easier for both humans and AI to solve.  For example, to compute statistics on student grades, you might: 1) read the data; 2) parse each record; 3) compute mean, median and mode; 4) format results.  When prompting Copilot, describe these steps explicitly.  For loop‑based tasks, mention the type of loop (`for` vs. `while`) and the stopping condition.  For decision making, specify the conditions and branches.

### 2.  Choosing Data Structures

Data structures influence performance.  Arrays and lists provide fast indexed access; dictionaries offer O(1) lookup; queues and stacks support FIFO/LIFO operations; trees and graphs model hierarchical and network structures.  When you ask Copilot to implement a solution, state which structure to use.  For example: *“Use a dictionary where keys are student IDs and values are lists of assignment scores”* or *“Implement a binary search tree with insertion and search methods.”*  This guidance helps Copilot generate efficient code.

### 3.  Time and Space Complexity

Performance matters, especially in large data sets.  Copilot may generate a naive implementation if you do not specify a complexity requirement.  If you need a sort algorithm faster than O(n²), ask explicitly for merge sort (O(n log n)) or quicksort.  When dealing with memory, mention whether you can afford extra space or require an in‑place algorithm.

### 4.  Prompt Examples

We’ll use **one** running example so every prompt builds on the same code: a function that computes the **median** of a list of integers.

* **Generate Code:**  
  - *“Write a Python function `calculate_median(scores: list[int]) -> float` that computes the median of a list of integers. If the list has an even number of elements, return the average of the two middle values. Use a sort with O(n log n) time. Include a docstring and type hints.”*

* **Refactor Code:**  
  - *“Refactor `calculate_median` to avoid sorting the entire list by using a selection algorithm (e.g., `statistics.median` or `heapq.nsmallest`). Preserve the function signature and include error handling for empty input.”*

* **Write Tests:**  
  - *“Generate `pytest` unit tests for `calculate_median`. Cover: odd length, even length, duplicates, negative numbers, large lists, and the empty‑list error path. Use clear assertion messages.”*

* **Explain and Document:**  
  - *“Explain what `calculate_median` does, define the input/output, the chosen algorithm and its complexity, list edge cases, and include the function’s docstring in reStructuredText or Google style.”*

These prompts specify the task, desired output and constraints, increasing the quality and relevance of Copilot’s suggestions.


---

## E]  Training Exercises

Use the accompanying `training_repo_final` repository to practise what you’ve learned.  Start by cloning the repo and opening it in VS Code.  The exercises below are written primarily in **Python**, with one Java file for code migration practice.  Instructions are in the `training_exercises.md` file of the repository.

1. **Data Processing (Python)** – Implement functions in `python_examples/data_processing.py` such as `calculate_student_statistics`, `normalise_scores` and `group_by_grade`.  Write prompts that instruct Copilot to compute average grades, normalise scores between 0 and 100, and categorise students into grade bands.  Review the generated code, ensure it handles edge cases and add type hints and documentation.
2. **File I/O and Parsing (Python)** – In `python_examples/file_io.py`, write prompts to parse CSV content, load files and summarise log data.  Use Copilot to generate robust parsing logic, including error handling for malformed lines.  Ask Copilot to write docstrings and examples for each function.
3. **API Client (Python)** – The `ApiClient` class in `python_examples/api_client.py` needs `get` and `post` methods.  Prompt Copilot to implement asynchronous HTTP requests with timeouts and error handling.  Request that it uses the `requests` or `httpx` library and includes proper docstrings.
4. **Class Relationships (Python)** – In `model_script.py`, fill in methods for `Author`, `Book` and `Library`.  Ask Copilot to implement methods like `describe`, `add_book`, `remove_book`, `search_by_title` and `list_books`.  Emphasise using list comprehensions and clear property handling.  Generate unit tests using `pytest` or `unittest` to cover typical and edge cases.
5. **Java Migration** – In `java_migration/legacy_java/Example.java`, there is an old Java implementation using raw collections and manual iteration.  Prompt Copilot (or RooCode) to migrate this code to the modern version in `modern_java/Example.java`, using generics, streams and the `Optional` class.  Compare the output with the provided modern implementation.

These exercises will help you practise prompting, algorithmic thinking and review.  After completing them, reflect on how your prompts influenced the generated code and which adjustments improved the results.

---

## F]  Additional Resources

### Articles

* [GitHub Copilot](https://docs.github.com/en/copilot) – Official documentation for installing, configuring and using Copilot.
* [How to Write Better Prompts for GitHub Copilot](https://github.blog/2023-09-12-how-to-write-better-prompts-for-github-copilot/) – A GitHub blog post with best practices for crafting clear, specific prompts.


### Videos

The following videos provide hands‑on demonstrations of AI coding tools.  Verify the dates and quality before sharing with your team:

| Topic                | Video Title                                         | Link                                                                    | Description                                                                 |
|----------------------|-----------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Copilot Beginner     | *How to Use GitHub Copilot (Beginner-friendly)*     | [Watch](https://www.youtube.com/watch?v=n0NlxUyA7FI)                    | Demonstrates installation and basic usage of Copilot in VS Code.            |
| Copilot Tips & Tricks | *Get the Most Out of GitHub Copilot – ng-conf 2024* | [Watch](https://youtu.be/bBpHGUn-O5U?si=u-LJ-D1vD0pUEbq5)                    | Offers practical tips on prompting, refactoring and code review.           

---

## G]  Summary

By following this training plan, you will learn how to install and enable GitHub Copilot using the Programmers.ai enterprise licence, configure optional features like Copilot Chat and Agentic mode, and leverage algorithmic thinking to craft effective prompts.  Practising with the exercises in the accompanying repository will help solidify these skills.  Remember to review all AI‑generated code carefully, ensure it meets your organisation’s quality standards, and iteratively refine your prompts for the best results.
