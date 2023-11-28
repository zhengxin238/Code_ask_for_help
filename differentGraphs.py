import networkx as nx
import matplotlib.pyplot as plt

# Create a scale-free graph with 10 nodes and a new node attaching to 2 existing nodes for each new addition.
scale_free_graph = nx.barabasi_albert_graph(10, 2)

nx.draw(scale_free_graph, with_labels=False, node_size=30)
plt.show()

#============================================================

# Create a small-world network with 30 nodes, each connected to 4 nearest neighbors, and rewiring probability of 0.3 watts_strogatz_graph
small_world_graph = nx.watts_strogatz_graph(30, 4, 0.3)
nx.draw(small_world_graph, with_labels=False, node_size=30)
plt.show()

#============================================================
#Random k-out graph not suitable because each vetex will be k degree, this is not realistic for voters

#============================================================

# The Erdős–Rényi (ER) random graph model
n = 20  # Number of nodes
p = 0.2  # Probability of edge existence

# Create an Erdős–Rényi random graph
G_er = nx.erdos_renyi_graph(n, p)
# Visualize the graph
nx.draw(G_er, with_labels=True, node_size=300, font_size=8, font_color='black', font_weight='bold')
plt.show()

#============================================================

# caveman graph model - social network model with strong internal connections and weaker connections between different communities.

# Parameters
num_communities = 3  # Number of communities
nodes_per_community = 5  # Number of nodes in each community

# Create a caveman graph
G_caveman = nx.connected_caveman_graph(num_communities, nodes_per_community)

# Visualize the graph
nx.draw(G_caveman, with_labels=True, node_size=300, font_size=8, font_color='black', font_weight='bold')
plt.show()

#============================================================
#
#
#





