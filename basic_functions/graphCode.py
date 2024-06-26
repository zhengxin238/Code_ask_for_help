import random
import networkx as nx

import numpy as np



def getGraph(p, n):
    g = nx.Graph()
    g.add_nodes_from(range(1, (n + 1)))  # Add nodes from 1 to n

    # Add an edge between the first two nodes
    if n >= 2:
        g.add_edge(1, 2)

    for i in range(2, n + 1):  # Start iterating from node 3
        for j in range(i + 1, n + 1):  # Iterate over remaining nodes
            R = random.random()  # Generate a random number between 0 and 1
            if R < p:  # If the random number is less than the probability p
                g.add_edge(i, j)  # Add an edge between nodes i and j based on probability p
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
# print(listOfFriendStructure)


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
# print(oneOverFv)


def getAdjacencyMatrix(gr):
    am = nx.adjacency_matrix(gr)
    return am.toarray()


# adjacencyMatrix = getAdjacencyMatrix(g)
# # print(adjacencyMatrix)


def getStepOneVector(g, adjacencyMatrix, oneOverFv):
    stepOneVector = []
    for i in range(g.number_of_nodes()):
        stepOneVector.append(np.dot(oneOverFv, adjacencyMatrix[i]))
    return stepOneVector


# stepOneVector = getStepOneVector(g, adjacencyMatrix, oneOverFv)

# # print(stepOneVector)
# df_bordaScore = function_code.borda_score_df_func(function_code.candidates, function_code.voters,
#                                                   function_code.preference_in_table)

# bs_transposed= df_bordaScore.transpose()
# bs_array = df_bordaScore.to_numpy()
# bs_array_transposed = bs_transposed.to_numpy()
# print(bs_array)
# print(bs_array_transposed)


def stepTwoVector(df_bordaScore, stepOneVector):
    stepTwoVector = []
    bsArray = df_bordaScore.to_numpy().transpose()
    print(bsArray)
    for i in bsArray:
        stepTwoVector.append(np.dot(i, stepOneVector))
    return stepTwoVector


# coefficient = stepTwoVector(df_bordaScore, stepOneVector)
# print(stepTwoVector(df_bordaScore, stepOneVector))
"""getFriendStructureList(0.03, 154)"""


