import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def display_and_save_all_images(source_directory, output_file, grid_size=(19, 19), image_size=(128, 128)):
    # List all image files in the source directory
    image_files = [f for f in os.listdir(source_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()  # Sort files alphabetically

    # Create a figure to hold the grid of images
    fig, axes = plt.subplots(nrows=grid_size[0], ncols=grid_size[1], figsize=(20, 20))
    
    # Flatten axes array for easy iteration
    axes = axes.flatten()

    # Display each image on the grid
    for ax, img_file in zip(axes, image_files):
        img_path = os.path.join(source_directory, img_file)
        img = Image.open(img_path).resize(image_size)
        ax.imshow(img)
        ax.set_xticks([])  # Remove x-axis marker
        ax.set_yticks([])  # Remove y-axis marker
        ax.set_frame_on(False)  # No borders or frame around individual images

    # Hide empty subplots if any
    for ax in axes[len(image_files):]:
        ax.axis('off')

    # Adjust layout to minimize gaps between images
    plt.subplots_adjust(wspace=0.05, hspace=0.05)

    # Add a title and possibly more aesthetic features
    fig.suptitle('Gallery of X-Ray Images', fontsize=20, fontweight='bold', color='navy', va='top')

    # Save the entire grid as a single image
    plt.savefig(output_file, dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.show()
    plt.close()

# Example usage
source_directory = os.getcwd()
output_file = 'path_to_your_output_file.jpg'
display_and_save_all_images(source_directory, output_file)

