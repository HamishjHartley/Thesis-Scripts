import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from scipy.stats import ks_2samp

def shortest_path_length_distribution(G):
    # Compute the shortest path lengths for all pairs of nodes
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Flatten the path lengths into a single list
    all_lengths = []
    for source, lengths in path_lengths.items():
        all_lengths.extend(lengths.values())
    
    return all_lengths

def plot_distribution(lengths1, lengths2, lengths3, label1, label2, label3):
    # Plot histograms for the two distributions
    plt.hist(lengths1, bins=range(max(lengths1 + lengths2+lengths3) + 1), alpha=0.5, label=label1, density=True)
    plt.hist(lengths2, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.5, label=label2, density=True)
    plt.hist(lengths3, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.5, label=label3, density=True)
    plt.xlabel('Shortest Path Length')
    plt.ylabel('Frequency')
    plt.title('Shortest Path Length Distribution')
    plt.legend()
    plt.show()

# Generate two graphs
G1 = nx.erdos_renyi_graph(23, 0.1) # Set to the same number of nodes as janet
G2 = nx.barabasi_albert_graph(23, 5) # Set to the same number of nodes as janet

# Real-world graph
janet_backbone = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/topology zoo/Janetbackbone.gml'
G_janet = nx.read_gml(janet_backbone)

# Compute shortest path length distributions
lengths1 = shortest_path_length_distribution(G1)
lengths2 = shortest_path_length_distribution(G2)
lengths3 = shortest_path_length_distribution(G_janet)

# Plot and compare the distributions
# plot_distribution(lengths1, lengths2, lengths3,'G1 (Erdos-Renyi)', 'G2 (Barabasi-Albert)', 'G3 (Janet Backbone)')


ks_stat, p_value = ks_2samp(lengths1, lengths2)
print(f"KS Statistic: {ks_stat}, p-value: {p_value}")
