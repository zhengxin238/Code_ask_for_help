from gurobipy import *

"""
candidates = list(range(1, (
        prefLibParse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
voters = list(
    range(1, (prefLibParse.getNumberOfVoters(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
preference_in_table = prefLibParse.getPreferenceList(r"https://www.preflib.org/static/data/agh/00009-00000001.soc")
friend_structure_list = graphCode.getFriendStructureList(0.05, prefLibParse.getNumberOfVoters(
    r"https://www.preflib.org/static/data/agh/00009-00000001.soc"))"""

# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# committee_size = 4
# #
# # m = Model("mlp")
# num_vars =len(candidates)
# #
# coeff = [15.33333333333333, 16.333333333333332, 13.666666666666664, 14, 15.666666666666664, 15]
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

def avgOfAvg_model_run_optimization(num_vars_aa,coeff_aa,committee_size_aa,voters_aa):
    m = Model("mlp")
    # Set the time limit (e.g., 300 seconds)
    m.Params.TimeLimit = 100
    # x_dic = {}
    # for i in range(num_vars_aa):
    #     x_dic[i] = m.addVar(name=f'x', vtype=GRB.BINARY)
    x_group1 = m.addVars(num_vars_aa, vtype=GRB.BINARY, name="x")
    objective_expression = quicksum(coeff_aa[i] * x_group1[i] for i in range(num_vars_aa))
    obj = m.setObjective(objective_expression/len(voters_aa), GRB.MAXIMIZE)
    m.addConstr(quicksum(x_group1[i] for i in range(num_vars_aa)) == committee_size_aa, "c2")
    m.optimize()
    if m.status == GRB.OPTIMAL:
        optimal_solution_dict = {}
        optimal_solution = {}
        for v in m.getVars():
            optimal_solution[v.varName] = v.x
        optimal_solution_dict["final_committee"] = optimal_solution
        optimal_solution_dict["optimized_value"] = m.objVal
        print(optimal_solution_dict)
        return optimal_solution_dict
    else:
        optimal_solution_dict = {}
        optimal_solution = {}
        for v in m.getVars():
            optimal_solution[v.varName] = v.x
        optimal_solution_dict["final_committee"] = optimal_solution
        optimal_solution_dict["optimized_value"] = m.objVal
        print(optimal_solution_dict)
        return optimal_solution_dict

# m = avgOfAvg_model(num_vars,coeff,4)





# m.optimize()
# if m.status == gp.GRB.OPTIMAL:
#     for var in m.getVars():
#         print(f"{var.varName} = {var.X}")
#
# print(len(candidates))
# for i in range(num_vars):
#     print(i)