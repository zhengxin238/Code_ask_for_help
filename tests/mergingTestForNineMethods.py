import networkx as nx

from gb import gb_min_avg, gb_AvgOfMin, gb_minOfMin, gb_maxOfMax, gb_max_avg, gb_avg_avg, gb_MaxOfMin, \
    gb_MinOfMax, gb_AvgOfMax
from basic_functions import graphCode, prefLibParse, function_code
from coefficients import graphCode_Coefficient_MinOfMax, graphCode_Coefficient_MaxOfMin, graphCode_Coefficient_MaxAvg, graphCode_Coefficient_MinAvg, graphCode_Coefficient_MinOfMin, \
    graphCode_Coefficient_AvgAvg, graphCode_Coefficient_AvgOfMin, graphCode_Coefficient_MaxOfMax, graphCode_Coefficient_AvgOfMax
import numpy as np
from pymongo import MongoClient

# pd.set_option('display.max_columns', None)
client = MongoClient('localhost', 27017)
db = client['DataTest_Voting']
collection = db['all_methods_00009-00000001']
# =====================================================
# the input information

# =====================================================
# url = r"https://www.preflib.org/static/data/agh/00009-00000001.soc"
# candidates = list(range(1, (
#         prefLibParse.getNumberOfAlternatives(url) + 1)))
# voters = list(
#     range(1, (prefLibParse.getNumberOfVoters(url) + 1)))
# preference_in_table = prefLibParse.getPreferenceList(url)
#
# # =====================================================
# p_list = np.arange(0.8, 1.0, 0.1).tolist()
# committee_size_list = np.arange(1, len(candidates), 1).tolist()


def getResultIntoDB_allMethods_graphnnormal_diff_committeesize_p(p_list, committee_size_list, candidates, voters,
                                                               preference_in_table, collection_db):
    for committee_size in committee_size_list:
        committee_size_dict = {}
        result_list_dict_temp = {}
        for p in p_list:
            g = graphCode.getGraph(p, len(voters))
            output_file = f"random_graph_allMethods_{committee_size}_{p}"
            nx.write_graphml(g, output_file)
            result_dict_avg_avg = gb_avg_avg.avgOfAvg_model_run_optimization(len(candidates),
                                                                             graphCode_Coefficient_AvgAvg.stepTwoVector_coeff(
                                                                         function_code.borda_score_df_func(candidates,
                                                                                                           voters,
                                                                                                           preference_in_table),
                                                                         graphCode_Coefficient_AvgAvg.getStepOneVector(
                                                                             g,
                                                                             graphCode_Coefficient_AvgAvg.getAdjacencyMatrix(
                                                                                 g),
                                                                             graphCode_Coefficient_AvgAvg.getOneOverFv(
                                                                                 graphCode.getFriendStructureList(g)))),
                                                                             committee_size, voters)
            # print(11111111111111111111111111111111111111111111111111)
            result_dict_max_avg = gb_max_avg.maxOfAvg_model_run_optimization(len(candidates),
                                                                             graphCode_Coefficient_MaxAvg.getCoefficientMatrix(
                                                                         graphCode_Coefficient_MaxAvg.getAdjacencyMatrix(
                                                                             g),
                                                                         function_code.borda_score_df_func(candidates,
                                                                                                           voters,
                                                                                                           preference_in_table),
                                                                         graphCode_Coefficient_MaxAvg.getOneOverFv(
                                                                             graphCode.getFriendStructureList(
                                                                                 g))),
                                                                             committee_size)
            # print(22222222222222222222222222222222222222222222)
            result_dict_min_avg = gb_min_avg.minOfAvg_model_run_optimization(len(candidates),
                                                                             graphCode_Coefficient_MinAvg.getCoefficientMatrix(
                                                                         graphCode_Coefficient_MinAvg.getAdjacencyMatrix(
                                                                             g),
                                                                         function_code.borda_score_df_func(candidates,
                                                                                                           voters,
                                                                                                           preference_in_table),
                                                                         graphCode_Coefficient_MinAvg.getOneOverFv(
                                                                             graphCode.getFriendStructureList(
                                                                                 g))),

                                                                             committee_size)
            # print(333333333333333333333333333333333333333333333333333333)
            result_dict_max_max = gb_maxOfMax.maxOfMax_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MaxOfMax.getCoefficientMatrix(
                                                                          function_code.borda_score_df_func(candidates,
                                                                                                            voters,
                                                                                                            preference_in_table)),
                                                                              committee_size)
            # print(444444444444444444444444444444444444444444444444444444444444444)
            result_dict_min_min = gb_minOfMin.minOfmin_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MinOfMin.getCoefficientMatrix(
                                                                          function_code.borda_score_df_func(candidates,
                                                                                                            voters,
                                                                                                            preference_in_table)),
                                                                              committee_size)
            # print(555555555555555555555555555555555555555555555555555555555555555555555)
            result_dict_max_min = gb_MaxOfMin.maxOfMin_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MaxOfMin.getCoefficientMatrix(
                                                                          function_code.borda_score_df_func(candidates,
                                                                                                            voters,
                                                                                                            preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_MaxOfMin.getNeighbors(g))
            # print(666666666666666666666666666666666666666666666666666666666666666666666666)
            result_dict_min_max = gb_MinOfMax.minOfMax_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MinOfMax.getCoefficientMatrix(
                                                                          function_code.borda_score_df_func(candidates,
                                                                                                            voters,
                                                                                                            preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_MinOfMax.getNeighbors(g),
                                                                              len(candidates) * 2)
            # print(77777777777777777777777777777777777777777777777777777777777777777777777)
            result_dict_avg_min = gb_AvgOfMin.avgOfMin_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_AvgOfMin.getCoefficientMatrix(
                                                                          function_code.borda_score_df_func(candidates,
                                                                                                            voters,
                                                                                                            preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_AvgOfMin.getNeighbors(g))
            # print(888888888888888888888888888888888888888888888888888888888888888888)
            result_dict_avg_max = gb_AvgOfMax.avgOfMax_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_AvgOfMax.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_AvgOfMin.getNeighbors(g), len(candidates)*len(voters) )
            #
            # print(9999999999999999999999999999999999999999999999999999999999999999999999999)
            result_list_dict_temp[str((p))]={}
            result_list_dict_temp[str((p))]["avg_avg"] = result_dict_avg_avg
            result_list_dict_temp[str((p))]["max_avg"] = result_dict_max_avg
            result_list_dict_temp[str((p))]["min_avg"] = result_dict_min_avg
            result_list_dict_temp[str((p))]["max_max"] = result_dict_max_max
            result_list_dict_temp[str((p))]["min_min"] = result_dict_min_min
            result_list_dict_temp[str((p))]["max_min"] = result_dict_max_min
            result_list_dict_temp[str((p))]["min_max"] = result_dict_min_max
            result_list_dict_temp[str((p))]["avg_min"] = result_dict_avg_min
            result_list_dict_temp[str((p))]["avg_max"] = result_dict_avg_max

        committee_size_dict[str(committee_size)] = result_list_dict_temp
        collection_db.insert_one(committee_size_dict)

    return None

def runTestAll(url):
    getResultIntoDB_allMethods_graphnnormal_diff_committeesize_p(np.arange(0.1, 1.0, 0.1).tolist(), np.arange(1, len(list(range(1, (
        prefLibParse.getNumberOfAlternatives(url) + 1)))), 1).tolist(), list(range(1, (
        prefLibParse.getNumberOfAlternatives(url) + 1))), list(
    range(1, (prefLibParse.getNumberOfVoters(url) + 1))),
                                                           prefLibParse.getPreferenceList(url), db['all_methods_00009-00000001'])
    return None

runTestAll(r"https://www.preflib.org/static/data/agh/00009-00000001.soc")
# #
# committee_size = 4
# p = 0.7
#
# num_vars = len(candidates)
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
# #
# # # =====================================================
# # adjacencyMatrix = graphCode_Coefficient_MinAvg.getAdjacencyMatrix(g)
# # # =====================================================
# # oneOverFv = graphCode_Coefficient_MinAvg.getOneOverFv(friend_structure_list)
# # =====================================================
# list_of_neighbors = graphCode_Coefficient_AvgOfMin.getNeighbors(g)
# # =====================================================
# coeff = graphCode_Coefficient_AvgOfMin.getCoefficientMatrix(df_bordaScore)
# # =====================================================f1
# m_value = 2 * len(candidates)
# # =====================================================
# result_dict = gb_AvgOfMin.avgOfMin_model_run_optimization(len(candidates),
#                                                           graphCode_Coefficient_AvgOfMin.getCoefficientMatrix(
#                                                               df_bordaScore), committee_size,
#                                                           graphCode_Coefficient_AvgOfMin.getNeighbors(g))
#
# # =====================================================f1
# result_dict = gb_AvgOfMin.avgOfMin_model_run_optimization(num_vars_a, coeff_a, committee_size_a, list_of_neighbors_a)
# =====================================================f1
# collection.insert_one(result_dict)
# =====================================================f1
# scale_free_graph = nx.barabasi_albert_graph(len(voters), 2)
# friend_structure_list_scale_free = graphCode.getFriendStructureList(scale_free_graph)
# =====================================================f1
