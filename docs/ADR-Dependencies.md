# ADR: Selecting Dependencies and Python 3.8 for Conda Environment

**Date:** 12-10-2024

**Status:** Accepted

## Context

The Conda environment for this project includes specific dependencies and the Python 3.8 version. The choice of these packages is guided by the requirements of the project, ensuring compatibility, functionality, and efficiency.

## Decision

We selected the following dependencies to support the project's functionality:

1. **`ipykernel`**: Enables the integration of Jupyter notebooks with IPython kernels, essential for interactive data analysis and visualization.
2. **`jupyter`**: Provides the core framework for creating and running Jupyter notebooks, which are central to our workflow.
3. **`matplotlib`**: A powerful plotting library for creating a wide range of static, animated, and interactive visualizations.
4. **`notebook`**: Supplies the Jupyter Notebook server for managing and executing notebook files.
5. **`numpy`**: A fundamental package for numerical computing, used for array operations and mathematical functions.
6. **`pandas`**: A library for data manipulation and analysis, offering data structures like DataFrames and Series.
7. **`python=3.8`**: Selected specifically for compatibility with the `dataprep` library, which does not yet support Python 3.11.
8. **`dataprep`**: Simplifies data preparation, cleaning, and exploratory data analysis, crucial for efficient data workflows.
9. **`pyarrow-hotfix`**: Provides compatibility fixes related to Apache Arrow, enabling efficient in-memory data processing.
10. **`openpyxl`**: A library for working with Excel files, required for reading, writing, and manipulating `.xlsx` files.

## Reasons for Decision

1. **Compatibility with `dataprep`**:
   - The `dataprep` library is critical for automating data cleaning and preparation tasks.
   - To ensure compatibility with `dataprep`, Python 3.8 was chosen, as it is supported by the library.

2. **Comprehensive Toolset**:
   - The selected libraries collectively provide a complete ecosystem for data analysis, visualization, and preparation.

3. **Efficiency and Flexibility**:
   - Libraries like `numpy` and `pandas` enable efficient manipulation of large datasets, while `matplotlib` ensures high-quality visualizations.

## Consequences

### Positive
- A robust environment tailored to the project's data analysis and preparation needs.
- Compatibility with the `dataprep` library, ensuring smooth workflows.

### Negative
- Use of Python 3.8 limits access to some features and libraries available in newer Python versions.

## Status

**Adopted**: This configuration has been implemented and is successfully supporting the project's requirements.

## Future Considerations

- Monitor updates to `dataprep` for compatibility with newer Python versions.
- Periodically review dependencies to optimize for performance and functionality.
