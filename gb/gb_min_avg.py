import gurobipy as gp
from gurobipy import *


# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# committee_size = 3
#
# m = Model("mlp")
# num_vars = len(candidates)
#
# # =========================================================
# coeff = graphCode_Coefficient_MinAvg.final_coeff_matrix
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
# # Introduce a new variable representing the maximum of the minimum values
# max_of_min = m.addVar(vtype=GRB.CONTINUOUS, name="max_of_min")
#
#
# # Add constraints to ensure that min_of_max is less than or equal to each objective
# for i, obj_func in enumerate(objective_functions):
#     m.addConstr(max_of_min <= obj_func, f"max_constraint_{i}")
#
# m.addConstr(quicksum(x[i] for i in range(num_vars)) == committee_size, "c2")
#
# m.setObjective(max_of_min, sense=GRB.MAXIMIZE)
#
#
# m.optimize()
#
# # Print the results
# if m.status == GRB.OPTIMAL:
#     print("Optimal solution found:")
#     for v in m.getVars():
#         print(f"{v.varName}: {v.x}")
#
# print(11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)



def minOfAvg_model_run_optimization(num_vars_a, coeff_a, committee_size_a):
    m = Model("mlp")
    # Set the time limit (e.g., 300 seconds)
    m.Params.TimeLimit = 100
    x = m.addVars(num_vars_a, vtype=GRB.BINARY, name="x")

    objective_functions = []

    for i in range(coeff_a.shape[0]):
        coeff_vector = coeff_a[i, :]
        if sum(coeff_vector) != 0:
            obj = gp.LinExpr()
            for j in range(num_vars_a):
                obj += coeff_vector[j] * x[j]
            objective_functions.append(obj)

    # Introduce a new variable representing the maximum of the minimum values
    min_of_avg = m.addVar(vtype=GRB.CONTINUOUS, name="min_of_avg")

    # Add constraints to ensure that min_of_max is less than or equal to each objective
    for i, obj_func in enumerate(objective_functions):
        m.addConstr(min_of_avg <= obj_func, f"max_constraint_{i}")

    m.addConstr(quicksum(x[i] for i in range(num_vars_a)) == committee_size_a, "c2")

    m.setObjective(min_of_avg, sense=GRB.MAXIMIZE)
    m.optimize()

    optimal_solution_dict = {}
    if m.status == GRB.OPTIMAL:
        optimal_solution_dict_temp = {}
        for v in m.getVars():
            if v.varName != "min_of_avg":
                optimal_solution_dict_temp[v.varName] = v.x
        optimal_solution_dict["final_committee"] = optimal_solution_dict_temp
        optimal_solution_dict["optimized_value"] = m.objVal
    else:
        optimal_solution_dict_temp = {}
        for v in m.getVars():
            if v.varName != "min_of_avg":
                optimal_solution_dict_temp[v.varName] = v.x
        optimal_solution_dict["final_committee"] = optimal_solution_dict_temp
        optimal_solution_dict["optimized_value"] = m.objVal

    print(optimal_solution_dict)
    return optimal_solution_dict

# minOfAvg_model_run_optimization(num_vars, coeff, committee_size)

    #     # Retrieve additional optimal solutions if they exist
    #     solution_count = m.getAttr('SolCount')
    # for solution_index in range(2, solution_count + 1):
    #     m.setParam(GRB.Param.SolutionNumber, solution_index)
    #     m.optimize()
    #     print(f"\nOptimal solution {solution_index}:")
    #     for v in m.getVars():
    #         print(f"{v.varName}: {v.x}")
    #     print(f"Maximum of minimum values: {max_of_min.x}")


