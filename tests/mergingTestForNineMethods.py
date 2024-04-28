import os
import uuid

import networkx as nx

from gb import gb_min_avg, gb_AvgOfMin, gb_minOfMin, gb_maxOfMax, gb_max_avg, gb_avg_avg, gb_MaxOfMin, \
    gb_MinOfMax, gb_AvgOfMax
from basic_functions import graphCode, prefLibParse, function_code
from coefficients import graphCode_Coefficient_MinOfMax, graphCode_Coefficient_MaxOfMin, graphCode_Coefficient_MaxAvg, \
    graphCode_Coefficient_MinAvg, graphCode_Coefficient_MinOfMin, \
    graphCode_Coefficient_AvgAvg, graphCode_Coefficient_AvgOfMin, graphCode_Coefficient_MaxOfMax, \
    graphCode_Coefficient_AvgOfMax
import numpy as np
from pymongo import MongoClient

collection = MongoClient('localhost', 27017)['DataTest_Voting']['all_methods_00009-00000001']


def write_graph_to_folder(G, output_folder, output_file):
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Write the graph to a GraphML file in the specified folder
    output_path = os.path.join(output_folder, output_file)
    nx.write_graphml(G, output_path)


def getResultIntoDB_allMethods_graphnnormal_diff_committeesize_p(p_list, committee_size_list, candidates, voters,
                                                                 preference_in_table, collection_db, dsvalue):
    for committee_size in committee_size_list:
        committee_size_dict = {}
        result_list_dict_temp = {}
        last_value = 1
        for p in p_list:
            g = graphCode.getGraph(p, len(voters))
            output_file = f"random_graph_{committee_size}_{p}_{dsvalue}_{uuid.uuid4()}"
            last_value += 1
            write_graph_to_folder(g, "D:/output", output_file)
            result_dict_avg_avg = gb_avg_avg.avgOfAvg_model_run_optimization(len(candidates),
                                                                             graphCode_Coefficient_AvgAvg.stepTwoVector_coeff(
                                                                                 function_code.borda_score_df_func(
                                                                                     candidates,
                                                                                     voters,
                                                                                     preference_in_table),
                                                                                 graphCode_Coefficient_AvgAvg.getStepOneVector(
                                                                                     g,
                                                                                     graphCode_Coefficient_AvgAvg.getAdjacencyMatrix(
                                                                                         g),
                                                                                     graphCode_Coefficient_AvgAvg.getOneOverFv(
                                                                                         graphCode.getFriendStructureList(
                                                                                             g)))),
                                                                             committee_size, voters)
            # print(11111111111111111111111111111111111111111111111111)
            result_dict_max_avg = gb_max_avg.maxOfAvg_model_run_optimization(len(candidates),
                                                                             graphCode_Coefficient_MaxAvg.getCoefficientMatrix(
                                                                                 graphCode_Coefficient_MaxAvg.getAdjacencyMatrix(
                                                                                     g),
                                                                                 function_code.borda_score_df_func(
                                                                                     candidates,
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
                                                                                 function_code.borda_score_df_func(
                                                                                     candidates,
                                                                                     voters,
                                                                                     preference_in_table),
                                                                                 graphCode_Coefficient_MinAvg.getOneOverFv(
                                                                                     graphCode.getFriendStructureList(
                                                                                         g))),

                                                                             committee_size)
            # print(333333333333333333333333333333333333333333333333333333)

            result_dict_max_max = gb_maxOfMax.maxOfMax_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MaxOfMax.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode.getFriendStructureList(g),
                                                                              2 * len(candidates))
            # print(444444444444444444444444444444444444444444444444444444444444444)
            result_dict_min_min = gb_minOfMin.minOfmin_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MinOfMin.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode.getFriendStructureList(g))
            # print(555555555555555555555555555555555555555555555555555555555555555555555)
            result_dict_max_min = gb_MaxOfMin.maxOfMin_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MaxOfMin.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_MaxOfMin.getNeighbors(
                                                                                  g))
            # print(666666666666666666666666666666666666666666666666666666666666666666666666)
            result_dict_min_max = gb_MinOfMax.minOfMax_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_MinOfMax.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_MinOfMax.getNeighbors(
                                                                                  g),
                                                                              len(candidates) * 2)
            # print(77777777777777777777777777777777777777777777777777777777777777777777777)
            result_dict_avg_min = gb_AvgOfMin.avgOfMin_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_AvgOfMin.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_AvgOfMin.getNeighbors(
                                                                                  g))
            # print(888888888888888888888888888888888888888888888888888888888888888888)
            result_dict_avg_max = gb_AvgOfMax.avgOfMax_model_run_optimization(len(candidates),
                                                                              graphCode_Coefficient_AvgOfMax.getCoefficientMatrix(
                                                                                  function_code.borda_score_df_func(
                                                                                      candidates,
                                                                                      voters,
                                                                                      preference_in_table)),
                                                                              committee_size,
                                                                              graphCode_Coefficient_AvgOfMin.getNeighbors(
                                                                                  g), len(candidates) * len(voters))
            #
            # print(9999999999999999999999999999999999999999999999999999999999999999999999999)
            result_list_dict_temp[str((p))] = {}
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


def runTestAll(url, collection_db, dsvalue):
    for i in range(1, 11):
        getResultIntoDB_allMethods_graphnnormal_diff_committeesize_p(np.arange(0.1, 1.1, 0.1).tolist(),
                                                                     np.arange(1, len(list(range(1, (
                                                                             prefLibParse.getNumberOfAlternatives(
                                                                                 url) + 1)))), 1).tolist(),
                                                                     list(range(1, (
                                                                             prefLibParse.getNumberOfAlternatives(
                                                                                 url) + 1))), list(
                range(1, (prefLibParse.getNumberOfVoters(url) + 1))),
                                                                     prefLibParse.getPreferenceList(url), collection_db,
                                                                     dsvalue)

    return None


def readURL_test_data(database_location, file_path_with_URL):
    with open(file_path_with_URL, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove leading and trailing whitespace from the line
            line = line.strip()
            parts = line.split('/')
            # Get the last part of the URL (the filename)
            filename = parts[-1]
            # Remove the '.soc' extension
            filename_without_extension = filename.split('.')[0]
            # Extract the desired substring
            substring = filename_without_extension
            """filename_without_extension.split('-')[1]"""
            runTestAll(line, database_location[substring], substring)
