from itertools import combinations
import pandas as pd

import gb_max_avg
import graphCode_Coefficient_MaxAvg
import prefLibParse
import graphCode
import function_code
import graphCode_Coefficient_AvgAvg
import gb_avg_avg
import numpy as np
from pymongo import MongoClient
from preflibtools.instances import PrefLibInstance

# pd.set_option('display.max_columns', None)
client = MongoClient('localhost', 27017)
db = client['votingdb']
collection = db['NewMaxOfAvg00015-00000001']
# =====================================================
# the input information

url = r"https://www.preflib.org/static/data/cleanweb/00015-00000001.soc"
candidates = list(range(1, (
        prefLibParse.getNumberOfAlternatives(r"https://www.preflib.org/static/data/cleanweb/00015-00000001.soc") + 1)))
voters = list(
    range(1, (prefLibParse.getNumberOfVoters(r"https://www.preflib.org/static/data/cleanweb/00015-00000001.soc") + 1)))
preference_in_table = prefLibParse.getPreferenceList(r"https://www.preflib.org/static/data/cleanweb/00015-00000001.soc")

# =====================================================
p_list = np.arange(0.99, 1.01, 0.01).tolist()
committee_size_list = np.arange(1, len(candidates)-len(candidates)+3, 1).tolist()


def getResultIntoDB_maxOfavg_graphnnormal_diff_committeesize_p(p_list, committee_size_list, candidates, voters,
                                                               preference_in_table, collection_db):
    committee_size_dict = {}
    result_list_dict_temp = {}
    for committee_size in committee_size_list:
        for p in p_list:
            result_dict = gb_max_avg.maxOfAvg_model_run_optimization(len(candidates),
                                                                     graphCode_Coefficient_MaxAvg.getCoefficientMatrix(
                                                                         graphCode_Coefficient_MaxAvg.getAdjacencyMatrix(
                                                                             graphCode.getGraph(p, len(voters))),
                                                                         function_code.borda_score_df_func(candidates,
                                                                                                           voters,
                                                                                                           preference_in_table),
                                                                         graphCode_Coefficient_MaxAvg.getOneOverFv(
                                                                             graphCode.getFriendStructureList(
                                                                                 graphCode.getGraph(p, len(voters))))),
                                                                     committee_size)
            result_list_dict_temp[str((p))] = result_dict
        committee_size_dict[str(committee_size)] = result_list_dict_temp
        collection_db.insert_one(committee_size_dict)

    return None


getResultIntoDB_maxOfavg_graphnnormal_diff_committeesize_p(p_list, committee_size_list, candidates, voters,
                                                           preference_in_table, collection)
# # committee_size = 4
# p = 0.7
#
# # graph and friendsstructure =====================================================f1 (p, committee_size)
#
# g = graphCode.getGraph(p, len(voters))
# friend_structure_list = graphCode.getFriendStructureList(g)
#
# # ===================================================== (candidates, voters, preference_in_table)
# # voter-candidate borda score dataframe
#
# df_bordaScore = function_code.borda_score_df_func(candidates, voters, preference_in_table)

# =====================================================
#
# adjacencyMatrix = graphCode_Coefficient_MaxAvg.getAdjacencyMatrix(g)
# # =====================================================
# oneOverFv = graphCode_Coefficient_MaxAvg.getOneOverFv(friend_structure_list)
# # =====================================================
# coeff = graphCode_Coefficient_MaxAvg.getCoefficientMatrix(adjacencyMatrix, df_bordaScore, oneOverFv)
# ===================================================== put into less steps
# coeff = graphCode_Coefficient_MaxAvg.getCoefficientMatrix(graphCode_Coefficient_MaxAvg.getAdjacencyMatrix(graphCode.getGraph(p, len(voters))), function_code.borda_score_df_func(candidates, voters, preference_in_table),
#                                                           graphCode_Coefficient_MaxAvg.getOneOverFv(
#                                                               graphCode.getFriendStructureList(graphCode.getGraph(p, len(voters)))))
# =====================================================

# result_dict = gb_max_avg.maxOfAvg_model_run_optimization(len(candidates), graphCode_Coefficient_MaxAvg.getCoefficientMatrix(graphCode_Coefficient_MaxAvg.getAdjacencyMatrix(graphCode.getGraph(p, len(voters))), function_code.borda_score_df_func(candidates, voters, preference_in_table),
#                                                           graphCode_Coefficient_MaxAvg.getOneOverFv(
#                                                               graphCode.getFriendStructureList(graphCode.getGraph(p, len(voters))))), committee_size)
# result_dict = gb_avg_avg.run_optimization(gb_avg_avg.avgOfAvg_model(len(candidates),
#                                                                     graphCode_Coefficient_AvgAvg.stepTwoVector_coeff(
#                                                                         function_code.borda_score_df_func(candidates,
#                                                                                                           voters,
#                                                                                                           preference_in_table),
#                                                                         graphCode_Coefficient_AvgAvg.getStepOneVector(
#                                                                             graphCode.getGraph(p, len(voters)),
#                                                                             graphCode_Coefficient_AvgAvg.getAdjacencyMatrix(
#                                                                                 graphCode.getGraph(p, len(voters))),
#                                                                             graphCode_Coefficient_AvgAvg.getOneOverFv(
#                                                                                 graphCode.getFriendStructureList(graphCode.getGraph(p, len(voters)))))),
#                                                                     committee_size))

# =====================================================f1


# collection.insert_one(result_dict)
# =====================================================f1
# scale_free_graph = nx.barabasi_albert_graph(len(voters), 2)
# friend_structure_list_scale_free = graphCode.getFriendStructureList(scale_free_graph)
# =====================================================f1
