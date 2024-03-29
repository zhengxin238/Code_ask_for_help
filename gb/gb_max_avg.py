import gurobipy as gp
from gurobipy import *


# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# committee_size = 3
#
# m = Model("max_of_max_objectives")
# num_vars = len(candidates)
#
# # =========================================================
# coeff = graphCode_Coefficient_MaxAvg.final_coeff_matrix
#
# x = m.addVars(num_vars, vtype=GRB.BINARY, name="x")
#
# objective_functions = []
#
# for i in range(coeff.shape[0]):
#     coeff_vector = coeff[i, :]
#     obj = gp.LinExpr()
#     for j in range(num_vars):
#         obj += coeff_vector[j] * x[j]
#     objective_functions.append(obj)
#
#
# # List to store optimal solutions
# optimal_solutions = []
# optimal_solution_dict = {}
#
#
# # List to store optimal values
# optimal_values = []
#
# # List to store corresponding objective functions
# corresponding_objectives = []
#
# m.addConstr(gp.quicksum(x[j] for j in range(num_vars)) == committee_size, "sum_constraint")
#
# # Iteratively optimize each objective function
# for i, obj_func in enumerate(objective_functions):
#     # Clear the model to reset for each iteration
#     m.reset()
#
#     # Set the current objective function
#     m.setObjective(obj_func, sense=GRB.MAXIMIZE)
#
#     # Optimize the model
#     m.optimize()
#
#     # Store the optimal solution, optimal value, and corresponding objective function
#     optimal_solutions.append([v.x for v in m.getVars()])
#     optimal_solution_dict_temp = {}
#     for v in m.getVars():
#         optimal_solution_dict_temp[v.varName] = v.x
#     optimal_solution_dict[i] = optimal_solution_dict_temp
#     optimal_values.append(m.objVal)
#     corresponding_objectives.append(i)
#
# # Find the index of the maximum optimal value
# max_optimal_index = optimal_values.index(max(optimal_values))
#
# # Retrieve the solution corresponding to the maximum optimal value
# max_optimal_solution = optimal_solutions[max_optimal_index]
# max_optimal_objective = corresponding_objectives[max_optimal_index]


def maxOfAvg_model_run_optimization(num_vars_a, coeff_a, committee_size_a):

    m = Model("max_of_max_objectives")
    # Set the time limit (e.g., 300 seconds)
    m.Params.TimeLimit = 300
    x = m.addVars(num_vars_a, vtype=GRB.BINARY, name="x")

    objective_functions = []
    for i in range(coeff_a.shape[0]):
        coeff_vector = coeff_a[i, :]
        obj = gp.LinExpr()
        for j in range(num_vars_a):
            obj += coeff_vector[j] * x[j]
        objective_functions.append(obj)
    # List to store optimal solutions
    optimal_solutions = []
    optimal_solution_dict = {}
    optimal_solution_dict_t = {}
    # List to store optimal values
    optimal_values = []


    m.addConstr(gp.quicksum(x[j] for j in range(num_vars_a)) == committee_size_a, "sum_constraint")
    # Iteratively optimize each objective function
    for i, obj_func in enumerate(objective_functions):
        # Clear the model to reset for each iteration
        m.reset()
        m.Params.TimeLimit = 120
        # Set the current objective function
        m.setObjective(obj_func, sense=GRB.MAXIMIZE)

        # Optimize the model
        m.optimize()

        # Store the optimal solution, optimal value, and corresponding objective function
        optimal_solutions.append([v.x for v in m.getVars()])
        optimal_solution_dict_temp = {}
        for v in m.getVars():
            optimal_solution_dict_temp[v.varName] = v.x
        optimal_solution_dict_t[i] = optimal_solution_dict_temp
        optimal_values.append(m.objVal)

    # Find the index of the maximum optimal value
    max_optimal_index = optimal_values.index(max(optimal_values))
    # Retrieve the solution corresponding to the maximum optimal value

    optimal_solution_dict["final_committee"] = optimal_solution_dict_t[max_optimal_index]
    optimal_solution_dict["optimized_value"] = max(optimal_values)
    print(optimal_solution_dict)
    return  optimal_solution_dict


# m = avgOfAvg_model(num_vars,coeff,4)

# def run_optimization(model):
#     optimal_solution = {}
#     model.optimize()
#
#     # Print the results
#     if model.status == GRB.OPTIMAL:
#         for v in model.getVars():
#             optimal_solution[v.varName] = v.x
#             print(f"{v.varName} = {v.x}")
#     return optimal_solution




# Print the results
# print(f"Maximum optimal value: {max(optimal_values)}")
# print(f"Corresponding objective function index: {max_optimal_objective}")
# print(f"Corresponding objective function: {objective_functions[max_optimal_objective]}")
# print(f"Variable values for maximum optimal value: {max_optimal_solution}")
# print(f"Variable values for maximum optimal value: { optimal_solution_dict[max_optimal_objective]}")
# for candidate, value in zip(x, max_optimal_solution):
#     print(f"{candidate}: {value}")
# if m.status == gp.GRB.OPTIMAL:
#     for var in m.getVars():
#         print(f"{var.varName} = {var.X}")