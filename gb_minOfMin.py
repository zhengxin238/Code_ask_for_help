import gurobipy as gp
from gurobipy import *
import graphCode_Coefficient_MinOfMin
import prefLibParse
from function_code import borda_score_df_func
import numpy as np

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size = 3

m = Model("mlp")
num_vars = len(candidates)

# =========================================================
coeff = graphCode_Coefficient_MinOfMin.final_coeff_matrix

x = m.addVars(num_vars, vtype=GRB.BINARY, name="x")

objective_functions = []

for i in range(coeff.shape[0]):
    coeff_vector = coeff[i, :]
    obj = gp.LinExpr()
    for j in range(num_vars):
        obj += coeff_vector[j] * x[j]
    objective_functions.append(obj)

# Introduce a new variable representing the minimum of the minimum values
min_of_min = m.addVar(vtype=GRB.CONTINUOUS, name="max_of_min")


# Add constraints to ensure that min_of_max is less than or equal to each objective
for i, obj_func in enumerate(objective_functions):
    m.addConstr(min_of_min <= obj_func, f"min_constraint_{i}")

m.addConstr(quicksum(x[i] for i in range(num_vars)) == committee_size, "c2")

m.setObjective(min_of_min, sense=GRB.MAXIMIZE)


m.optimize()

# Print the results
if m.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for v in m.getVars():
        print(f"{v.varName}: {v.x}")



