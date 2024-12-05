# ADR - Optimization Method for Maintenance Cost Minimization

**Date:** 11-17-2024  
**Status:** Accepted  

## Context

The project involves optimizing turbine maintenance costs while ensuring operational efficiency and uptime. The primary cost components include:
1. **Internal Maintenance Cost**: A fixed cost per fault type.
2. **External Maintenance Cost**: A variable cost per trip, depending on the season.
3. **Preventative Maintenance Cost**: A fixed cost per fault type that reduces the likelihood of faults by 60%.

The objective is to minimize the total maintenance cost by deciding:
- Which faults should be handled by internal maintenance.
- Which faults should require external maintenance trips.
- Whether preventative maintenance should be applied to reduce fault occurrences.

## Decision

To solve this optimization problem, we chose to implement a **constraint optimization model** using **linear programming**. The following tools and methods were applied:
- **Tools**: The optimization was implemented using the **PuLP** library, which is well-suited for solving linear and mixed-integer linear programming problems.
- **Variables**:
  - **Internal Maintenance**: Binary variable for each fault type.
  - **External Trips**: Binary variable for each fault type on each day.
  - **Preventative Maintenance**: Binary variable for each fault type.
- **Objective**:
  - Minimize the total cost, which includes internal, external, and preventative maintenance costs:
    \[
    \text{Total Cost} = \text{Internal Cost} + \text{External Cost} + \text{Preventative Maintenance Cost}
    \]
- **Constraints**:
  1. **Maintenance Requirement**: Each fault type must be addressed either through internal maintenance, external maintenance, or reduced by preventative maintenance.
  2. **Fault Reduction**: Preventative maintenance reduces faults by 60%.
  3. **Daily Trip Limit**: For each fault type on a specific day, at most one external trip is allowed.
  4. **Monthly Reset**: Fault tracking resets at the start of each month to ensure no carryover between months.

## Consequences

**Positive:**
- Provides a systematic and scalable framework for balancing maintenance costs and operational efficiency.
- Accounts for seasonal demand variations and fault reduction due to preventative maintenance.
- Ensures reproducibility and flexibility by using an open-source optimization library (PuLP).
- Facilitates strategic decision-making by exploring trade-offs between maintenance types.

**Negative:**
- Requires expertise in linear programming for proper implementation and troubleshooting.
- Increased computational complexity for larger datasets or additional constraints.

---

This optimization method ensures a robust and cost-effective maintenance strategy by balancing internal, external, and preventative maintenance decisions. Future improvements may include incorporating stochastic modeling to handle uncertainty in fault occurrences or seasonal variations.  
