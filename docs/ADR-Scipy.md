# ADR: Selection of Scipy for Optimization Task

**Date:** 11-11-2024

**Status:** Proposed

## Context
The task at hand is to optimize the maintenance schedule and energy production for a wind turbine located in Texas within the ERCOT region. The optimization problem involves minimizing maintenance costs (both internal and external), managing failure rates, and maximizing energy production and revenue, while adhering to constraints like pre-sold energy and seasonal demand. This requires an optimization library that can efficiently handle the problem's non-linear and constrained nature.

Three potential libraries have been considered for solving the optimization problem:

- Scipy (scipy.optimize)
- PuLP
- Pyomo

## Decision
Scipy has been selected as the optimization library for this project. The reasons for this decision are as follows:

- Problem Fit: While the problem involves some integer decision variables (such as the number of maintenance trips and whether to perform preventative maintenance), the majority of the optimization is focused on continuous variables (such as energy production and maintenance costs). Scipy provides excellent support for these types of problems and can efficiently handle non-linear constraints.
- Simplicity: Scipy’s API is clean and integrates well into the existing codebase without the need for complex solver configurations or external dependencies. For this project, we value ease of use and the ability to quickly test and refine the optimization model.
- Performance: For the scale of the problem (a single turbine and a single year of data), Scipy’s solvers are expected to perform well. If performance issues arise, we can consider moving to a more robust solution like Pyomo.
-  Simplicity and Community Support: Scipy is widely used within the scientific and engineering communities, and it has extensive documentation and tutorials. This makes it an ideal choice for teams with new members or those not deeply familiar with optimization. Its integration with the broader Python ecosystem also means that developers can easily collaborate and troubleshoot issues.

## Alternatives Considered
1. PuLP
Strengths:
- PuLP provides a user-friendly, high-level interface for linear programming and mixed-integer programming. It is built around linear and integer optimization problems.
- PuLP integrates well with open-source solvers. This flexibility in solver choice allows us to scale based on problem complexity.
- PuLP has extensive documentation and a large user base, which makes it easy to troubleshoot and find solutions to common problems.

Weaknesses:
- PuLP is primarily focused on linear and mixed-integer linear programming problems. It doesn't have robust support for non-linear optimization problems, which may be a limitation for non-linear relationships or constraints (e.g., non-linear failure costs or maintenance schedules).

2. Pyomo
Strengths:
- Pyomo is highly flexible and used across various domains for optimization, making it a highly robust and scalable choice for industrial-level problems.
- Pyomo is well-suited for both linear and mixed-integer programming problems.

Weaknesses:
- Pyomo has a steeper learning curve and is more complex than other libraries like Scipy and PuLP. Setting up a problem in Pyomo might require more code and understanding of solver interfaces.
- Like PuLP, Pyomo requires external solvers for mixed-integer programming, which can add overhead in terms of setup, installation, and solver licensing.

## Consequences
**Positive:** We will have a quick and simple implementation using Scipy's optimization tools, with the flexibility to handle non-linear and constrained optimization efficiently. Its widespread usage means that new team members can quickly get up to speed and contribute to the project.

**Negative:** If the problem scales up (e.g., involving more turbines or a larger dataset), we may need to explore more powerful libraries like Pyomo or PuLP, especially for mixed-integer optimization.

## Implementation

### Minimizing Hired Personnel Cost:
**Objective:** Contribute to minimizing maintenance cost by deciding between internal and external maintenance.

Use Scipy's `minimize` function to find the optimal allocation between internal and external maintenance, while considering constraints like available resources, maintenance schedules, and seasonal demand.

- Inputs: Expected maintenance needs, historical data on internal vs external maintenance costs, seasonal demand.
- Outputs: The optimal decision between internal and external maintenance to minimize costs.

### Minimizing Outage-Based Maintenance Cost:
**Objective:** Minimize overall maintenance costs by deciding between corrective and preventative maintenance. 

- Inputs: EMaintenance failure rates, downtime costs, and preventative maintenance success rate. 
- Outputs: The optimal decision between preventative and corrective maintenance to minimize costs.
