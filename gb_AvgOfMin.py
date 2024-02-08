import gurobipy as gp
from gurobipy import *
from pymongo import MongoClient

import graphCode_Coefficient_AvgOfMin

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size =3

# Define decision variables
num_vars = len(candidates)

coeff = graphCode_Coefficient_AvgOfMin.final_coeff_matrix
num_of_friends_list = graphCode_Coefficient_AvgOfMin.num_of_friends
list_of_neighbors = graphCode_Coefficient_AvgOfMin.list_of_neighbors
m_value = graphCode_Coefficient_AvgOfMin.m_value_big

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
        constrains_objective_functions.append(obj)
        m.addConstr(s_group[voterindex] <= obj, "avgofmin_constraint_{i}")

# Define the objective function as the sum of all variables
objective_expr = s_group.sum() / num_variables_s

m.setObjective(objective_expr, sense=GRB.MAXIMIZE)
m.optimize()

optimal_solution = {}
#Print the results
if m.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for v in m.getVars():
        optimal_solution[v.varName] = v.x
        print(f"{v.varName}: {v.x}")




client = MongoClient('localhost', 27017)
db = client['votingdb']
collection = db['AvgOfMin']


collection.insert_one(optimal_solution)