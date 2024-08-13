import networkx as nx
import matplotlib.pyplot as plt

# Parameters for the BA model
num_nodes = 10  # Total number of nodes in the graph
num_edges_to_attach = 1  # Number of edges to attach from a new node to existing nodes

# Generate the BA graph
G = nx.barabasi_albert_graph(num_nodes, num_edges_to_attach)

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(G, node_size=50, node_color='blue', edge_color='gray', with_labels=False)
plt.title("Barabási-Albert (BA) Model Graph")
plt.show()
