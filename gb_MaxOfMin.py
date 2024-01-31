import gurobipy as gp
from gurobipy import *

import graphCode_Coefficient_MinOfMax

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size =3

# Define decision variables
num_vars = len(candidates)

coeff = graphCode_Coefficient_MinOfMax.final_coeff_matrix
num_of_friends_list = graphCode_Coefficient_MinOfMax.num_of_friends
list_of_neighbors = graphCode_Coefficient_MinOfMax.list_of_neighbors
m_value = graphCode_Coefficient_MinOfMax.m_value_big

## # # # # # #  x = m.addVars(num_vars, vtype=GRB.BINARY, name="x")

# Decision variables for group 1, this is fixed


# Decision variables for group 2, this dependents on how many friends a voter has


# [2, 5, 6]
for neighborofvoterv in list_of_neighbors:
    m = Model("mlp")
    num_variables_group1 = num_vars
    x_variables = m.addVars(num_variables_group1, vtype=GRB.BINARY, name="x")
    num_variables_group2 = len(neighborofvoterv)
    a_group = m.addVars(num_variables_group2, vtype=GRB.BINARY, name="x")
    constrains_objective_functions = []
    for i in range (0,len(neighborofvoterv)):
        coeff_vector = coeff[(neighborofvoterv[i] - 1), :]
        obj = gp.LinExpr()
        for j in range(num_vars):
            obj += coeff_vector[j] * x_variables[j]
        constrains_objective_functions.append(obj)
    # Introduce a new variable s
    s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
    # Add constraints to ensure that min_of_max is less than or equal to each objective
    for i, obj_func in enumerate(constrains_objective_functions):
        m.addConstr(s <= obj_func, f"max_constraint_{i}")

    m.addConstr(quicksum(x_variables[i] for i in range(num_vars)) == committee_size, "c2")
    m.addConstr(quicksum(a_group[i] for i in range(len(neighborofvoterv))) == 1, "c3")

    m.setObjective(s, sense=GRB.MAXIMIZE)
    m.optimize()
    #Print the results
    if m.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for v in m.getVars():
           print(f"{v.varName}: {v.x}")
"""
# Introduce a new variable s
s = m.addVar(vtype=GRB.CONTINUOUS, name="s")
# Add constraints to ensure that min_of_max is less than or equal to each objective
for i, obj_func in enumerate(objective_functions):
    m.addConstr(s <= obj_func, f"max_constraint_{i}")

m.addConstr(quicksum(x_group1[i] for i in range(num_vars)) == committee_size, "c2")
m.addConstr(quicksum(x_group2[i] for i in range(num_vars)) == 1, "c3")

m.setObjective(s, sense=GRB.MAXIMIZE)
m.optimize()

"""

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
