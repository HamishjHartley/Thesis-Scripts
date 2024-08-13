import networkx as nx
import numpy as np
from scipy.stats import pearsonr

# Create two random graphs
G1 = nx.erdos_renyi_graph(23, 0.1) # Set to 23 nodes to match janet_backbone
G2 = nx.barabasi_albert_graph(100, 5)


# Import real-world graph
geant_file = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/topology zoo/Geant2012.gml'
janet_backbone = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/topology zoo/Janetbackbone.gml'


janet_backbone = nx.read_gml(janet_backbone)

# Get the degree sequences

# Random graph
degree_seq_G1 = [d for n, d in G1.degree()]
degree_seq_G2 = [d for n, d in G2.degree()]

# Real-world graph
degree_seq_GEANT = [d for n, d in janet_backbone.degree()]

# Calculate Pearson correlation between the degree sequences
correlation, _ = pearsonr(degree_seq_G1, janet_backbone)

print(f"Degree sequence correlation: {correlation}")