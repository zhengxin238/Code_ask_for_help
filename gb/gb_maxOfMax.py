import gurobipy as gp
from gurobipy import *

from coefficients import graphCode_Coefficient_MaxOfMax


def maxOfMax_model_run_optimization(num_vars_a, coeff_a, committee_size_a, list_of_neighbors_a,m_value_a):
    optimal_solutions = []
    optimal_values = []
    optimal_solution_dict = {}


    for neighborofvoterv in list_of_neighbors_a:
        if len(neighborofvoterv) != 0:
            m = Model("mlp")
            # Set the time limit (e.g., 300 seconds)
            m.Params.TimeLimit = 100
            m.reset()
            num_variables_group1 = num_vars_a
            x_variables = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")
            a_group = m.addVars(len(neighborofvoterv), vtype=GRB.BINARY, name="a")
            constrains_objective_functions = []
            for i in range(0, len(neighborofvoterv)):
                coeff_vector = coeff_a[(neighborofvoterv[i] - 1), :]
                obj = gp.LinExpr()
                for j in range(num_vars_a):
                    obj += coeff_vector[j] * x_variables[j]
                obj += (1 - a_group[i]) * m_value_a
                constrains_objective_functions.append(obj)
        # Introduce a new variable s
            s = m.addVar(vtype=GRB.CONTINUOUS, name=f"s{i}")
        # Add constraints to ensure that max_of_min is less than or equal to each objective
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



















    #
    #
    # m = Model("mlp")
    # # Set the time limit (e.g., 300 seconds)
    # m.Params.TimeLimit = 100
    # num_variables_group1 = num_vars_a
    # x_group1 = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")
    #
    # # Introduce 2D variables
    # a_group_2dimensional = {}
    # for i in range(len(list_of_neighbors_a)):
    #     for j in range(len(list_of_neighbors_a[i])):
    #         if len(list_of_neighbors_a[i]) != 0:
    #             a_group_2dimensional[i, j] = m.addVar(vtype=GRB.BINARY, name=f"a_{i}_{j}")
    #
    # for i in range(len(list_of_neighbors_a)):
    #     if len(list_of_neighbors_a[i]) != 0:
    #         m.addConstr(sum(a_group_2dimensional[i, j] for j in range(len(list_of_neighbors_a[i]))) == 1,
    #                     f"constraint_sum_{i}")
    #
    # m.addConstr(quicksum(x_group1[i] for i in range(num_vars_a)) == committee_size_a, "c2")
    #
    # # Introduce a new group variables s
    # num_variables_s = len(list_of_neighbors_a)
    # s_group = m.addVars(num_variables_s, vtype=GRB.CONTINUOUS, name="s")
    #
    # # print(a_group_2dimensional)
    # constrains_objective_functions = []
    #
    # for voterindex, voter in enumerate(list_of_neighbors_a):
    #     if len(voter) != 0:
    #         for i in range(0, len(voter)):
    #             coeff_vector = coeff_a[(voter[i] - 1), :]
    #             obj = gp.LinExpr()
    #             for j in range(num_vars_a):
    #                 obj += coeff_vector[j] * x_group1[j]
    #             obj += (1 - a_group_2dimensional[voterindex, i]) * m_value_a
    #             constrains_objective_functions.append(obj)
    #             m.addConstr(s_group[voterindex] <= obj, f"avgofmax_constraint_{i}")
    #     else:
    #         s_group[voterindex] = 0
    # # Define the objective function as the sum of all variables
    # objective_expr = s_group.sum() / num_variables_s
    #
    # m.setObjective(objective_expr, sense=GRB.MAXIMIZE)
    # m.optimize()
    # # Print the results
    # if m.status == GRB.OPTIMAL:
    #     x_value_dict = m.getAttr('X', x_group1)
    #     max_optimal_solution_formatted = {f'x[{k}]': v for k, v in x_value_dict.items()}
    #     optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
    #     optimal_solution_dict["optimized_value"] = m.objVal
    #     print(optimal_solution_dict)
    #     return optimal_solution_dict
    # else:
    #     best_solution = m.getVars()
    #     x_value_dict = m.getAttr('X', x_group1)
    #     max_optimal_solution_formatted = {f'x[{k}]': v for k, v in x_value_dict.items()}
    #     optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
    #     optimal_solution_dict["optimized_value"] = m.objVal
    #     print(optimal_solution_dict)
    #     return optimal_solution_dict








