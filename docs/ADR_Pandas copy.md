## ADR: Adoption of Pandas in Wind Turbine Optimization

**date:** [12/11/2024]

**status:** Approved

## Context

The team is tasked with developing a data processing pipeline for analyzing and transforming large datasets related to the **WindTurbin product**. The pipeline requires capabilities such as:

- Efficient data manipulation (e.g., filtering, aggregations, joins).
- Support for various file formats (e.g., CSV, Excel, Parquet).
- Scalability to handle datasets ranging from a few megabytes to several gigabytes.
- A user-friendly API to reduce the learning curve for new developers.

The primary decision is whether to use **Pandas**, a popular Python library for data manipulation, or explore alternative tools such as **Dask**, **PySpark**, or **SQL-based approaches**.

## Decision

We have decided to use **Pandas** as the primary tool for our data processing needs.

## Alternatives Considered

### 1. **Dask**
- **Pros:**
  - Scales better for larger-than-memory datasets.
  - Similar API to Pandas, easing the transition for experienced Pandas users.
  - Supports parallel and distributed computation.
- **Cons:**
  - Increased complexity in debugging and setup.
  - Performance overhead for smaller datasets due to task scheduling.

### 2. **PySpark**
- **Pros:**
  - Excellent for distributed computing across large clusters.
  - Integrated with the Hadoop ecosystem and supports SQL-like queries.
- **Cons:**
  - Steeper learning curve compared to Pandas.
  - Overhead in serialization/deserialization for Python users.
  - Requires additional infrastructure for cluster management.

### 3. **SQL-Based Approaches**
- **Pros:**
  - Well-suited for relational data.
  - Can leverage existing database systems (e.g., PostgreSQL, Snowflake).
- **Cons:**
  - Limited flexibility for non-tabular data structures.
  - Requires a combination of SQL and another programming language for complex workflows.

## Rationale

### Why Pandas?
1. **Ease of Use:**
   - Pandas provides an intuitive and user-friendly API for data manipulation.
   - A large amount of community documentation and tutorials exist, reducing the onboarding time for new team members.

2. **Versatility:**
   - Supports a wide variety of file formats and data sources out of the box.
   - Extensive support for handling missing data and reshaping datasets.

3. **Performance for Small-to-Medium Datasets:**
   - For datasets that fit into memory, Pandas offers high performance with minimal setup.

4. **Community and Ecosystem:**
   - A large and active user base ensures continuous updates and the availability of third-party extensions.
   - Seamless integration with popular Python libraries such as NumPy, Matplotlib, and Scikit-learn.

### Why Not Alternatives?
- **Dask and PySpark** introduce overhead and complexity that are unnecessary for our current dataset sizes.
- **SQL-based approaches** lack the flexibility needed for advanced data transformations.

## Consequences

### Positive:
- Faster implementation due to familiarity with the Pandas API.
- Efficient processing of datasets within the current memory limits.
- Reduced learning curve for new developers joining the project.

### Negative:
- Potential limitations if dataset sizes grow beyond available memory.
- Single-threaded performance bottlenecks may arise in specific use cases.
- Migration to a scalable tool like Dask or PySpark may be required in the future.

## Mitigation Plan

- Monitor dataset sizes and performance metrics as the project evolves.
- Document code with scalability in mind to ease future migration.
- Provide training for team members on alternative tools like Dask and PySpark to prepare for potential scaling needs.