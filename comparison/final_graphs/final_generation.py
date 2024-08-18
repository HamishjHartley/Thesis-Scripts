import networkx as nx
import matplotlib.pyplot as plt

# Create the graphs
ER1 = nx.erdos_renyi_graph(23, 0.5)
ER2 = nx.erdos_renyi_graph(23, 0.3)

BA1 = nx.barabasi_albert_graph(23, 2)
BA2 = nx.barabasi_albert_graph(23, 3)

# 6 nodes
napnet_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Napnet.gml'
NAPNET = nx.read_gml(napnet_path)

# 6 nodes
bas_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Basnet.gml'
BASNET = nx.read_gml(bas_path)

# 16 nodes
er_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Ernet.gml'
#ERNET = nx.read_gml(er_path)

#garr_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Garr201201.gml'
#GARR = nx.read_gml(garr_path)

network_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/NetworkUsa.gml'
USA = nx.read_gml(network_path)

vision_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/VisionNet.gml'
VISION = nx.read_gml(vision_path)

cesnet_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Cesnet201006.gml'
CESNET = nx.read_gml(cesnet_path)

#belnet_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Belnet2010.gml'
#BELNET = nx.read_gml(belnet_path)

# 31 nodes
rnp_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/rnp.gml'
RNP = nx.read_gml(rnp_path)

# 43 nodes
lambda_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/LambdaNet.gml'
LAMBDA_NET = nx.read_gml(lambda_path)

gts_ce = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/GtsCe.gml'
#GTS_CE = nx.read_gml(gts_ce)

miss_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Missouri.gml'
MISS = nx.read_gml(miss_path)
#ion_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Ion.gml'
#ION = nx.read_gml(ion_path)

iris_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/Iris.gml'
IRIS = nx.read_gml(iris_path)

# Write to file
nx.write_gml(ER1,"ER1")
nx.write_gml(ER2,"ER2")
nx.write_gml(BA1,"BA1")
nx.write_gml(BA2,"BA2")

#hib_path = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/Thesis-Scripts/topology zoo/HiberniaIreland.gml'
#HIBERNIA = nx.read_gml(hib_path)

# List of graphs
graph_list = [ER1, ER2, BA1, BA2, MISS, VISION]
titles = ["Erdős-Rényi 1", "Erdős-Rényi 2", "Barabási-Albert 1", "Barabási-Albert 2", "Napnet", "Basnet"]


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