import gurobipy as gp
from gurobipy import *


# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# committee_size =3
#
# # Define decision variables
# num_vars = len(candidates)
#
# coeff = graphCode_Coefficient_MaxOfMin.final_coeff_matrix
# # num_of_friends_list = graphCode_Coefficient_MinOfMax.num_of_friends
# list_of_neighbors = graphCode_Coefficient_MaxOfMin.list_of_neighbors
# m_value = graphCode_Coefficient_MaxOfMin.m_value_big

## # # # # # #  x = m.addVars(num_vars, vtype=GRB.BINARY, name="x")

# Decision variables for group 1, this is fixed


# Decision variables for group 2, this dependents on how many friends a voter has


# [2, 5, 6]
# for neighborofvoterv in list_of_neighbors:
#     m = Model("mlp")
#
#     num_variables_group1 = num_vars
#     x_variables = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")
#     num_variables_group2 = len(neighborofvoterv)
#     a_group = m.addVars(num_variables_group2, vtype=GRB.BINARY, name="a")
#     constrains_objective_functions = []
#     for i in range (0,len(neighborofvoterv)):
#         coeff_vector = coeff[(neighborofvoterv[i] - 1), :]
#         obj = gp.LinExpr()
#         for j in range(num_vars):
#             obj += coeff_vector[j] * x_variables[j]
#         constrains_objective_functions.append(obj)
#     # Introduce a new variable s
#     s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
#     # Add constraints to ensure that min_of_max is less than or equal to each objective
#     for i, obj_func in enumerate(constrains_objective_functions):
#         m.addConstr(s <= obj_func, f"max_constraint_{i}")
#
#     m.addConstr(quicksum(x_variables[i] for i in range(num_vars)) == committee_size, "c2")
#     m.addConstr(quicksum(a_group[i] for i in range(len(neighborofvoterv))) == 1, "c3")
#
#     m.setObjective(s, sense=GRB.MAXIMIZE)
#     m.optimize()
#     #Print the results
#     if m.status == GRB.OPTIMAL:
#         print("Optimal solution found:")
#         for v in m.getVars():
#            print(f"{v.varName}: {v.x}")


def maxOfMin_model_run_optimization(num_vars_a, coeff_a, committee_size_a, list_of_neighbors_a):
    optimal_solutions = []
    optimal_values = []
    optimal_solution_dict = {}

    for neighborofvoterv in list_of_neighbors_a:
        if len(neighborofvoterv) != 0:
            m = Model("mlp")
            # Set the time limit (e.g., 300 seconds)
            m.Params.TimeLimit = 300
            m.reset()
            num_variables_group1 = num_vars_a
            x_variables = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")
            num_variables_group2 = len(neighborofvoterv)
            a_group = m.addVars(num_variables_group2, vtype=GRB.BINARY, name="a")
            constrains_objective_functions = []
            for i in range(0, len(neighborofvoterv)):
                coeff_vector = coeff_a[(neighborofvoterv[i] - 1), :]
                obj = gp.LinExpr()
                for j in range(num_vars_a):
                    obj += coeff_vector[j] * x_variables[j]
                constrains_objective_functions.append(obj)
        # Introduce a new variable s
            s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
        # Add constraints to ensure that min_of_max is less than or equal to each objective
            for i, obj_func in enumerate(constrains_objective_functions):
                m.addConstr(s <= obj_func, f"max_constraint_{i}")

            m.addConstr(quicksum(x_variables[i] for i in range(num_vars_a)) == committee_size_a, "c2")
            m.addConstr(quicksum(a_group[i] for i in range(len(neighborofvoterv))) == 1, "c3")

            m.setObjective(s, sense=GRB.MAXIMIZE)
            m.optimize()

            x_value_dict = m.getAttr('X', x_variables)
            optimal_solutions.append(x_value_dict)
            optimal_values.append(m.objVal)
        if len(neighborofvoterv) == 0:
            m = Model("mlp")
            m.reset()
            x_variables = m.addVars(num_vars_a, vtype=GRB.BINARY, name="x")
            m.addConstr(quicksum(x_variables[i] for i in range(num_vars_a)) == committee_size_a, "c2")
            m.addConstr(quicksum(x_variables[i] for i in range(committee_size_a)) == committee_size_a, "c3")
            m.optimize()
            x_value_dict = m.getAttr('X', x_variables)
            optimal_solutions.append(x_value_dict)
            optimal_values.append(0)
        # Find the index of the maximum optimal value
    if optimal_values != []:
        max_optimal_index = optimal_values.index(max(optimal_values))
        # Retrieve the solution corresponding to the maximum optimal value
        max_optimal_solution = optimal_solutions[max_optimal_index]
        max_optimal_solution_formatted = {f'x[{k}]': v for k, v in max_optimal_solution.items()}
        # max_optimal_objective = corresponding_objectives[max_optimal_index]
        optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
        optimal_solution_dict["optimized_value"] = max(optimal_values)
        print(optimal_solution_dict)
        return optimal_solution_dict





# def dict_to_preflib_format(approval_data, directory, filename):
#     full_path = os.path.join(directory, filename)
#     with open(full_path, 'w') as f:
#         for candidate, approval in approval_data.items():
#             if approval == 1:
#                 f.write(candidate + '\n')

# print(maxOfMin_model_run_optimization(num_vars, coeff, committee_size, list_of_neighbors))
