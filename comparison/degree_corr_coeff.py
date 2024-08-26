import networkx as nx
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

import networkx as nx
import matplotlib.pyplot as plt

def calculate_degree_correlation_coefficient(G):
    # Calculate the degree correlation (assortativity) coefficient
    return nx.degree_assortativity_coefficient(G)

def plot_degree_correlation_coefficients(graphs, labels):
    coefficients = [calculate_degree_correlation_coefficient(G) for G in graphs]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, coefficients, color='skyblue')
    plt.xlabel('Graphs')
    plt.ylabel('Degree Correlation Coefficient')
    plt.title('Degree Correlation Coefficients comparison')
    plt.ylim(-1, 1)  # Assortativity coefficient ranges from -1 to 1
    plt.grid(True)

    # Add text annotations to display the value of each bar
    for bar, coef in zip(bars, coefficients):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{coef:.2f}', 
                 ha='center', va='bottom', fontsize=12, color='black')
    
    plt.show()

# List of graphs and labels
graphs = [ER1_27, ER2_27, BA1_27, BA2_27, Bbnplanet, Integra]
labels = ['Erdos-Renyi 1', 'Erdos-Renyi 2', 'Barabasi-Albert 1', 'Barabasi-Albert, 2', 'Bbnplanet', 'Integra']

# Plot the degree correlation coefficients
plot_degree_correlation_coefficients(graphs, labels)
