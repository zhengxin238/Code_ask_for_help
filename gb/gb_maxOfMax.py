import gurobipy as gp
from gurobipy import *

from coefficients import graphCode_Coefficient_MaxOfMax


def maxOfMax_model_run_optimization(num_vars_a, coeff_a, committee_size_a, list_of_neighbors_a):
    m_value_a = 2 *num_vars_a
    optimal_solution_dict = {}
    m = Model("mlp")
    # Set the time limit (e.g., 300 seconds)
    m.Params.TimeLimit = 60
    num_variables_group1 = num_vars_a
    x_group1 = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")

    # Introduce 2D variables
    a_group_2dimensional = {}
    for i in range(len(list_of_neighbors_a)):
        for j in range(len(list_of_neighbors_a[i])):
            if len(list_of_neighbors_a[i]) != 0:
                a_group_2dimensional[i, j] = m.addVar(vtype=GRB.BINARY, name=f"a_{i}_{j}")

    for i in range(len(list_of_neighbors_a)):
        if len(list_of_neighbors_a[i]) != 0:
            m.addConstr(sum(a_group_2dimensional[i, j] for j in range(len(list_of_neighbors_a[i]))) == 1,
                        f"constraint_sum_{i}")

    m.addConstr(quicksum(x_group1[i] for i in range(num_vars_a)) == committee_size_a, "c2")

    # Introduce a new group variables s
    s = m.addVar(vtype=GRB.CONTINUOUS, name="s")

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
                m.addConstr(s <= obj, f"maxofmax_constraint_{i}")
        else:
            s = 0
    # Define the objective function as the sum of all variables
    objective_expr = s

    m.setObjective(objective_expr, sense=GRB.MAXIMIZE)
    m.optimize()
    # Print the results
    if m.status == GRB.OPTIMAL:
        x_value_dict = m.getAttr('X', x_group1)
        max_optimal_solution_formatted = {f'x[{k}]': v for k, v in x_value_dict.items()}
        optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
        optimal_solution_dict["optimized_value"] = m.objVal
        print(optimal_solution_dict)
        return optimal_solution_dict
    else:
        best_solution = m.getVars()
        x_value_dict = m.getAttr('X', x_group1)
        max_optimal_solution_formatted = {f'x[{k}]': v for k, v in x_value_dict.items()}
        optimal_solution_dict["final_committee"] = max_optimal_solution_formatted
        optimal_solution_dict["optimized_value"] = m.objVal
        print(optimal_solution_dict)
        return optimal_solution_dict








