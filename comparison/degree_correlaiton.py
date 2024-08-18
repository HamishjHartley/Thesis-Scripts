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

def degree_correlation_matrix(G):
    # Get the degree of each node
    degrees = dict(G.degree())
    
    # Get the maximum degree to define the size of the matrix
    max_degree = max(degrees.values())
    
    # Initialize a matrix of zeros with dimensions (max_degree+1) x (max_degree+1)
    matrix = np.zeros((max_degree+1, max_degree+1), dtype=int)
    
    # Fill in the matrix with degree correlations
    for u, v in G.edges():
        deg_u = degrees[u]
        deg_v = degrees[v]
        matrix[deg_u][deg_v] += 1
        if deg_u != deg_v:  # Ensure symmetry
            matrix[deg_v][deg_u] += 1
    
    return matrix

def plot_degree_correlation_matrices(graphs, labels):
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()  # Flatten the 2D array of axes into a 1D array for easy indexing

    for i, (G, label) in enumerate(zip(graphs, labels)):
        matrix = degree_correlation_matrix(G)
        ax = axes[i]
        cax = ax.imshow(matrix, origin='lower', cmap='Blues')
        ax.set_title(label)
        ax.set_xlabel('Degree of Node u')
        ax.set_ylabel('Degree of Node v')
        ax.grid(False)
    
    # Adjust spacing between plots and add a colorbar
    fig.tight_layout()
    fig.colorbar(cax, ax=axes, orientation='vertical', fraction=0.02, pad=0.02)
    plt.show()


# List of graphs and labels
graphs = [ER1_6, BA2_6, ER1_13, BA2_13, ER1_20, BA2_20]
labels = ['ER1_6', 'BA2_6', 'ER1_13', 'BA2_13', 'ER1_20', 'BA2_20']

# Plot the degree correlation matrices
plot_degree_correlation_matrices(graphs, labels)