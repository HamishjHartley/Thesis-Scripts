import networkx as nx
import matplotlib.pyplot as plt

# Load the GEANT graph from the GML file
geant = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/topology zoo/Geant2012.gml' 
janet_backbone = 'C:/Users/theha/OneDrive/Desktop/Masters Project/Scripts/topology zoo/Janetbackbone.gml'
G = nx.read_gml(geant)

# Draw the graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Position nodes using the Fruchterman-Reingold force-directed algorithm
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

# Display the plot
plt.title("GEANT Internet Topology")
plt.show()

