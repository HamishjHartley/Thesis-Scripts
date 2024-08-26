import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, linregress

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

# 6 nodes
Layer42 = nx.read_gml(path+"Layer42.gml")

# 7 nodes
Basnet = nx.read_gml(path+"Basnet.gml")

# 8 nodes
Gblnet = nx.read_gml(path+"Gblnet.gml")

# 9 nodes
Gridnet = nx.read_gml(path+"Gridnet.gml")

# 11 nodes
Abilene = nx.read_gml(path+"Abilene.gml")

# 13 Nodes
Navigata = nx.read_gml(path+"Navigata.gml")

# 13 nodes
Nsfnet = nx.read_gml(path+"Nsfnet.gml")

# 15 nodes
Spiralight = nx.read_gml(path+"Spiralight.gml")

# 16 nodes
Peer1 = nx.read_gml(path+"Peer1.gml")

# 18 nodes
Jgn2Plus = nx.read_gml(path+"Jgn2Plus.gml")

# 19 nodes
Aarnet = nx.read_gml(path+"Aarnet.gml")

# 20 nodes
Quest = nx.read_gml(path+"Quest.gml")

# 20 nodes
Eli = nx.read_gml(path+"EliBackbone.gml")

# 23 nodes
York = nx.read_gml(path+"York.gml")

# 23 nodes
Aconet = nx.read_gml(path+"Aconet.gml")

# 24 nodes
Psinet = nx.read_gml(path+"Psinet.gml")

# 24 nodes
Vision = nx.read_gml(path+"VisionNet.gml")

# 24 nodes
Xeex = nx.read_gml(path+"Xeex.gml")

# 24 nodes
Uran = nx.read_gml(path+"Uran.gml")

# 27 nodes
Bbnplanet = nx.read_gml(path+"Bbnplanet.gml")

# 27 nodes
Integra = nx.read_gml(path+"Integra.gml")

# 29 nodes
Biznet = nx.read_gml(path+"Biznet.gml")

# 30 nodes
Cynet = nx.read_gml(path+"Cynet.gml")

# 37 nodes
Evolink = nx.read_gml(path+"Evolink.gml")

# 42 nodes
Chinanet = nx.read_gml(path+"Chinanet.gml")

# 62 nodes
Forthnet = nx.read_gml(path+"Forthnet.gml")

# 73 nodes
Telcove = nx.read_gml(path+"Telcove.gml")

def shortest_path_length_distribution(G):
    # Compute the shortest path lengths for all pairs of nodes
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    
    # Flatten the path lengths into a single list
    all_lengths = []
    for source, lengths in path_lengths.items():
        all_lengths.extend(lengths.values())
    
    return all_lengths

def match_lengths(list1, list2):
    # Match the lengths by truncating the longer list
    min_len = min(len(list1), len(list2))
    return list1[:min_len], list2[:min_len]

graph1 = BA1_24
graph2 = Psinet
graph1_name = "Barabasi-Albert, m=2"
graph2_name = "Psinet"

# Compute shortest path length distributions for the specified graphs
lengths1 = shortest_path_length_distribution(graph1)
lengths2 = shortest_path_length_distribution(graph2)

# Match the lengths of the distributions
matched_lengths1, matched_lengths2 = match_lengths(lengths1, lengths2)

# Calculate Pearson correlation coefficient
corr, _ = pearsonr(matched_lengths1, matched_lengths2)

# Calculate line of best fit
slope, intercept, r_value, p_value, std_err = linregress(matched_lengths1, matched_lengths2)
line = np.array(matched_lengths1) * slope + intercept

# Plot the correlation with a scatter plot and line of best fit
plt.figure(figsize=(8, 6))
plt.scatter(matched_lengths1, matched_lengths2, alpha=0.5, color='blue', label=f'{graph1_name}')
plt.scatter(matched_lengths2, matched_lengths1, alpha=0.5, color='orange', label=f'{graph2_name}')
plt.plot(matched_lengths1, line, color='red', label=f'Line of Best Fit (r = {r_value:.2f})')
plt.xlabel(f'Shortest Path Lengths in {graph1_name}')
plt.ylabel(f'Shortest Path Lengths in {graph2_name}')
plt.title(f'Correlation between {graph1_name} and {graph2_name} (r = {corr:.2f})')
plt.legend()
plt.show()