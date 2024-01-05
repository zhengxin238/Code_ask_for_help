import gurobipy as gp
from gurobipy import *
import graphCode_Coefficient_MaxOfMax
import prefLibParse
from function_code import borda_score_df_func
import numpy as np

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size = 3

m = Model("mlp")
num_vars = len(candidates)

# =========================================================
coeff = graphCode_Coefficient_MaxOfMax.final_coeff_matrix


x = m.addVars(num_vars, vtype=GRB.BINARY, name="x")

objective_functions = []

for i in range(coeff.shape[0]):
    coeff_vector = coeff[i, :]
    obj = gp.LinExpr()
    for j in range(num_vars):
        obj += coeff_vector[j] * x[j]
    objective_functions.append(obj)


# List to store optimal solutions
optimal_solutions = []

# List to store optimal values
optimal_values = []

# List to store corresponding objective functions
corresponding_objectives = []

m.addConstr(gp.quicksum(x[j] for j in range(num_vars)) == committee_size, "sum_constraint")

# Iteratively optimize each objective function
for i, obj_func in enumerate(objective_functions):
    # Clear the model to reset for each iteration
    m.reset()

    # Set the current objective function
    m.setObjective(obj_func, sense=GRB.MAXIMIZE)

    # Optimize the model
    m.optimize()

    # Store the optimal solution, optimal value, and corresponding objective function
    optimal_solutions.append([v.x for v in m.getVars()])
    optimal_values.append(m.objVal)
    corresponding_objectives.append(i)

# Find the index of the maximum optimal value
max_optimal_index = optimal_values.index(max(optimal_values))

# Retrieve the solution corresponding to the maximum optimal value
max_optimal_solution = optimal_solutions[max_optimal_index]
max_optimal_objective = corresponding_objectives[max_optimal_index]

# Print the results
print(f"Maximum optimal value: {max(optimal_values)}")
print(f"Corresponding objective function index: {max_optimal_objective}")
print(f"Corresponding objective function: {objective_functions[max_optimal_objective]}")
print(f"Variable values for maximum optimal value: {max_optimal_solution}")
