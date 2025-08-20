# Module 2 – Foundations of AI Tooling & AI Review

This training pack provides the **content, examples, exercises and assessments** for **Module 2** of the training program.  
It is designed for developers, tech leads, and QA engineers who have completed Module 1 (*Mindset Shift*).  

---

## 1. Module Objective and Outcomes

**Objective:** Enable every team member to confidently use both basic and advanced agentic features of AI coding assistants for complex, multi‑file tasks.

**Outcomes:** By the end of this module, participants will be able to:  
- Distinguish between reactive Copilot suggestions and proactive agentic capabilities.  
- Use indexing to make AI tools repository‑aware.  
- Work in chat workspaces to guide AI through step‑by‑step tasks.  
- Perform static and dynamic reviews of AI output.  
- Orchestrate multi‑lead scenarios and apply best practices for prompt design.  

---

## 2. Core Topics and Examples

### 2.1 AI Tooling Spectrum
| Tool | Description | Practical Example |
|------|-------------|-------------------|
| **GitHub Copilot (reactive)** | Inline code completion & simple chat. Best for boilerplate and known patterns. | Typing a function signature triggers Copilot to suggest a body. |
| **Roo Code (agentic)** | Repository‑wide agent that can refactor, rename, and restructure. | Rename `InvoiceAdd` to `CustomInvoice` across multiple files. |
| **Hybrid workflow** | Combine Copilot for micro‑tasks and Roo Code for macro‑refactoring. | Scaffold a class with Copilot, then refactor with Roo Code. |

**Key takeaway:** Copilot = local assistant, Roo Code = orchestrator.  

### 2.2 Indexing and Repository Awareness
- **Why index?** Without it, AI only sees open files. With it, Roo Code maps the repo.  
- **Example:** After indexing, ask: *“Find duplicate `process_line_item` functions and merge them.”* Roo Code proposes a diff.  

### 2.3 Chat Workspace & Multi‑Lead Scenarios
- Chat workspace enables collaborative, task‑specific dialogue.  
- **Best practices:** break tasks, start new chats, be specific, request explanations.  
- **Example:** Developer A refactors a 500‑line method with Roo Code; Developer B validates tests; Tech Lead reviews diffs with Copilot Chat.  

### 2.4 Static vs Dynamic Review
- **Static:** linting, naming, style checks.  
- **Dynamic:** run tests (Pytest, integration).  
- **Documentation review:** ask AI to explain its code.  

### 2.5 Copilot vs Agent Examples
- **Copilot:** Suggest inline code for parsing CSVs.  
- **Roo Code:** Merge multiple duplicate methods into one and update references repo‑wide.  

---

## 3. Step‑by‑Step Labs
- **Lab 1:** Copilot coding tasks (student stats, normalise scores, API client).  
- **Lab 2:** Roo Code tasks (merge duplicates, rename class, refactor long methods).  
- **Lab 3:** Prompt engineering drills (binary search, group by grade, documentation).  
- **Lab 4:** Static & dynamic review (linting, testing, documentation).  

See `labs/` folder for details.  

---

## 4. Assessment Plan
- **Practical assignment:** Implement & refactor with Copilot and Roo Code.  
- **Quiz:** Concepts of Copilot vs agents, indexing, reviews.  
- **Reflection:** Developers document effective prompts & improvements.  

---

## 5. Files in This Pack
- `module2_training_pack.md` – Full theory, labs and reporting.  
- `labs/lab1.md` … `labs/lab4.md` – Step‑by‑step exercises.  
- `assessments/quiz.md` – Multiple choice & free response questions.  
- `assessment_reflection.md` – Template for self‑reflection.  
- `slides/module2.pptx` – Slide deck with notes.  

---

## 6. Summary
Module 2 is the **bridge from theory to practice**. It equips participants to confidently use GitHub Copilot and Roo Code, harness indexing and chat workspaces, and critically review AI output.

