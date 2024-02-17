import gb_AvgOfMin
import graphCode
import graphCode_Coefficient_AvgOfMin
import prefLibParse
import function_code
import numpy as np
from pymongo import MongoClient
import preflib_format

# pd.set_option('display.max_columns', None)
client = MongoClient('localhost', 27017)
db = client['votingdb']
collection = db['AvgOfMin00009-00000001']
# =====================================================
# the input information
url = r"https://www.preflib.org/static/data/agh/00009-00000001.soc"
candidates = list(range(1, (
        prefLibParse.getNumberOfAlternatives(url) + 1)))
voters = list(
    range(1, (prefLibParse.getNumberOfVoters(url) + 1)))
preference_in_table = prefLibParse.getPreferenceList(url)

# =====================================================
p_list = np.arange(0.05, 0.07, 0.01).tolist()
committee_size_list = np.arange(1, len(candidates) - len(candidates) + 2, 1).tolist()


def getResultIntoDB_avgOfmin_graphnnormal_diff_committeesize_p(p_list, committee_size_list, candidates, voters,
                                                               preference_in_table, collection_db):
    for committee_size in committee_size_list:
        committee_size_dict = {}
        result_list_dict_temp = {}
        for p in p_list:
            g = graphCode.getGraph(p, len(voters))
            result_dict = gb_AvgOfMin.avgOfMin_model_run_optimization(len(candidates),
                                                                      graphCode_Coefficient_AvgOfMin.getCoefficientMatrix(
                                                                          function_code.borda_score_df_func(candidates,
                                                                                                            voters,
                                                                                                            preference_in_table)),
                                                                      committee_size,
                                                                      graphCode_Coefficient_AvgOfMin.getNeighbors(g))

            result_list_dict_temp[str((p))] = result_dict
        committee_size_dict[str(committee_size)] = result_list_dict_temp
        collection_db.insert_one(committee_size_dict)

    return None


getResultIntoDB_avgOfmin_graphnnormal_diff_committeesize_p(p_list, committee_size_list, candidates, voters,
                                                           preference_in_table, collection)
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