import networkx as nx
import matplotlib.pyplot as plt

def shortest_path_length_distribution(G):
    # Compute the shortest path lengths for all pairs of nodes
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Flatten the path lengths into a single list
    all_lengths = []
    for source, lengths in path_lengths.items():
        all_lengths.extend(lengths.values())
    
    return all_lengths

def plot_distributions(graphs, labels):
    # Set up the 3x3 grid for plotting
    fig, axes = plt.subplots(3, 3, figsize=(15, 15))
    axes = axes.flatten()
    

    # Plot each graph's shortest path length distribution
    for i, (G, label) in enumerate(zip(graphs, labels)):
        lengths = shortest_path_length_distribution(G)
        axes[i].hist(lengths, bins=range(max(lengths) + 1), alpha=0.7, label=label, density=True)
        axes[i].set_xlabel('Shortest Path Length')
        axes[i].set_ylabel('Frequency')
        axes[i].set_title(f'{label} Distribution')
        axes[i].legend()

    plt.tight_layout()
    plt.show()

# Generate different graphs using various models and parameters
graphs = [
    nx.erdos_renyi_graph(23, 0.1),
    nx.erdos_renyi_graph(23, 0.2),
    nx.erdos_renyi_graph(23, 0.3),
    nx.barabasi_albert_graph(23, 2),
    nx.barabasi_albert_graph(23, 3),
    nx.barabasi_albert_graph(23, 5),
    nx.watts_strogatz_graph(23, 4, 0.1),
    nx.watts_strogatz_graph(23, 6, 0.3),
    nx.read_gml('C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/topology zoo/Janetbackbone.gml')
]

labels = [
    "Erdos-Renyi p=0.1",
    "Erdos-Renyi p=0.2",
    "Erdos-Renyi p=0.3",
    "Barabasi-Albert m=2",
    "Barabasi-Albert m=3",
    "Barabasi-Albert m=5",
    "Watts-Strogatz k=4, p=0.1",
    "Watts-Strogatz k=6, p=0.3",
    "Janet Backbone"
]

# Plot and compare the distributions
plot_distributions(graphs, labels)
