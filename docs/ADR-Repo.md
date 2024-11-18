# Architecture Decision Record (ADR)

## Title: Repository Structure for BUSI732_F24_Team3

**Date:** November 17, 2024  
**Status:** Accepted  

---

## Context

The **BUSI732_F24_Team3** repository is intended for a collaborative project that involves data analysis, model development, and reporting. A well-organized structure is necessary to:

- Streamline collaboration among team members.
- Ensure clear separation of concerns within the project.
- Maintain scalability and clarity as the project grows.
- Support reproducibility and version control best practices.

---

## Decision

The repository is structured as follows:

### Root-Level Files
- **`.gitignore`**: Ensures that temporary files, logs, and sensitive information are excluded from version control.
- **`README.md`**: Provides an overview of the repository, including the project's objectives, instructions for use, and contact information.
- **`environment.yml`**: Defines a reproducible environment using Conda. It lists all required libraries and dependencies to ensure uniformity across team members' environments.

### Directories
#### **`data/`**
- Purpose: Stores all datasets used in the project.
- Structure:
  - `raw/`: Contains unprocessed datasets obtained from external sources.
  - `processed/`: Stores data that has been cleaned, transformed, or otherwise prepared for analysis.
- Reason: Keeps the raw data intact for reproducibility while organizing processed data separately to avoid confusion.

#### **`docs/`**
- Purpose: Houses all project-related documentation.
- Structure:
  - `design/`: Includes design documents, diagrams, or architectural outlines.
  - `references/`: Contains external resources, research papers, or guidelines referenced during the project.
- Reason: Ensures that documentation is easily accessible to team members and stakeholders.

#### **`models/`**
- Purpose: Stores machine learning or statistical models created during the project.
- Structure:
  - `saved_models/`: Holds serialized models (e.g., `.pkl` or `.h5` files) for deployment or further use.
  - `training_scripts/`: Includes scripts used to train the models.
- Reason: Centralizes all models and their related scripts for easy access and version control.

#### **`notebooks/`**
- Purpose: Contains Jupyter notebooks used for exploratory data analysis, prototyping, and visualization.
- Structure:
  - `eda/`: Notebooks focused on exploring and understanding datasets.
  - `experiments/`: Notebooks testing hypotheses or trying different models.
- Reason: Encourages an iterative workflow and keeps exploratory work separate from production code.

#### **`reports/`**
- Purpose: Stores deliverables such as generated reports, summaries, and presentations.
- Structure:
  - `visualizations/`: Includes charts, graphs, or other visual elements used in reports.
  - `final/`: Contains finalized reports ready for submission or presentation.
- Reason: Maintains a clear history of both intermediate and final reporting efforts.

#### **`src/`**
- Purpose: Contains all source code used for implementing the project's main functionality.
- Structure:
  - `data_processing/`: Scripts for cleaning and transforming raw data.
  - `analysis/`: Scripts for statistical and machine learning analysis.
  - `utils/`: Reusable utility scripts for common operations.
- Reason: Keeps code modular and well-organized, separating different functionalities into specific subdirectories.

---

## Rationale

- **Clarity**: Each directory has a dedicated purpose, reducing ambiguity and enhancing navigation.
- **Collaboration**: A standardized layout ensures all team members understand the structure and can work efficiently.
- **Scalability**: Modular design supports adding new components without disrupting existing workflows.
- **Reproducibility**: By separating raw data, processed data, and environment configurations, the structure supports consistent replication of results.

---

## Consequences

- **Positive**: This structure will promote better organization, improve collaboration, and reduce development time by providing a clear framework for the team to follow.
- **Negative**: Initial setup may require effort to establish and communicate the structure to all team members, but this cost is outweighed by long-term benefits.

---

## Status Updates

This structure is subject to review and adjustments as the project evolves. Feedback from team members will inform any necessary changes.

---
