# Business Requirements Document (BRD)

## Project: Student Performance Dashboard

### Overview

Our organisation would like to build a **Student Performance Dashboard** as a module inside our internal Learning Management System (LMS).  This dashboard should provide instructors and administrators with insights into student grades, attendance and progress over time.  The module will fetch data from existing databases, process it and display interactive charts and tables.  Future iterations may include predictive analytics.

### Goals

1. **Consolidate Data** – Aggregate grades and attendance records from multiple sources into a unified model.
2. **Compute Metrics** – Calculate averages, medians, maximums and grade distributions for classes and individual students.
3. **Expose API** – Provide endpoints to access processed metrics for integration with the LMS front end.
4. **Generate Reports** – Produce downloadable PDF or CSV reports summarising performance at class and student levels.
5. **Document the Design** – Create comprehensive documentation and diagrams of the data model, API endpoints and processing pipeline.

### Functional Requirements

* **FR1** – The system shall ingest student data from the `students`, `grades`, and `attendance` tables in the SQL database.
* **FR2** – The system shall compute statistical measures (mean, median, maximum) for each student and each assignment.
* **FR3** – The system shall categorise grade percentages into letter grades (A–F) and produce distributions for each class.
* **FR4** – The system shall expose REST endpoints for retrieving aggregated metrics per class (`/api/classes/{class_id}/metrics`) and per student (`/api/students/{student_id}/metrics`).
* **FR5** – The system shall allow administrators to download a report in CSV format summarising class performance.
* **FR6** – The system shall include comprehensive API documentation using the OpenAPI/Swagger specification.

### Non‑Functional Requirements

* **NFR1** – All computations shall complete within two seconds for classes of up to 1,000 students.
* **NFR2** – The system shall comply with our data privacy policy by not exposing personally identifiable information.
* **NFR3** – The codebase shall include unit tests achieving at least 80 % coverage of core logic.
* **NFR4** – Documentation shall be written in Markdown and include Mermaid diagrams illustrating the data flow and entity relationships.

### Acceptance Criteria

1. All REST endpoints return HTTP 200 responses with correct JSON payloads when supplied with valid IDs.
2. PDF or CSV reports correctly reflect the computed metrics and adhere to the approved template.
3. Unit tests run successfully and cover edge cases such as missing grades or attendance records.
4. Developers and administrators can understand the architecture via the provided diagrams and documentation.

### Use Case Scenario

*Professor Lee logs into the LMS to check her class’s performance.  She navigates to the Student Performance Dashboard and selects her Class ID.  The dashboard displays a bar chart of grade distribution and a table listing each student’s average score and attendance rate.  She clicks on a student’s name to view that student’s detail page, which lists assignments, scores and progress over time.  Satisfied with the overview, Professor Lee exports a CSV report to share with her department head.*