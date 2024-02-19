import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import function_code

candidates = ['candidate_a', 'candidate_b', 'candidate_c', 'candidate_d', 'candidate_e', 'candidate_f']
voters = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']

preferences_v1 = [candidates[0], candidates[1], candidates[2], candidates[3], candidates[4], candidates[5]]
preferences_v2 = [candidates[1], candidates[3], candidates[4], candidates[2], candidates[5], candidates[0]]
preferences_v3 = [candidates[5], candidates[4], candidates[1], candidates[0], candidates[3], candidates[2]]
preferences_v4 = [candidates[3], candidates[2], candidates[0], candidates[5], candidates[1], candidates[4]]
preferences_v5 = [candidates[2], candidates[0], candidates[5], candidates[4], candidates[3], candidates[1]]
preferences_v6 = [candidates[4], candidates[5], candidates[3], candidates[1], candidates[0], candidates[2]]

preference_in_table = [preferences_v1, preferences_v2, preferences_v3, preferences_v4, preferences_v5, preferences_v6]

friends_v1 = [voters[1], voters[4], voters[5]]
friends_v2 = [voters[0], voters[4], voters[5]]
friends_v3 = [voters[3], voters[4]]
friends_v4 = [voters[2]]
friends_v5 = [voters[0], voters[1], voters[2]]
friends_v6 = [voters[0], voters[1]]

friend_structure_list = [friends_v1, friends_v2, friends_v3, friends_v4, friends_v5, friends_v6]
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


g = nx.Graph()

# Add nodes
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

# Add edges
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 4)
g.add_edge(3, 5)


def getFriendStructureList(g):
    friend_structure_list = []
    for i in g.nodes():
        lFriends = []
        for k in g.neighbors(i):
            lFriends.append(k)
        friend_structure_list.append(lFriends)
    nx.draw(g, with_labels=True)
    plt.show()
    return friend_structure_list


listOfFriendStructure = getFriendStructureList(g)


def getNumberOfFriends(friendStructureList):
    FvList = []
    for i in friendStructureList:
        if len(i) != 0:
            FvList.append(len(i))
        else:
            FvList.append(1)
    return FvList


getNumberOfFriends(listOfFriendStructure)

df_bordaScore = function_code.borda_score_df_func(candidates, voters,
                                                  preference_in_table)

m_value_big = len(candidates)*2


def getCoefficientMatrix(df_bordaScore):
    final_coeff_matrix = df_bordaScore.to_numpy()
    return final_coeff_matrix


final_coeff_matrix = df_bordaScore.to_numpy()
num_of_friends = getNumberOfFriends(listOfFriendStructure)


# Print out neighboring nodes for each node
def getNeighbors(graph_g):
    list_l = []
    for node in graph_g.nodes():
        neighbors = list(graph_g.neighbors(node))
        list_l.append(neighbors)
    return list_l


list_of_neighbors = getNeighbors(g)

