import networkx as nx
import matplotlib.pyplot as plt
import time

def create_and_save_erdos_renyi_graph(n, p, index):
    # Generate an Erdős-Rényi graph
    G = nx.erdos_renyi_graph(n, p)

    # Plot the graph
    plt.figure()
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(f'Erdős-Rényi Graph {index}')
    plt.show()

    # Save the graph to a GML file with a unique filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f'erdos_renyi_graph_{index}_{timestamp}.gml'
    nx.write_gml(G, filename)

    print(f"Graph {index} saved as {filename}")

# Parameters for the Erdős-Rényi graphs
n_nodes = 5
p_values = [0.1, 0.2, 0.3]  # Different probabilities for edge creation

# Generate, display, and save three different Erdős-Rényi graphs
for i, p in enumerate(p_values, start=1):
    create_and_save_erdos_renyi_graph(n_nodes, p, i)
