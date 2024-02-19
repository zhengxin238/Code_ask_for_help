import gurobipy as gp
from gurobipy import *


#
# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# committee_size = 3
#
# # Define decision variables
# num_vars = len(candidates)
#
# coeff = graphCode_Coefficient_AvgOfMin.final_coeff_matrix
# list_of_neighbors = graphCode_Coefficient_AvgOfMin.list_of_neighbors
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
# # Introduce a new group variables s
# num_variables_s = len(list_of_neighbors)
# s_group = m.addVars(num_variables_s, vtype=GRB.CONTINUOUS, name="s")
#
# # print(a_group_2dimensional)
# constrains_objective_functions = []
#
# for voterindex, voter in enumerate(list_of_neighbors):
#     for i in range(0, len(voter)):
#         coeff_vector = coeff[(voter[i] - 1), :]
#         obj = gp.LinExpr()
#         for j in range(num_vars):
#             obj += coeff_vector[j] * x_group1[j]
#         constrains_objective_functions.append(obj)
#         m.addConstr(s_group[voterindex] <= obj, "avgofmin_constraint_{i}")
#
# # Define the objective function as the sum of all variables
# objective_expr = s_group.sum() / num_variables_s
#
# m.setObjective(objective_expr, sense=GRB.MAXIMIZE)
# m.optimize()
#
# optimal_solution = {}
# # Print the results
# if m.status == GRB.OPTIMAL:
#     print("Optimal solution found:")
#     for v in m.getVars():
#         optimal_solution[v.varName] = v.x
#         print(f"{v.varName}: {v.x}")


def avgOfMin_model_run_optimization(num_vars_a, coeff_a, committee_size_a, list_of_neighbors_a):
    optimal_solution_dict = {}

    m = Model("mlp")
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

    # Introduce a new group variables s # number of s = s number of voters
    num_variables_s = len(list_of_neighbors_a)
    s_group = m.addVars(num_variables_s, vtype=GRB.CONTINUOUS, name="s")

    # print(a_group_2dimensional)
    constrains_objective_functions = []

    for voterindex, voter in enumerate(list_of_neighbors_a):
        if len(voter) != 0:
            for i in range(0, len(voter)):
                coeff_vector = coeff_a[(voter[i] - 1), :]
                obj = gp.LinExpr()
                for j in range(num_vars_a):
                    obj += coeff_vector[j] * x_group1[j]
                constrains_objective_functions.append(obj)
                m.addConstr(s_group[voterindex] <= obj, "avgofmin_constraint_{i}")
        else:
            s_group[voterindex] = 0
    # Define the objective function as the sum of all variables
    objective_expr = s_group.sum() / num_variables_s

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
        pass

# avgOfMin_model_run_optimization(num_vars, coeff, committee_size, list_of_neighbors)

# client = MongoClient('localhost', 27017)
# db = client['votingdb']
# collection = db['AvgOfMin']
#
#
# collection.insert_one(optimal_solution)
