import gurobipy as gp
from gurobipy import *


# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# committee_size =3
#
# # Define decision variables
# num_vars = len(candidates)
#
# coeff = graphCode_Coefficient_MinOfMax.final_coeff_matrix
# list_of_neighbors = graphCode_Coefficient_MinOfMax.list_of_neighbors
# m_value = graphCode_Coefficient_MinOfMax.m_value_big
#
# m = Model("mlp")
# num_variables_group1 = num_vars
# x_group1 = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")
#
# # Introduce 2D variables
# a_group_2dimensional = {}
# for i in range(len(list_of_neighbors)):
#     for j in range(len(list_of_neighbors[i])):
#         a_group_2dimensional[i, j] = m.addVar(vtype=GRB.BINARY, name=f"a_{i}_{j}")
#
# for i in range(len(list_of_neighbors)):
#     m.addConstr(sum(a_group_2dimensional[i, j] for j in range(len(list_of_neighbors[i]))) == 1, f"constraint_sum_{i}")
#
# m.addConstr(quicksum(x_group1[i] for i in range(num_vars)) == committee_size, "c2")
#
# # Introduce a new variable s
# s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
#
# # print(a_group_2dimensional)
# constrains_objective_functions = []
#
# # Group variables by their first index
# grouped_variables = {}
#
# for key, var in a_group_2dimensional.items():
#     first_index = key[0]
#     if first_index not in grouped_variables:
#         grouped_variables[first_index] = []
#     grouped_variables[first_index].append(var)
#
# print(grouped_variables)
# # Add constraints for each group of variables
# for first_index, variables_in_group in grouped_variables.items():
#     m.addConstr(sum(variables_in_group) <= 1, f"group_constraint_{first_index}")
#
# for voterindex, voter in enumerate(list_of_neighbors):
#     for i in range (0,len(voter)):
#         coeff_vector = coeff[(voter[i] - 1), :]
#         obj = gp.LinExpr()
#         for j in range(num_vars):
#             obj += coeff_vector[j] * x_group1[j]
#         obj += (1 - a_group_2dimensional[voterindex,i]) * m_value
#         constrains_objective_functions.append(obj)
#
# for i, obj_func in enumerate(constrains_objective_functions):
#     m.addConstr(s <= obj_func, f"max_constraint_{i}")
#
#
# m.setObjective(s, sense=GRB.MAXIMIZE)
# m.optimize()
#
# if m.status == GRB.OPTIMAL:
#     x_value_dict = m.getAttr('X', x_group1)
#     max_optimal_solution_formatted = {f'x[{k}]': v for k, v in x_value_dict.items()}
#     optimal_solution_dict = {}
#     optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
#     optimal_solution_dict["optimized_value"] = m.objVal
#     print(optimal_solution_dict)

def minOfMax_model_run_optimization(num_vars_a, coeff_a, committee_size_a, list_of_neighbors_a, m_value_a):

    optimal_solution_dict = {}

    m = Model("mlp")
    num_variables_group1 = num_vars_a
    x_group1 = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")

    a_group_2dimensional = {}
    for i in range(len(list_of_neighbors_a)):
        for j in range(len(list_of_neighbors_a[i])):
            if len(list_of_neighbors_a[i]) != 0:
                a_group_2dimensional[i, j] = m.addVar(vtype=GRB.BINARY, name=f"a_{i}_{j}")

    for i in range(len(list_of_neighbors_a)):
        if len(list_of_neighbors_a[i]) != 0:
            m.addConstr(sum(a_group_2dimensional[i, j] for j in range(len(list_of_neighbors_a[i]))) == 1,f"constraint_sum_{i}")

    m.addConstr(quicksum(x_group1[i] for i in range(num_vars_a)) == committee_size_a, "c2")

    # Introduce a new variable s
    s = m.addVar(vtype=GRB.CONTINUOUS, name="s")



    # Group variables by their first index
    grouped_variables = {}

    for key, var in a_group_2dimensional.items():
        first_index = key[0]
        if first_index not in grouped_variables:
            grouped_variables[first_index] = []
        grouped_variables[first_index].append(var)

    # Add constraints for each group of variables
    for first_index, variables_in_group in grouped_variables.items():
            m.addConstr(sum(variables_in_group) == 1, f"group_constraint_{first_index}")


    # print(a_group_2dimensional)
    constrains_objective_functions = []
    for voterindex, voter in enumerate(list_of_neighbors_a):
        if len(voter) != 0:
            for i in range(0, len(voter)):
                coeff_vector = coeff_a[(voter[i] - 1), :]
                obj = gp.LinExpr()
                for j in range(num_vars_a):
                    obj += coeff_vector[j] * x_group1[j]
                obj += (1 - a_group_2dimensional[voterindex, i]) * m_value_a
                constrains_objective_functions.append(obj)
        else: constrains_objective_functions.append(num_vars_a*len(list_of_neighbors_a))

    for i, obj_func in enumerate(constrains_objective_functions):
        m.addConstr(s <= obj_func, f"max_constraint_{i}")

    m.setObjective(s, sense=GRB.MAXIMIZE)
    m.optimize()
    if m.status == GRB.OPTIMAL:
        print("zhengzheng")
        x_value_dict = m.getAttr('X', x_group1)
        max_optimal_solution_formatted = {f'x[{k}]': v for k, v in x_value_dict.items()}
        optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
        optimal_solution_dict["optimized_value"] = m.objVal
        print(optimal_solution_dict)
        return optimal_solution_dict


# minOfMax_model_run_optimization(num_vars, coeff, committee_size, list_of_neighbors, m_value)


