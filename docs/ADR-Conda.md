# ADR - Selection of Conda for Environment Management

**Date:** 11-11-2024

**Status:** Accepted

## Context

This project involves optimizing turbine maintenance and energy production. The core task requires using optimization libraries (like Scipy, PuLP, Pyomo), alongside other packages such as NumPy, Pandas, and Matplotlib. Managing these dependencies efficiently is critical for ensuring reproducibility, avoiding version conflicts, and enabling a smooth development and deployment process.

## Decision

Conda was selected as the environment and package manager for this project for the following reasons: 
- Comprehensive Package Management: Conda is a powerful tool for managing both Python and non-Python dependencies, which is crucial given that this project may require system-level dependencies.
- Reproducibility: By using Conda, we ensure that the project's dependencies are captured in environment files (environment.yml), making it easy to reproduce the exact environment on different machines, whether for other team members or for deployment.
- Cross-Platform Compatibility: Conda is cross-platform and can be used on Windows, macOS, and Linux.
- Ecosystem Integration: Conda integrates well with the Python ecosystem and supports a wide variety of data science, scientific computing, and optimization libraries, which are key for this project (e.g., Scipy, Pandas, Matplotlib).

## Consequences

Positive:
- Easy environment setup and dependency management for all team members.
- Better compatibility with packages that require non-Python dependencies (e.g., C extensions or system libraries).
- Reproducibility across different systems.
- Simplified onboarding process for new developers or contributors.

Negative:
- Conda environments can be large, and there may be some initial overhead in setting up environments and solving dependencies.
- There may be some additional time required for understanding Conda for team members unfamiliar with it.
