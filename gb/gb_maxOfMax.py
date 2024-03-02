import gurobipy as gp
from gurobipy import *

from coefficients import graphCode_Coefficient_MaxOfMax



def maxOfMax_model_run_optimization(num_vars_a, coeff_a, committee_size_a):
    optimal_solution_dict = {}
    m = Model("mlp")
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
    max_optimal_solution_dict = {f'x[{i}]': value for i, value in enumerate(max_optimal_solution)}
    optimal_solution_dict["final_committee"] = max_optimal_solution_dict
    optimal_solution_dict["optimized_value"] = max(optimal_values)
    return optimal_solution_dict







