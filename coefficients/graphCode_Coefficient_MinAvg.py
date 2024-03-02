import random
import networkx as nx
import numpy as np


# candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
# voters = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']
#
# preferences_v1 = [candidates[0], candidates[1], candidates[2], candidates[3], candidates[4], candidates[5]]
# preferences_v2 = [candidates[1], candidates[3], candidates[4], candidates[2], candidates[5], candidates[0]]
# preferences_v3 = [candidates[5], candidates[4], candidates[1], candidates[0], candidates[3], candidates[2]]
# preferences_v4 = [candidates[3], candidates[2], candidates[0], candidates[5], candidates[1], candidates[4]]
# preferences_v5 = [candidates[2], candidates[0], candidates[5], candidates[4], candidates[3], candidates[1]]
# preferences_v6 = [candidates[4], candidates[5], candidates[3], candidates[1], candidates[0], candidates[2]]
#
# preference_in_table = [preferences_v1, preferences_v2, preferences_v3, preferences_v4, preferences_v5, preferences_v6]
#
# friends_v1 = [voters[1], voters[4], voters[5]]
# friends_v2 = [voters[0], voters[4], voters[5]]
# friends_v3 = [voters[3], voters[4]]
# friends_v4 = [voters[2]]
# friends_v5 = [voters[0], voters[1], voters[2]]
# friends_v6 = [voters[0], voters[1]]
#
# friend_structure_list = [friends_v1, friends_v2, friends_v3, friends_v4, friends_v5, friends_v6]
def getGraph(p, n):
    g = nx.Graph()
    g.add_nodes_from(range(1, (n + 1)))
    for i in g.nodes():
        for j in g.nodes():
            if (i < j):
                R = random.random()
                if (R < p):
                    g.add_edge(i, j)
        # pos = nx.circular_layout(g)
    return g


# g = nx.Graph()
#
# # Add nodes
# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)
# g.add_node(5)
# g.add_node(6)
#
# # Add edges
# g.add_edge(1, 2)
# g.add_edge(1, 5)
# g.add_edge(1, 6)
# g.add_edge(2, 5)
# g.add_edge(2, 6)
# g.add_edge(3, 4)
# g.add_edge(3, 5)


def getFriendStructureList(g):
    friend_structure_list = []
    for i in g.nodes():
        lFriends = []
        for k in g.neighbors(i):
            lFriends.append(k)
        friend_structure_list.append(lFriends)
    # print(friend_structure_list)
    # nx.draw(g, with_labels=True)
    # plt.show()
    return friend_structure_list


# listOfFriendStructure = getFriendStructureList(g)
# print(1111111111111111)
# print(listOfFriendStructure)
# for i in range(0, len(listOfFriendStructure)):
#     print(i)
#     print(listOfFriendStructure[i])
#
# print(1111111111111111)

def getOneOverFv(friendStructureList):
    oneOverFvList = []
    for i in friendStructureList:
        if len(i) != 0:
            oneOverFvList.append(1 / len(i))
            # print(len(i))
        else:
            oneOverFvList.append(1)
    return oneOverFvList


# oneOverFv = getOneOverFv(listOfFriendStructure)
# oneOverFv = np.array(oneOverFv)
# print(1111111111111111)
# print(oneOverFv)
# print(1111111111111111)
def getAdjacencyMatrix(gr):
    am = nx.adjacency_matrix(gr)
    return am.toarray()


# adjacencyMatrix = getAdjacencyMatrix(g)
# # print(adjacencyMatrix)
#
# df_bordaScore = function_code.borda_score_df_func(candidates, voters,
#                                                   preference_in_table)


# def getCoefficientMatrix(adjMatrix, df_bordaScore, oneOverFvList):
#     bs_transposedMatrix = df_bordaScore.transpose().to_numpy()
#     coeff_matrix = []
#     final_coeff_matrix = []
#     for row_aj in adjMatrix:
#         row_appd = []
#         coeff_matrix.append(row_appd)
#         for line_bs in bs_transposedMatrix:
#             vector_value = np.dot(row_aj,line_bs)
#             row_appd.append(vector_value)
#     oneOverFv_np = np.array(oneOverFvList)
#     for i in range(0, len(oneOverFv_np)):
#         final_value = oneOverFv_np[i] * coeff_matrix[i]
#         final_coeff_matrix.append(final_value)
#     return final_coeff_matrix


# bs_transposedMatrix = df_bordaScore.transpose().to_numpy()
# coeff_matrix = []
# final_coeff_matrix = []
# for row_aj in adjacencyMatrix:
#     row_appd = []
#     coeff_matrix.append(row_appd)
#     for line_bs in bs_transposedMatrix:
#         vector_value = np.dot(row_aj, line_bs)
#         row_appd.append(vector_value)
# # print(np.array(coeff_matrix))
# oneOverFv_np = np.array(oneOverFv)
# for i in range(0, len(oneOverFv_np)):
#     final_coeff_matrix.append(oneOverFv_np[i]*np.array(coeff_matrix)[i])
#
# # print(final_coeff_matrix)
#
# final_coeff_matrix = np.array(final_coeff_matrix)
# print(final_coeff_matrix)


def getCoefficientMatrix(adjacencyMatrix, df_bordaScore, oneOverFv):
    bs_transposedMatrix = df_bordaScore.transpose().to_numpy()
    coeff_matrix = []
    final_coeff_matrix = []
    for row_aj in adjacencyMatrix:
        row_appd = []
        coeff_matrix.append(row_appd)
        for line_bs in bs_transposedMatrix:
            vector_value = np.dot(row_aj, line_bs)
            row_appd.append(vector_value)
    # print(np.array(coeff_matrix))
    oneOverFv_np = np.array(oneOverFv)
    for i in range(0, len(oneOverFv_np)):
        final_coeff_matrix.append(oneOverFv_np[i] * np.array(coeff_matrix)[i])

    return np.array(final_coeff_matrix)

# print(getCoefficientMatrix(adjacencyMatrix,df_bordaScore,oneOverFv))