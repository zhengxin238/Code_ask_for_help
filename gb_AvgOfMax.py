import gurobipy as gp
from gurobipy import *

import graphCode_Coefficient_AvgOfMax

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size =3

# Define decision variables
num_vars = len(candidates)

coeff = graphCode_Coefficient_AvgOfMax.final_coeff_matrix
num_of_friends_list = graphCode_Coefficient_AvgOfMax.num_of_friends
list_of_neighbors = graphCode_Coefficient_AvgOfMax.list_of_neighbors
m_value = graphCode_Coefficient_AvgOfMax.m_value_big

m = Model("mlp")
num_variables_group1 = num_vars
x_group1 = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")




# Introduce 2D variables
a_group_2dimensional = {}
for i in range(len(list_of_neighbors)):
    for j in range(len(list_of_neighbors[i])):
        a_group_2dimensional[i, j] = m.addVar(vtype=GRB.BINARY, name="a_{i}_{j}")

for i in range(len(list_of_neighbors)):
    m.addConstr(sum(a_group_2dimensional[i, j] for j in range(len(list_of_neighbors[i]))) == 1, f"constraint_sum_{i}")

m.addConstr(quicksum(x_group1[i] for i in range(num_vars)) == committee_size, "c2")

# Introduce a new group variables s
num_variables_s = len(list_of_neighbors)
s_group = m.addVars(num_variables_s, vtype=GRB.CONTINUOUS, name="s")

# print(a_group_2dimensional)
constrains_objective_functions = []

for voterindex, voter in enumerate(list_of_neighbors):
    for i in range (0,len(voter)):
        coeff_vector = coeff[(voter[i] - 1), :]
        obj = gp.LinExpr()
        for j in range(num_vars):
            obj += coeff_vector[j] * x_group1[j]
        obj += (1 - a_group_2dimensional[voterindex,i]) * m_value
        constrains_objective_functions.append(obj)
        m.addConstr(s_group[voterindex] <= obj, "avgofmax_constraint_{i}")

# Define the objective function as the sum of all variables
objective_expr = s_group.sum() / num_variables_s

m.setObjective(objective_expr, sense=GRB.MAXIMIZE)
m.optimize()
#Print the results
if m.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for v in m.getVars():
        print(f"{v.varName}: {v.x}")


"""
for voter in list_of_neighbors:       
    for i in range (0,len(voter)):
        coeff_vector = coeff[(voter[i] - 1), :]
        obj = gp.LinExpr()
        for j in range(num_vars):
            obj += coeff_vector[j] * x_group1[j]s
        obj += (1 - a_group[i]) * m_value
        objective_functions.append(obj)
    # Introduce a new variable s
    s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
    # Add constraints to ensure that min_of_max is less than or equal to each objective
    for i, obj_func in enumerate(objective_functions):
        m.addConstr(s <= obj_func, f"max_constraint_{i}")
    """ """
    m.addConstr(quicksum(x_group1[i] for i in range(num_vars)) == committee_size, "c2")
    m.addConstr(quicksum(a_group[i] for i in range(len(neighborofvoterv))) == 1, "c3")

    m.setObjective(s, sense=GRB.MAXIMIZE)
    m.optimize()
    #Print the results
    if m.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for v in m.getVars():
           print(f"{v.varName}: {v.x}")
"""
"""
´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
# Introduce a new variable s
s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
# Add constraints to ensure that min_of_max is less than or equal to each objective
for i, obj_func in enumerate(objective_functions):
    m.addConstr(s <= obj_func, f"max_constraint_{i}")

m.addConstr(quicksum(x_group1[i] for i in range(num_vars)) == committee_size, "c2")
m.addConstr(quicksum(x_group2[i] for i in range(num_vars)) == 1, "c3")

m.setObjective(s, sense=GRB.MAXIMIZE)
m.optimize()
´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
""""""
# Group variables by their first index
grouped_variables = {}

for key, var in a_group_2dimensional.items():
    first_index = key[0]
    if first_index not in grouped_variables:
        grouped_variables[first_index] = []
    grouped_variables[first_index].append(var)

print(grouped_variables)
# Add constraints for each group of variables
for first_index, variables_in_group in grouped_variables.items():
    m.addConstr(sum(variables_in_group) <= 1, f"group_constraint_{first_index}")


# Print the results
# 1if m.status == GRB.OPTIMAL:
# 2   print("Optimal solution found:")
#  3  for v in m.getVars():
#   4     print(f"{v.varName}: {v.x}")
#     # Retrieve additional optimal solutions if they exist
#     solution_count = m.getAttr('SolCount')
# for solution_index in range(2, solution_count + 1):
#     m.setParam(GRB.Param.SolutionNumber, solution_index)
#     m.optimize()
#     print(f"\nOptimal solution {solution_index}:")
#     for v in m.getVars():
#         print(f"{v.varName}: {v.x}")
#     print(f"Maximum of minimum values: {max_of_min.x}")"""
