import gurobipy as gp
from gurobipy import *

import function_code
import graphCode_Coefficient_MaxOfMax
import prefLibParse
from function_code import borda_score_df_func
import numpy as np

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size = 3

m = Model("mlp")
num_vars = len(candidates)
#
# =========================================================
coeff = graphCode_Coefficient_MaxOfMax.getCoefficientMatrix(graphCode_Coefficient_MaxOfMax.df_bordaScore)


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

def maxOfMax_model_run_optimization(num_vars_a, coeff_a, committee_size_a):
    optimal_solution_dict = {}
    m = Model("mlp")
    x = m.addVars(num_vars_a, vtype=GRB.BINARY, name="x")
    objective_functions = []
    for i in range(coeff_a.shape[0]):
        coeff_vector = coeff_a[i, :]
        obj = gp.LinExpr()
        for j in range(num_vars_a):
            obj += coeff_vector[j] * x[j]
        objective_functions.append(obj)

    optimal_solutions = []
    optimal_values = []
    corresponding_objectives = []

    m.addConstr(gp.quicksum(x[j] for j in range(num_vars_a)) == committee_size_a, "sum_constraint")

    for i, obj_func in enumerate(objective_functions):
        m.reset()
        m.setObjective(obj_func, sense=GRB.MAXIMIZE)
        m.optimize()

        # Store the optimal solution, optimal value, and corresponding objective function
        optimal_solutions.append([v.x for v in m.getVars()])
        optimal_values.append(m.objVal)
        corresponding_objectives.append(i)

    # Find the index of the maximum optimal value
    max_optimal_index = optimal_values.index(max(optimal_values))

    # Retrieve the solution corresponding to the maximum optimal value
    max_optimal_solution = optimal_solutions[max_optimal_index]
    # max_optimal_objective = corresponding_objectives[max_optimal_index]
    optimal_solution_dict["final_committee"] = max_optimal_solution
    optimal_solution_dict["optimized_value"] = max(optimal_values)
    return optimal_solution_dict


# print(maxOfMax_model_run_optimization(num_vars, coeff, committee_size))

def save_list_to_preflib_file(approval_data, directory, filename):
    preflib_format = ""
    for i, approval in enumerate(approval_data):
        if approval == 1.0:
            preflib_format += f"x[{i}]\n"

    filepath = directory + '/' + filename
    with open(filepath, 'w') as file:
        file.write(preflib_format)


