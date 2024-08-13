import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_images_in_grid(image_paths):
    # Create a 3x3 grid
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))
    axes = axes.flatten()  # Flatten the 3x3 array of axes

    for i, ax in enumerate(axes):
        if i < len(image_paths):
            img = mpimg.imread(image_paths[i])  # Read the image
            ax.imshow(img)  # Display the image in the grid
            ax.axis('off')  # Hide the axes (ticks and labels)
        else:
            ax.axis('off')  # If there are fewer than 9 images, turn off extra subplots

    plt.tight_layout()  # Adjust subplots to fit into the figure area.
    plt.show()

# Example usage:
image_paths = [
    'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet1.png', 'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet2.png', 'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet3.png',
    'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet4.png', 'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet5.png', 'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet6.png',
    'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet7.png', 'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet8.png', 'C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet9.png'
]

display_images_in_grid(image_paths)

#"C:/Users/theha/OneDrive/Desktop/Masters Project/figures/topo_comparison/janet1.png"