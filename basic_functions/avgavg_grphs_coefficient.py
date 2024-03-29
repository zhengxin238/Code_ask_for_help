import networkx as nx
import gurobipy as gp
from gurobipy import *
import function_code
import prefLibParse
from coefficients import graphCode_Coefficient_AvgAvg

# =========================================================
candidates = list(range(1, (
        prefLibParse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
voters = list(
    range(1, (prefLibParse.getNumberOfVoters(r"https://www.preflib.org/static/data/agh/00009-00000001.soc") + 1)))
preference_in_table = prefLibParse.getPreferenceList(r"https://www.preflib.org/static/data/agh/00009-00000001.soc")
committee_size = 3

bs_df = function_code.borda_score_df_func(candidates, voters, preference_in_table)
# =========================================================


erdos_renyi_graph = graphCode_Coefficient_AvgAvg.getGraph(0.03, len(voters))
friend_structure_list_erdos_renyi_0 = graphCode_Coefficient_AvgAvg.getFriendStructureList(erdos_renyi_graph)

scale_free_graph = nx.barabasi_albert_graph(len(voters), 2)
friend_structure_list_scale_free_0 = graphCode_Coefficient_AvgAvg.getFriendStructureList(scale_free_graph)
friend_structure_list_scale_free = [[element + 1 for element in inner_list] for inner_list in friend_structure_list_scale_free_0]

small_world_graph = nx.watts_strogatz_graph(len(voters), 3, 0.25)
friend_structure_list_small_world_0 = graphCode_Coefficient_AvgAvg.getFriendStructureList(small_world_graph)
friend_structure_list_small_world = [[element + 1 for element in inner_list] for inner_list in friend_structure_list_small_world_0]
# =========================================================

oneOverFv_erdos_renyi = graphCode_Coefficient_AvgAvg.getOneOverFv(friend_structure_list_erdos_renyi_0)
oneOverFv_scale_free = graphCode_Coefficient_AvgAvg.getOneOverFv(friend_structure_list_scale_free)
oneOverFv_small_world = graphCode_Coefficient_AvgAvg.getOneOverFv(friend_structure_list_small_world)

# =========================================================

adjacencyMatrix_erdos_renyi = graphCode_Coefficient_AvgAvg.getAdjacencyMatrix(erdos_renyi_graph)
adjacencyMatrix_scale_free = graphCode_Coefficient_AvgAvg.getAdjacencyMatrix(scale_free_graph)
adjacencyMatrix_small_world = graphCode_Coefficient_AvgAvg.getAdjacencyMatrix(small_world_graph)

# =========================================================

stepOneVector_erdos_renyi = graphCode_Coefficient_AvgAvg.getStepOneVector(erdos_renyi_graph,
                                                                          adjacencyMatrix_erdos_renyi,
                                                                          oneOverFv_erdos_renyi)
stepOneVector_scale_free = graphCode_Coefficient_AvgAvg.getStepOneVector(scale_free_graph, adjacencyMatrix_scale_free,
                                                                         oneOverFv_scale_free)
stepOneVector_small_world = graphCode_Coefficient_AvgAvg.getStepOneVector(small_world_graph,
                                                                          adjacencyMatrix_small_world,
                                                                          oneOverFv_small_world)

stepTwoVector_erdos_renyi = graphCode_Coefficient_AvgAvg.stepTwoVector_coeff(bs_df, stepOneVector_erdos_renyi)
stepTwoVector_scale_free = graphCode_Coefficient_AvgAvg.stepTwoVector_coeff(bs_df, stepOneVector_scale_free)
stepTwoVector_small_world = graphCode_Coefficient_AvgAvg.stepTwoVector_coeff(bs_df, stepOneVector_small_world)

m_er = Model("er")
m_sf = Model("sf")
m_sw = Model("sw")
num_vars = len(candidates)

x = {}
for i in range(num_vars):
    x[i] = m_er.addVar(name=f'x_{i}', vtype=GRB.BINARY)
objective_expression_erdos_renyi = quicksum(stepTwoVector_erdos_renyi[i] * x[i] for i in range(num_vars))
obj = m_er.setObjective(objective_expression_erdos_renyi, GRB.MAXIMIZE)
m_er.addConstr(quicksum(x[i] for i in range(num_vars)) == committee_size, "er")

m_er.optimize()
if m_er.status == gp.GRB.OPTIMAL:
    for var in m_er.getVars():
        print(f"{var.varName} = {var.X}")

y = {}
for i in range(num_vars):
    y[i] = m_sf.addVar(name=f'x_{i}', vtype=GRB.BINARY)
objective_expression_scale_free = quicksum(stepTwoVector_scale_free[i] * y[i] for i in range(num_vars))
obj = m_sf.setObjective(objective_expression_scale_free, GRB.MAXIMIZE)
m_sf.addConstr(quicksum(y[i] for i in range(num_vars)) == committee_size, "sf")

m_sf.optimize()
if m_sf.status == gp.GRB.OPTIMAL:
    for var in m_sf.getVars():
        print(f"{var.varName} = {var.X}")

z = {}
for i in range(num_vars):
    z[i] = m_sw.addVar(name=f'x_{i}', vtype=GRB.BINARY)
objective_expression_small_world = quicksum(stepTwoVector_small_world[i] * z[i] for i in range(num_vars))
obj = m_sw.setObjective(objective_expression_small_world, GRB.MAXIMIZE)
m_sw.addConstr(quicksum(z[i] for i in range(num_vars)) == committee_size, "sf")

m_sw.optimize()
if m_sw.status == gp.GRB.OPTIMAL:
    for var in m_sw.getVars():
        print(f"{var.varName} = {var.X}")
