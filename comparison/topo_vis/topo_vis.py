import networkx as nx
import matplotlib.pyplot as plt
import time

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

graph = nx.read_gml(path+"Integra.gml")


# Create the graphs
ER1 = nx.erdos_renyi_graph(27, 0.3)
ER2 = nx.erdos_renyi_graph(27, 0.5)

BA1 = nx.barabasi_albert_graph(27, 2)
BA2 = nx.barabasi_albert_graph(27, 3)

# Write to file
nx.write_gml(ER1,"ER1_27.gml")
nx.write_gml(ER2,"ER2_27.gml")
nx.write_gml(BA1,"BA1_27.gml")
nx.write_gml(BA2,"BA2_27.gml")


# List of graphs
graph_list = [ER1, ER2, BA1, BA2, Bbnplanet, Integra]
titles = ["Erdős-Rényi 1", "Erdős-Rényi 2", "Barabási-Albert 1", "Barabási-Albert 2", "Bpnplanet", "Integra"]



# Create a 2x3 plot
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Plot each graph in its respective subplot
for i, graph in enumerate(graph_list):
    nx.draw(graph, ax=axes[i], with_labels=False, node_color='lightblue', edge_color='gray')
    axes[i].set_title(titles[i])

# Adjust layout for better spacing
plt.tight_layout()
plt.show()
