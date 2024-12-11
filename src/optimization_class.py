from pulp import LpProblem, LpMaximize, LpVariable, lpSum

class MaintenanceOptimization:
    def __init__(self, data, revenue_data, internal_cost=750000, external_normal=50000,
                 external_high_demand=150000, preventative_cost=50000, high_demand_months=None):
        self.data = data
        self.revenue_data = revenue_data
        self.internal_cost = internal_cost
        self.external_normal = external_normal
        self.external_high_demand = external_high_demand
        self.preventative_cost = preventative_cost
        self.high_demand_months = high_demand_months or [1, 2, 6, 7, 8]
        self.problem = None
        self.internal_vars = {}
        self.external_vars = {}
        self.preventative_vars = {}

    def initialize_variables(self, fault_types, days):
        """Initialize optimization variables."""
        self.internal_vars = {f: LpVariable(f"Internal_{f}", 0, 1, cat="Binary") for f in fault_types if f != 'NF'}
        self.external_vars = {
            (f, d): LpVariable(f"External_{f}_{d}", 0, 1, cat="Binary")
            for f in fault_types if f != 'NF' for d in days
        }
        self.preventative_vars = {f: LpVariable(f"Preventative_{f}", 0, 1, cat="Binary") for f in fault_types if f != 'NF'}

    def define_problem(self, fault_types, days):
        """Define the optimization problem with revenue loss during faults."""
        self.problem = LpProblem("Maintenance_Revenue_Maximization", LpMaximize)

        # Total revenue from revenue_data
        total_revenue = lpSum(
            self.revenue_data[self.revenue_data['Day'] == d]['Revenue'].sum()
            for d in days
        )

        # Revenue lost due to faults
        lost_revenue = lpSum(
            self.revenue_data[
                (self.revenue_data['Day'] == d) & (self.data['Fault'] == f)
            ]['Revenue'].sum()
            for f in fault_types for d in days
        )

        # Total maintenance costs
        total_internal_cost = lpSum(self.internal_vars[f] * self.internal_cost for f in fault_types if f != 'NF')
        total_external_cost = lpSum(
            self.external_vars[(f, d)] *
            (self.external_high_demand if self.data[self.data['Day'] == d]['Month'].iloc[0] in self.high_demand_months else self.external_normal)
            for f in fault_types if f != 'NF' for d in days
        )
        total_preventative_cost = lpSum(self.preventative_vars[f] * self.preventative_cost for f in fault_types if f != 'NF')

        # Objective: Maximize revenue minus costs and lost revenue
        self.problem += total_revenue - (total_internal_cost + total_external_cost + total_preventative_cost + lost_revenue)

        # Constraints
        for f in fault_types:
            if f != 'NF':
                for d in days:
                    # At least one maintenance method is required (internal or external)
                    self.problem += (
                        self.internal_vars[f] + self.external_vars[(f, d)] >= 1,
                        f"Maintenance_required_{f}_{d}"
                    )

                    # Prevent internal and external maintenance simultaneously
                    self.problem += (
                        self.internal_vars[f] + self.external_vars[(f, d)] <= 1,
                        f"Exclusive_internal_external_{f}_{d}"
                    )




    def solve(self):
        """Solve the optimization problem."""
        self.problem.solve()

    def get_results(self):
        """Retrieve optimization results."""
        optimized_internal_cost = sum(self.internal_vars[f].varValue * self.internal_cost for f in self.internal_vars)
        optimized_external_cost = sum(
            self.external_vars[(f, d)].varValue *
            (self.external_high_demand if self.data[self.data['Day'] == d]['Month'].iloc[0] in self.high_demand_months else self.external_normal)
            for (f, d) in self.external_vars
        )
        optimized_preventative_cost = sum(self.preventative_vars[f].varValue * self.preventative_cost for f in self.preventative_vars)
        total_revenue = self.problem.objective.value() + (optimized_internal_cost + optimized_external_cost + optimized_preventative_cost)

        return {
            "optimized_internal_cost": optimized_internal_cost,
            "optimized_external_cost": optimized_external_cost,
            "optimized_preventative_cost": optimized_preventative_cost,
            "total_cost": optimized_internal_cost + optimized_external_cost + optimized_preventative_cost,
            "total_revenue": total_revenue,
        }
