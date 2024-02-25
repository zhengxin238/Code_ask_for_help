import random
import networkx as nx

import numpy as np


def getGraph(p, n):
    g = nx.Graph()
    g.add_nodes_from(range(1, (n + 1)))
    for i in g.nodes():
        for j in g.nodes():
            if (i < j):
                R = random.random()
                if (R < p):
                    g.add_edge(i, j)
        pos = nx.circular_layout(g)
    return g


def getFriendStructureList(g):
    friend_structure_list = []
    for i in g.nodes():
        lFriends = []
        for k in g.neighbors(i):
            lFriends.append(k)
        friend_structure_list.append(lFriends)

    return friend_structure_list


def getOneOverFv(friendStructureList):
    oneOverFvList = []
    for i in friendStructureList:
        if len(i) != 0:
            oneOverFvList.append(1 / len(i))
            # print(len(i))
        else:
            oneOverFvList.append(1)
    return oneOverFvList


def getAdjacencyMatrix(gr):
    am = nx.adjacency_matrix(gr)
    return am.toarray()


def getStepOneVector(g, adjacencyMatrix, oneOverFv):
    stepOneVector = []
    for i in range(g.number_of_nodes()):
        stepOneVector.append(np.dot(oneOverFv, adjacencyMatrix[i]))
    return stepOneVector


def stepTwoVector_coeff(df_bordaScore, stepOneVector):
    stepTwoVector = []
    bsArray = df_bordaScore.to_numpy().transpose()
    # print(bsArray)
    for i in bsArray:
        stepTwoVector.append(np.dot(i, stepOneVector))
    return stepTwoVector
