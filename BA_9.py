import networkx as nx
import matplotlib.pyplot as plt

def create_ba_graphs():
    # Set up the plot figure with a 3x3 grid of subplots
    fig, axs = plt.subplots(3, 3, figsize=(15, 15))
    
    # Parameters for generating the graphs
    node_counts = [20, 30, 40]  # Different numbers of nodes
    edge_counts = [1, 2, 3]  # Different numbers of edges to attach

    # Iterate over the grid and create different BA graphs
    for i in range(3):
        for j in range(3):
            # Generate a BA graph with the current parameters
            G = nx.barabasi_albert_graph(node_counts[i], edge_counts[j])
            
            # Get the corresponding subplot and draw the graph
            ax = axs[i, j]
            nx.draw(G, ax=ax, node_size=50, node_color='blue', edge_color='gray', with_labels=False)
            
            # Set the title for each subplot
            ax.set_title(f"n={node_counts[i]}, m={edge_counts[j]}")
    
    # Adjust spacing between subplots
    plt.tight_layout()
    
    # Display the plots
    plt.show()

# Call the function to create and display the graphs
create_ba_graphs()
