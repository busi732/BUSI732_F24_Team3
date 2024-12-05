# ADR - Decision to Not Use DVC for Version Control

**Date:** 12-4-2024  
**Status:** Proposed  

## Context

Data Version Control (DVC) is a tool designed for managing datasets, models, and machine learning pipelines. It integrates with Git to provide version control for large files and track changes in data and machine learning experiments. While DVC offers several advantages, its integration and usage add complexity to the repository management process. 

Our team considered adopting DVC for this project but decided against it due to specific reasons related to the project scope, timeline, and team expertise.

## Decision

We decided **not to use DVC** for managing datasets and experiments in this project. Instead, we will rely on the following methods for versioning and tracking:
- Storing raw, processed, and final datasets in a clearly structured folder hierarchy (`data/`).
- Using Git for tracking code, environment configurations, and documentation.
- Explicitly documenting experiment results and model artifacts in the `reports/` directory.

## Reasons for the Decision

1. **Project Scope and Complexity**:
   - The project's dataset size and complexity are manageable without DVC.
   - Using DVC would add unnecessary setup time and overhead for a small-to-medium-sized project like ours.

2. **Team Expertise**:
   - Not all team members are familiar with DVC.
   - Introducing DVC would require training and adjustment, which is not feasible within the current project timeline.

3. **Additional Infrastructure**:
   - DVC often requires integration with remote storage backends (e.g., AWS S3, Google Drive) for effective data management.
   - Setting up and managing these integrations adds complexity, especially when our current storage solutions are sufficient.

4. **Sufficient Alternatives**:
   - Our repository structure already separates raw, processed, and final datasets in the `data/` directory.
   - Experiment results and model artifacts can be manually tracked and documented without significant overhead.

5. **Timeline Constraints**:
   - Implementing DVC and updating the workflow would require additional time that could be better spent on optimizing the model and analysis.

## Consequences

**Positive:**
- Simplifies the repository and workflow by avoiding the additional complexity of DVC.
- Reduces the learning curve and technical debt for the team.
- Saves setup and configuration time, allowing us to focus on project deliverables.

**Negative:**
- Manual tracking of data and experiment changes may introduce the risk of human error.
- Limited support for automated tracking and versioning of datasets and models compared to DVC.

---

This decision aligns with the project's scope and timeline while balancing the trade-offs between complexity and functionality. In future, larger-scale projects with more complex data pipelines or collaborative needs, adopting DVC may be reconsidered.  
