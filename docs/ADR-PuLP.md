# ADR: Selection of PuLP for Optimization Task

**Date:** 12-11-2024

**Status:** Accepted

## Context
The task at hand is to optimize the maintenance schedule and energy production for a wind turbine located in Texas within the ERCOT region. The optimization problem involves minimizing maintenance costs (both internal and external), managing failure rates, and maximizing energy production and revenue, while adhering to constraints like pre-sold energy and seasonal demand. This requires an optimization library that can efficiently handle the problem's non-linear and constrained nature.

Three potential libraries have been considered for solving the optimization problem:

- Scipy (scipy.optimize)
- PuLP
- Pyomo

## Decision
The task at hand is to optimize the maintenance schedule and energy production for a wind turbine located in Texas within the ERCOT region. The optimization problem involves minimizing maintenance costs (both internal and external), managing failure rates, and maximizing energy production and revenue, while adhering to constraints like pre-sold energy and seasonal demand. This requires an optimization library that can efficiently handle both linear and mixed-integer linear programming problems.

Three potential libraries have been considered for solving the optimization problem:

Scipy (scipy.optimize)
PuLP
Pyomo
Decision

PuLP has been selected as the optimization library for this project. The reasons for this decision are as follows:

Problem Fit: The optimization problem involves mixed-integer decision variables (such as the number of maintenance trips and whether to perform preventative maintenance) and linear relationships (e.g., cost structures, scheduling). PuLP excels in handling mixed-integer linear programming (MILP) problems, which makes it well-suited for this task.
While Scipy's strength lies in non-linear problems, PuLP offers a better fit for problems with discrete decision variables (such as choosing between internal and external maintenance) and linear constraints.
Simplicity: PuLP provides a high-level, easy-to-use interface for linear programming and MILP that integrates well with open-source solvers like CBC, CPLEX, and GLPK.
The simplicity of setting up linear models in PuLP, combined with its user-friendly syntax, allows for quick testing and model iteration. The library also has good documentation and a large user base, making it easy for team members to collaborate.
Performance: For this problem, which involves mixed-integer decisions and linear constraints, PuLP is expected to perform efficiently at the scale of a single turbine and a single year of data. PuLP can handle reasonably large MILP problems, and if the problem scales up, additional solver configurations (like CPLEX or Gurobi) can be explored for better performance.
Community Support: PuLP has extensive documentation, a wide user base, and active community support, making it easy to troubleshoot and resolve issues. It integrates well with solvers like CBC (an open-source solver) and is compatible with the broader Python ecosystem.

## Alternatives Considered
1. Scipy
Strengths:
- Scipy is excellent for continuous optimization problems and can handle some integer decision variables. It is often used for scientific and engineering optimization tasks.

Weaknesses:
- Scipy is not designed for mixed-integer problems and doesn’t natively support linear programming or MILP as efficiently as PuLP.
- For mixed-integer programming (like choosing between internal/external maintenance), Scipy would require additional custom code, making it less practical for this problem.

2. Pyomo

Strengths:
- Pyomo is highly flexible and used across various domains for optimization, making it a highly robust and scalable choice for industrial-level problems.
- Pyomo is well-suited for both linear and mixed-integer programming problems.

Weaknesses:
- Pyomo has a steeper learning curve and is more complex than other libraries like Scipy and PuLP. Setting up a problem in Pyomo might require more code and understanding of solver interfaces.
- Like PuLP, Pyomo requires external solvers for mixed-integer programming, which can add overhead in terms of setup, installation, and solver licensing.

## Consequences
**Positive:** PuLP’s high-level interface and easy integration with open-source solvers will allow for quick and simple implementation. The simplicity of setting up the optimization model ensures that the team can focus on refining the model and running tests. If the problem scales (e.g., more turbines or a larger dataset), PuLP can efficiently handle the problem using MILP solvers. We can also scale performance by swapping to more powerful solvers if needed.

**Negative:** If the problem includes non-linear constraints, PuLP would be less suited for those aspects, as it is not optimized for non-linear programming. In such cases, we might need to switch to more specialized libraries (e.g., Pyomo) for handling complex non-linear optimization.

## Implementation

### Minimizing Hired Personnel Cost:

**Objective:** Contribute to minimizing maintenance cost by deciding between internal and external maintenance.

Use PuLP to model the problem as a linear program. The decision variables will include whether to use internal or external maintenance services, while the objective is to minimize the total maintenance cost subject to constraints on availability of resources and seasonal demand.

- Inputs: Expected maintenance needs, historical data on internal vs. external maintenance costs, seasonal demand.
- Outputs: The optimal allocation between internal and external maintenance to minimize costs.

### Minimizing Outage-Based Maintenance Cost:

**Objective:** Minimize overall maintenance costs by deciding between corrective and preventative maintenance. 

- Inputs: EMaintenance failure rates, downtime costs, and preventative maintenance success rate. 
- Outputs: The optimal decision between preventative and corrective maintenance to minimize costs.
