## ADR: Adoption of pyenv in Wind Turbine Optimization

**date:** [11/16/2024]

**status:** Approved

## Context: 

The wind turbine optimization project involves developing a financial and operational efficiency model using Python. The project requires multiple Python libraries and tools, some of which may depend on specific Python versions. 
Managing Python versions manually can lead to errors, such as conflicts between libraries or using an unsupported Python version for a critical library. To streamline development and ensure project consistency, we need a tool to manage Python versions efficiently and flexibly.

## Decision: 

We will adopt pyenv as the primary tool for Python version management for the wind turbine optimization project.

## Rationale: 

We have chosen pyenv because it allows seamless installation and switching between Python versions, ensuring compatibility with the libraries and tools used in the wind turbine optimization project. It supports project-specific Python configurations, enabling consistency across diverse development environments, including Linux, macOS, and Windows (via pyenv-win). With its intuitive interface and integration with virtual environment tools like venv, pyenv minimizes setup complexity while ensuring isolation and stability. Additionally, it simplifies adopting new Python versions in the future, making it a flexible and future-proof solution for managing Python versions across the team.

## consequences

* Positive:
  - Ensures all team members use the same Python version across development and production.Reduces risk of dependency conflicts and incompatibility issues.
  - Simplifies onboarding for new developers by standardizing the Python setup.
  - Provides flexibility for testing code compatibility across multiple Python versions.
* Negative:
  - Team members unfamiliar with pyenv may need initial guidance.
  - Adds a dependency on an external tool, requiring occasional updates to pyenv.
