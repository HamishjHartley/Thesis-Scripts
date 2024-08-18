import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from scipy.stats import ks_2samp
import time

def shortest_path_length_distribution(G):
    # Compute the shortest path lengths for all pairs of nodes
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Flatten the path lengths into a single list
    all_lengths = []
    for source, lengths in path_lengths.items():
        all_lengths.extend(lengths.values())
    
    return all_lengths

def plot_graphs_and_distribution(G1, G2, G3, lengths1, lengths2, lengths3, label1, label2, label3):
    # Create a figure with subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 12))

    # Plot the first graph
    nx.draw(G1, ax=axs[0, 0], with_labels=True, node_color='lightblue', edge_color='gray')
    axs[0, 0].set_title(label1)

    # Plot the second graph
    nx.draw(G2, ax=axs[0, 1], with_labels=True, node_color='lightgreen', edge_color='gray')
    axs[0, 1].set_title(label2)

    # Plot the third graph
    nx.draw(G3, ax=axs[1, 0], with_labels=True, node_color='lightcoral', edge_color='gray')
    axs[1, 0].set_title(label3)

    # Plot histograms for the three distributions
    axs[1, 1].hist(lengths1, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.5, label=label1, density=True)
    axs[1, 1].hist(lengths2, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.5, label=label2, density=True)
    axs[1, 1].hist(lengths3, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.5, label=label3, density=True)
    axs[1, 1].set_xlabel('Shortest Path Length')
    axs[1, 1].set_ylabel('Frequency')
    axs[1, 1].set_title('Shortest Path Length Distribution')
    axs[1, 1].legend()

    # Adjust layout
    plt.tight_layout()
    plt.show()

def save_graphs_to_gml(G1, G2, G3, base_filename):
    # Generate a unique timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Create unique filenames using the timestamp
    file1 = f"{base_filename}_G1_{timestamp}.gml"
    file2 = f"{base_filename}_G2_{timestamp}.gml"
    file3 = f"{base_filename}_G3_{timestamp}.gml"

    # Save the graphs to GML format
    nx.write_gml(G1, file1)
    nx.write_gml(G2, file2)
    nx.write_gml(G3, file3)

# Generate two graphs
G1 = nx.erdos_renyi_graph(6, 0.3)  # Set to the same number of nodes as janet
G2 = nx.barabasi_albert_graph(6, 5)  # Set to the same number of nodes as janet

# Real-world graph
janet_backbone = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Janetbackbone.gml'
G_janet = nx.read_gml(janet_backbone)

napnet_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/napnet.gml'
G_napnet = nx.read_gml(napnet_path)

# Compute shortest path length distributions
lengths1 = shortest_path_length_distribution(G1)
lengths2 = shortest_path_length_distribution(G2)
lengths3 = shortest_path_length_distribution(G_napnet)

# Plot and compare the distributions along with the graphs
plot_graphs_and_distribution(G1, G2, G_napnet, lengths1, lengths2, lengths3, 'G1 (Erdos-Renyi)', 'G2 (Barabasi-Albert)', 'G3 (Napnet)')

# Save the generated graphs to GML format with unique filenames
save_graphs_to_gml(G1, G2, G_napnet, 'graph')
