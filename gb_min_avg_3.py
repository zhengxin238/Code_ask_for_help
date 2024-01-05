import gurobipy as gp
from gurobipy import *
import graphCode_Coefficient_MinAvg
import prefLibParse
from function_code import borda_score_df_func
import numpy as np

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size = 3

m = Model("mlp")
num_vars = len(candidates)

# =========================================================
# coeff = [[1.66666667, 2.33333333, 2.33333333, 2.66666667, 3.33333333, 2.66666667]
#          [3.33333333, 2.0, 2.66666667, 2.0, 2.66666667, 2.33333333]
#          [3.5, 0.5, 4.5, 3.0, 1.0, 2.5]
#          [2.0, 3.0, 0.0, 1.0, 4.0, 5.0]
#          [2.33333333, 4.0, 1.66666667, 2.33333333, 2.66666667, 2.0]
#          [2.5, 4.5, 2.5, 3.0, 2.0, 0.5]]

# Define decision variables
num_variables = 6
x = m.addVars(num_variables, vtype=GRB.BINARY, name="x")

# Define multiple objective functions
obj_functions = [
    1.66666667*x[0] + 2.33333333*x[1] + 2.33333333*x[2] + 2.66666667*x[3] + 3.33333333*x[4] + 2.66666667*x[5],
    3.33333333*x[0] + 2*x[1] + 2.66666667*x[2] + 2*x[3] + 2.66666667*x[4] + 2.33333333*x[5],
    3.5*x[0] + 0.5*x[1] + 4.5*x[2] + 3.0*x[3] + x[4] + 2.5*x[5],
    2*x[0] + 3*x[1] + x[3] + 4*x[4] + 5*x[5],
    2.33333333*x[0] + 4*x[1] + 1.66666667*x[2] + 2.33333333*x[3] + 2.66666667*x[4] + 2*x[5],
    2.5*x[0] + 4.5*x[1] + 2.5*x[2] + 3*x[3] + 2*x[4] + 0.5*x[5]

]


# Introduce a new variable representing the minimum of the maximum values
min_of_max = m.addVar(vtype=GRB.CONTINUOUS, name="min_of_max")

# Add constraints to ensure that min_of_max is less than or equal to each objective
for i, obj_func in enumerate(obj_functions):
    m.addConstr(min_of_max <= obj_func, f"max_constraint_{i}")

# Set the overall objective to maximize min_of_max
m.setObjective(min_of_max, sense=GRB.MAXIMIZE)

m.addConstr(quicksum(x[i] for i in range(num_vars)) == 3, "c2")

m.setObjective(min_of_max, sense=GRB.MAXIMIZE)

m.optimize()

# Print the results
if m.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for v in m.getVars():
        print(f"{v.varName}: {v.x}")
    #     # Retrieve additional optimal solutions if they exist
    #     solution_count = m.getAttr('SolCount')
    # for solution_index in range(2, solution_count + 1):
    #     m.setParam(GRB.Param.SolutionNumber, solution_index)
    #     m.optimize()
    #     print(f"\nOptimal solution {solution_index}:")
    #     for v in m.getVars():
    #         print(f"{v.varName}: {v.x}")
    #     print(f"Maximum of minimum values: {max_of_min.x}")
