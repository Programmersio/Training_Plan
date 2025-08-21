# Training Repository for Copilot & RooCode Exercises

This repository accompanies the **GitHub Copilot**, **RooCode**, and **Prompt Engineering** training plans. It contains Python and Java exercises, curated prompts, quizzes, and supporting materials for hands-on AI-assisted coding practice.

## Structure

```
training_repo/
├── README.md                # this file
├── python_examples/         # Python source files for exercises
│   ├── data_processing.py    # functions for statistics and data manipulation
│   ├── file_io.py           # functions for reading and parsing files
│   ├── api_client.py        # skeleton of an HTTP client class
│   ├── model_script.py      # simple classes to model a library system
│   ├── invoice_utils.py     # example for RooCode refactoring
│   ├── customer_utils.py    # example for RooCode refactoring
│   └── __init__.py
├── java_migration/          # Java code demonstrating legacy and modern styles
│   ├── legacy_java/
│   │   └── Example.java     # old Java code using raw collections
│   └── modern_java/
│       └── Example.java     # refactored version with generics and streams
├── requirements/
│   └── BRD.md               # business requirements document
├── tests/                   # unit tests
│   ├── test_data_processing.py
│   ├── test_file_io.py
│   ├── test_invoice_utils.py
│   └── test_customer_utils.py
├── prompt_library.md        # curated prompts for various tasks
├── training_exercises.md    # summary of exercises referencing the training plans
└── demo_scripts.md          # guidance for live demonstrations
```

## How to Use

1. **Clone this repository** locally or open it directly in VS Code.
2. Review the training plans for Copilot, RooCode, and Prompt Engineering (see `../Module 1/training_plans/` and `../Module_2/`).
3. Work through the exercises in `training_exercises.md` using GitHub Copilot or RooCode. Write clear prompts based on the guidelines, then review and iterate on the results.
4. For the Java migration example, examine the difference between the `legacy_java` and `modern_java` versions. Use Copilot’s Agents or RooCode’s Orchestrator Mode to perform the migration yourself.

## Slides

Slide decks for each module are located in the top-level `Slides/` directory. The summary deck for Module 2 is in `Module_2/slides/module2.pptx`.

By completing these exercises you will gain hands-on experience with AI-assisted development and learn how to craft effective prompts.