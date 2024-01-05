import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import function_code


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
    print(friend_structure_list)
    nx.draw(g, with_labels=True)
    plt.show()
    return friend_structure_list




df_bordaScore = function_code.borda_score_df_func(function_code.candidates, function_code.voters,
                                                  function_code.preference_in_table)


final_coeff_matrix=df_bordaScore.to_numpy()

print(final_coeff_matrix)





