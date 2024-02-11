import gurobipy as gp
from gurobipy import *
import graphCode_Coefficient_AvgAvg
import graphCode_Coefficient_AvgAvg
import prefLibParse
from function_code import borda_score_df_func

"""
candidates = list(range(1, (
        prefLibParse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
voters = list(
    range(1, (prefLibParse.getNumberOfVoters(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
preference_in_table = prefLibParse.getPreferenceList(r"https://www.preflib.org/static/data/agh/00009-00000001.soc")
friend_structure_list = graphCode.getFriendStructureList(0.05, prefLibParse.getNumberOfVoters(
    r"https://www.preflib.org/static/data/agh/00009-00000001.soc"))"""

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
committee_size = 4
#
# m = Model("mlp")
num_vars =len(candidates)
#
coeff = [15.33333333333333, 16.333333333333332, 13.666666666666664, 14, 15.666666666666664, 15]
#
# """variables = m.addVars(num_vars, vtype=gp.GRB.BINARY)"""
#
# x = {}
# for i in range(num_vars):
#     x[i] = m.addVar(name=f'x_{i}', vtype=GRB.BINARY)
#
#
# objective_expression = quicksum(coeff[i] * x[i] for i in range(num_vars))
# obj = m.setObjective(objective_expression, GRB.MAXIMIZE)
#
# m.addConstr(quicksum(x[i] for i in range(num_vars)) == 4, "c2")

# m.optimize()
# if m.status == gp.GRB.OPTIMAL:
#     for var in m.getVars():
#         print(f"{var.varName} = {var.X}")
#
# print(len(candidates))
# for i in range(num_vars):
#     print(i)

def avgOfAvg_model(num_vars_aa,coeff_aa,committee_size_aa):
    m = Model("mlp")
    x_dic = {}
    for i in range(num_vars_aa):
        x_dic[i] = m.addVar(name=f'x_{i}', vtype=GRB.BINARY)
    objective_expression = quicksum(coeff_aa[i] * x_dic[i] for i in range(num_vars_aa))
    obj = m.setObjective(objective_expression, GRB.MAXIMIZE)
    m.addConstr(quicksum(x_dic[i] for i in range(num_vars_aa)) == committee_size_aa, "c2")
    return m

# m = avgOfAvg_model(num_vars,coeff,4)

def run_optimization(model):
    optimal_solution = {}
    model.optimize()

    # Print the results
    if model.status == GRB.OPTIMAL:
        for v in model.getVars():
            optimal_solution[v.varName] = v.x
    return optimal_solution


# m.optimize()
# if m.status == gp.GRB.OPTIMAL:
#     for var in m.getVars():
#         print(f"{var.varName} = {var.X}")
#
# print(len(candidates))
# for i in range(num_vars):
#     print(i)