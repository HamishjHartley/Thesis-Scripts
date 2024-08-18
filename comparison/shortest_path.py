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
    plt.hist(lengths1, bins=range(max(lengths1 + lengths2+lengths3) + 1), alpha=0.5, label=label1, density=True, color="Blue")
    plt.hist(lengths2, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.5, label=label2, density=True, color="Red")
    plt.hist(lengths3, bins=range(max(lengths1 + lengths2 + lengths3) + 1), alpha=0.7, label=label3, density=True, color="Green")
    plt.xlabel('Shortest Path Length')
    plt.ylabel('Frequency')
    plt.title('Shortest Path Length Distribution')
    plt.legend()
    plt.show()

def plot_distribution_6(lengths1, lengths2, lengths3, lengths4, lengths5, lengths6, label1, label2, label3, label4, label5, label6):
    # Plot histograms for the six distributions
    max_length = max(lengths1 + lengths2 + lengths3 + lengths4 + lengths5 + lengths6)
    bins = range(max_length + 1)
    
    plt.hist(lengths1, bins=bins, alpha=0.5, label=label1, density=True, color="Blue")
    plt.hist(lengths2, bins=bins, alpha=0.5, label=label2, density=True, color="Red")
    plt.hist(lengths3, bins=bins, alpha=0.5, label=label3, density=True, color="Green")
    plt.hist(lengths4, bins=bins, alpha=0.5, label=label4, density=True, color="Purple")
    plt.hist(lengths5, bins=bins, alpha=0.5, label=label5, density=True, color="Orange")
    plt.hist(lengths6, bins=bins, alpha=0.5, label=label6, density=True, color="Cyan")
    
    plt.xlabel('Shortest Path Length')
    plt.ylabel('Frequency')
    plt.title('Shortest Path Length Distribution')
    plt.legend()
    plt.show()

def plot_line_distribution(lengths1, lengths2, lengths3, lengths4, lengths5, lengths6, label1, label2, label3, label4, label5, label6):
    # Compute frequency distributions
    max_length = max(lengths1 + lengths2 + lengths3 + lengths4 + lengths5 + lengths6)
    bins = np.arange(0, max_length + 1)
    
    freq1, _ = np.histogram(lengths1, bins=bins, density=True)
    freq2, _ = np.histogram(lengths2, bins=bins, density=True)
    freq3, _ = np.histogram(lengths3, bins=bins, density=True)
    freq4, _ = np.histogram(lengths4, bins=bins, density=True)
    freq5, _ = np.histogram(lengths5, bins=bins, density=True)
    freq6, _ = np.histogram(lengths6, bins=bins, density=True)

    # Plot line distributions
    plt.plot(bins[:-1], freq1, label=label1, linestyle='-', color='blue')
    plt.plot(bins[:-1], freq2, label=label2, linestyle='-', color='red')
    plt.plot(bins[:-1], freq3, label=label3, linestyle='-', color='green')
    plt.plot(bins[:-1], freq4, label=label4, linestyle='-', color='purple')
    plt.plot(bins[:-1], freq5, label=label5, linestyle='-', color='orange')
    plt.plot(bins[:-1], freq6, label=label6, linestyle='-', color='cyan')
    
    plt.xlabel('Shortest Path Length')
    plt.ylabel('Frequency')
    plt.title('Shortest Path Length Distribution Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()


#Load in graphs for comparison
topo_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Topology Set/'
ER1_6 = nx.read_gml(topo_path+'ER1_6.gml')
ER2_6 = nx.read_gml(topo_path+'ER2_6.gml')

BA1_6 = nx.read_gml(topo_path+'BA1_6.gml')
BA2_6 = nx.read_gml(topo_path+'BA2_6.gml')

ER1_13 = nx.read_gml(topo_path+'ER1_13.gml')
ER2_13 = nx.read_gml(topo_path+'ER2_13.gml')

BA1_13 = nx.read_gml(topo_path+'BA1_13.gml')
BA2_13 = nx.read_gml(topo_path+'BA2_13.gml')

ER1_20 = nx.read_gml(topo_path+'ER1_20.gml')
ER2_20 = nx.read_gml(topo_path+'ER2_20.gml')

BA1_20 = nx.read_gml(topo_path+'BA1_20.gml')
BA2_20 = nx.read_gml(topo_path+'BA2_20.gml')

ER1_23 = nx.read_gml(topo_path+'ER1_23.gml')
ER2_23 = nx.read_gml(topo_path+'ER2_23.gml')

BA1_23 = nx.read_gml(topo_path+'BA1_23.gml')
BA2_23 = nx.read_gml(topo_path+'BA2_23.gml')

ER1_24 = nx.read_gml(topo_path+'ER1_24.gml')
ER2_24 = nx.read_gml(topo_path+'ER2_24.gml')

BA1_24 = nx.read_gml(topo_path+'BA1_24.gml')
BA2_24 = nx.read_gml(topo_path+'BA2_24.gml')

ER1_27 = nx.read_gml(topo_path+'ER1_27.gml')
ER2_27 = nx.read_gml(topo_path+'ER2_27.gml')

BA1_27 = nx.read_gml(topo_path+'BA1_27.gml')
BA2_27 = nx.read_gml(topo_path+'BA2_27.gml')
# Real-world graph
path = 'C:/Users/theha/OneDrive/Documents/GitHub/3D-internet-zoo/dataset/'
# 6 nodes
Dataxchange = nx.read_gml(path+"Dataxchange.gml")
Layer42 = nx.read_gml(path+"Layer42.gml")

# 13 Nodes
Navigata = nx.read_gml(path+"Navigata.gml")
Nsfnet = nx.read_gml(path+"Nsfnet.gml")

# 20 nodes
Quest = nx.read_gml(path+"Quest.gml")
Eli = nx.read_gml(path+"EliBackbone.gml")

# 23 nodes
York = nx.read_gml(path+"York.gml")
Aconet = nx.read_gml(path+"Aconet.gml")

# 24 nodes
Psinet = nx.read_gml(path+"Psinet.gml")
Vision = nx.read_gml(path+"VisionNet.gml")

# 27 nodes
Bbnplanet = nx.read_gml(path+"Bbnplanet.gml")
Integra = nx.read_gml(path+"Integra.gml")


# Compute shortest path length distributions
lengths1 = shortest_path_length_distribution(ER1_6)
lengths2 = shortest_path_length_distribution(ER2_6)

lengths3 = shortest_path_length_distribution(BA1_27)
lengths4 = shortest_path_length_distribution(BA2_27)

lengths5 = shortest_path_length_distribution(Dataxchange)
lengths6 = shortest_path_length_distribution(Integra)

# Plot and compare the distributions
plot_distribution(lengths1,lengths2,lengths5, 'Erdos-Renyi, 6 nodes, p=0.3', 'Erdos-Renyi, 6 nodes, p=0.5', 'Dataxchange')

#plot_distribution_6(lengths1, lengths2, lengths3, lengths4, lengths5, lengths6,'ER1_6', 'BA2_6', 'ER1_13', 'BA2_13', 'ER1_20', 'BA2_20')


#plot_line_distribution(lengths1, lengths2, lengths3, lengths4, lengths5, lengths6, 'Erdos-Renyi, 27 nodes, p=0.3', 'Erdos-Renyi, 27 nodes, p=0.5', 'Barabasi-Albert, 27 nodes, m=2', 'Barabasi-Albert, 27 nodes, m=3', 'Bbnplanet', 'Integra')

#ks_stat, p_value = ks_2samp(lengths1, lengths2)
#print(f"KS Statistic: {ks_stat}, p-value: {p_value}")