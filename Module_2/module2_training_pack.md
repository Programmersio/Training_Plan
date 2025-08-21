# Module 2 Training – Foundations of AI Tooling & AI Review

## Overview

Module 2 builds on the mindset shift introduced in Module 1.  It focuses on the practical foundations of using AI coding assistants and reviewers, primarily **GitHub Copilot** and **Roo Code**, and introduces best practices for static and dynamic code review.  The goal is to prepare developers to select the right tool for the task, craft effective prompts, orchestrate multi‑file refactorings and validate AI‑generated code.

This document contains:

1. **Theory and examples** outlining key concepts (AI tooling spectrum, indexing and chat workspace, static vs dynamic review, Copilot vs agents) with illustrations and anecdotes.
2. **Labs and tasks** (four hands‑on labs) with step‑by‑step instructions for using Copilot and Roo Code in real scenarios.
3. **Assessment plan** with quizzes and reflection templates.


Feel free to modify file paths and task names to match your repository structure.  All files referenced here are located in the `module2` directory.

---

## 1. Theory and Key Concepts

### 1.1 The AI Tooling Spectrum

AI coding assistants span a range from simple autocompletion to autonomous agents.  Understanding where Copilot and Roo Code fit on this spectrum helps you choose the right tool:

| Category | Description | Examples |
| --- | --- | --- |
| **Assistive Autocomplete** | Suggests the next few tokens based on local context. | GitHub Copilot inline completions, VS Code IntelliSense |
| **Contextual Assistant** | Consumes the entire file or selection to offer coherent functions, refactors or documentation. | Copilot Chat, Roo Code Ask/Doc modes |
| **Agentic Assistant** | Plans and executes multi‑step tasks across files, such as migrating code or scaffolding projects. | Roo Code Architect mode, Copilot Agents in Visual Studio |
| **Autonomous Coder** | Capable of orchestrating complex workflows end‑to‑end with minimal human intervention. | Experimental agents; emerging research |

Moving from left to right increases power but also risk.  More advanced modes require careful review.

### 1.2 Indexing and Chat Workspace

Roo Code relies on an **index** of your workspace to understand file names, symbol definitions and relationships.  Before running large tasks or using Ask mode:

1. Open the project in VS Code.
2. Run **“Roo Code: Index Workspace”** from the Command Palette.  The index is stored locally and can be refreshed at any time.
3. In the Roo Code panel, you can see indexed files and search for symbols.

The **chat workspace** is where you interact with the model.  Each new prompt opens a chat window.  For long conversations, you may need to start a fresh chat to avoid context bloat.  See the Labs for examples of when to switch chats.

### 1.3 Static vs Dynamic Review

AI tools can generate working code, but they cannot guarantee correctness or style compliance.  Combine multiple forms of review:

| Review Type | Tools & Techniques | Detects |
| --- | --- | --- |
| **Static Analysis** | Linters (`flake8`, `pylint`), type checkers (`mypy`), security scanners. | Dead code, style issues, missing type hints, simple vulnerabilities. |
| **Dynamic Testing** | Unit tests with `pytest`, integration tests, property‑based testing. | Runtime errors, incorrect outputs, edge cases. |
| **Manual Review** | Code reviews, pair programming, design discussions. | Architecture flaws, business logic errors, readability, maintainability. |

Use static checks early to catch low‑hanging issues, then run tests to validate behaviour.  Combine results with your domain knowledge.

### 1.4 Copilot vs Agents

GitHub Copilot excels at **inline completions** and simple functions within a file.  It uses surrounding code as context and suggests single functions or loops.  Agents, such as Roo Code Architect or Copilot in Agentic mode, can:

- Read and write multiple files.
- Plan refactoring steps (rename symbols, extract methods, scaffold projects).
- Execute commands (e.g. running tests) and iterate.

However, agents operate like an intern: they require clear instructions, supervision and acceptance of changes.  They are best for repetitive or large tasks, while Copilot is ideal for quick scaffolding.

#### Example

**Copilot scenario:** You need to implement `calculate_student_statistics`.  A detailed comment including algorithm complexity yields a clean function suggestion.  Copilot’s suggestion is immediate and easy to accept after minor tweaks.

**Agent scenario:** You need to rename a class across a monorepo.  Roo Code’s agentic mode creates a plan, highlights all occurrences, applies changes and updates imports.  You review the diffs before committing.

### 1.5 Best Practices

1. **Start small:** Use Copilot for simple functions; move to agents when tasks span multiple files or require repeated edits.
2. **Write clear prompts:** Provide roles, tasks, inputs/outputs, algorithm constraints and examples.  See Lab 3 for practice.
3. **Index often:** Keep Roo Code’s index up to date so that it can find symbols quickly and avoid stale references.
4. **Review everything:** Treat AI suggestions as drafts.  Use linters, tests and manual review to catch mistakes.
5. **Manage chat sessions:** When a conversation becomes long, open a new chat to avoid outdated context.  Use explicit file references in prompts.

---

## 2. Labs and Tasks

There are four labs in this module.  Each lab has its own step‑by‑step instructions in the `labs` folder:

| Lab | Focus | Key Skills |
| --- | --- | --- |
| [Lab 1](labs/lab1.md) | Using GitHub Copilot | Generating functions, API clients, running unit tests |
| [Lab 2](labs/lab2.md) | Refactoring with Roo Code | Indexing, renaming classes, merging functions, splitting long methods |
| [Lab 3](labs/lab3.md) | Prompt Engineering Drills | Writing precise prompts, algorithm specification, documentation & diagrams |
| [Lab 4](labs/lab4.md) | Static & Dynamic Review | Linting, test coverage, code review, comparing static vs dynamic feedback |

Each lab ends with reflection questions to encourage critical thinking about the AI’s output and your role in supervising it.

---

## 3. Assessment Plan

### 3.1 Quiz

The file **`assessments/quiz.md`** contains multiple‑choice and short‑answer questions.  Example topics include:

1. **Tool differentiation:** Contrast Copilot and Roo Code in terms of scope and capabilities.
2. **Indexing:** Explain how indexing improves Roo Code’s performance.  What happens if you forget to reindex after significant changes?
3. **Prompt structure:** Identify the seven components of a well‑structured prompt and demonstrate with an example.
4. **Static vs dynamic review:** Describe scenarios where static analysis might detect issues that dynamic testing misses, and vice versa.
5. **AI risks:** Discuss potential risks of using agentic tools without proper oversight.

### 3.2 Reflection Template

Developers complete **`assessment_reflection.md`** after finishing the labs.  They should:

1. **Summarise** the tasks they performed.
2. **List effective prompts** they crafted, including variants that improved results.
3. **Identify challenges** encountered, such as ambiguous outputs, tooling limitations, or environment issues.
4. **Propose improvements** to prompts, workflows or tool features.
5. **Consider adoption**: Would they use Copilot/Roo Code in daily work?  What guidelines would they share with colleagues?

### 3.3 Evaluation

Trainers or team leads can review quiz answers and reflection documents.  Success criteria may include:

- Score ≥ 80% on the quiz.
- Demonstrated understanding of indexing, prompt engineering and review principles.
- Meaningful reflections showing critical thinking about AI‑generated code.

---


## 4. Files Included

This training pack includes the following files:

- **module2_training_pack.md** – The document you are reading, containing theory, labs and assessments..
- **labs/lab1.md** – Step‑by‑step instructions for using GitHub Copilot to generate functions and API clients.
- **labs/lab2.md** – Step‑by‑step instructions for performing repository‑wide refactors with Roo Code.
- **labs/lab3.md** – Prompt engineering drills including algorithm implementation, grouping functions and documentation generation.
- **labs/lab4.md** – Static and dynamic review tasks for verifying AI‑generated code.
- **assessments/quiz.md** – A quiz for evaluating knowledge of the module.
- **assessment_reflection.md** – A template for learners to summarise their experience and list effective prompts.
- **slides/module2.pptx** – The summary slide deck for Module 2 (see `Module_2/slides/module2.pptx`).
- **Slides/** – Detailed slide decks for each module (see `Slides/` at the root of the repository).

Use this package as the foundation for your training sessions on AI‑augmented development.
