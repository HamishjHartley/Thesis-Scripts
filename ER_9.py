import networkx as nx
import matplotlib.pyplot as plt

def create_er_graphs():
    # Set up the plot figure with a 3x3 grid of subplots
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    
    # Parameters for generating the graphs
    node_counts = [5, 10, 20]  # Different numbers of nodes
    edge_probs = [0.05, 0.1, 0.2]  # Different probabilities for edge creation

    # Iterate over the grid and create different ER graphs
    for i in range(3):
        for j in range(3):
            # Generate an ER graph with the current parameters
            G = nx.erdos_renyi_graph(node_counts[i], edge_probs[j])
            
            # Get the corresponding subplot and draw the graph
            ax = axs[i, j]
            nx.draw(G, ax=ax, node_size=50, node_color='blue', edge_color='gray', with_labels=False)
            
            # Set the title for each subplot
            ax.set_title(f"n={node_counts[i]}, p={edge_probs[j]}")
    
    # Adjust spacing between subplots
    plt.tight_layout()
    
    # Display the plots
    plt.show()

# Call the function to create and display the graphs
create_er_graphs()
