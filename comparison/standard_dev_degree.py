import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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

# Define graphs for each set
node_6 = [ER1_6, ER2_6, BA1_6, BA2_6, Dataxchange, Layer42]
node_13 = [ER1_13, ER2_13, BA1_13, BA2_13, Navigata, Nsfnet]
node_20 = [ER1_20, ER2_20, BA1_20, BA2_20, Quest, Eli]
node_23 = [ER1_23, ER2_23, BA1_23, BA2_23, York, Aconet]
node_24 = [ER1_24, ER2_24, BA1_24, BA2_24, Psinet, Vision]
node_27 = [ER1_27, ER2_27, BA1_27, BA2_27, Bbnplanet, Integra]

er_set = [ER1_6, ER2_6,ER1_13,ER2_13,ER1_20,ER2_20,ER1_23,ER2_23,ER1_24,ER2_24,ER1_27,ER2_27]
ba_set = [BA1_6, BA2_6, BA1_13,BA2_13,BA1_20,BA2_20,BA1_23,BA2_23,BA1_24,BA2_24,BA1_27,BA2_27]

er1_set = [ER1_6,ER1_13,ER1_20,ER1_23,ER1_24,ER1_27]
er2_set = [ER2_6,ER2_13,ER2_20,ER2_23,ER2_24,ER2_27]

ba1_set = [BA1_6,BA1_13,BA1_20,BA1_23,BA1_24,BA1_27]
ba2_set = [BA2_6,BA2_13,BA2_20,BA2_23,BA2_24,BA2_27]

real_world = [Dataxchange, Layer42, Basnet, Gblnet, Gridnet, Abilene, Navigata, Nsfnet, Spiralight, Peer1, Jgn2Plus,Aarnet,Quest,Eli,York, Aconet,Psinet,Vision, Xeex, Uran,Bbnplanet,Integra, Biznet, Cynet,Evolink,Chinanet, Forthnet,Telcove]

def calculate_degree_correlation_coefficient(G):
    return nx.degree_assortativity_coefficient(G)

# List of graph sets
sets_of_graphs = [node_6, node_13, node_20, node_23, node_24, node_27]

sets_of_sets = [er1_set, er2_set, ba1_set, ba2_set]


# Calculate degree correlation coefficients for each graph in each set
coefficients = []
for graph_set in [real_world]:
    coeffs = [calculate_degree_correlation_coefficient(G) for G in graph_set]
    coefficients.append(coeffs)

# Convert list to numpy array for easier manipulation
coefficients = np.array(coefficients)

# Transpose the array to prepare for box plot (each column represents a graph set)
coefficients_transposed = coefficients.T

# Labels for each set
size_labels = ['6 Nodes ', '13 Nodes', '20 Nodes', '23 Nodes', '24 Nodes', '27 Nodes']
set_labels = ['Erdos-Renyi, p=0.3', 'Erdos-Renyo, p=0.5', 'Barabasi-Albert, m=2', 'Barabasi-Albert, m=3']

real_world_labels = ['Real-world']

print(len(real_world))

# Plot the box plot
plt.figure(figsize=(12, 8))
plt.boxplot(coefficients_transposed, labels=real_world_labels, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'), 
            whiskerprops=dict(color='blue'), 
            capprops=dict(color='blue'), 
            medianprops=dict(color='red'))
plt.xlabel('Graph Sets')
plt.ylabel('Degree Correlation Coefficient')
plt.title('Degree Correlation Coefficient Distribution Across 28 real-world network topologies of varying size')
plt.grid(True)
plt.show()
