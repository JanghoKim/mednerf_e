
import os
from PIL import Image
from torchvision import transforms
import glob

# Define the transformation for center cropping
transform = transforms.Compose([
    transforms.CenterCrop(80)  # Crop a 64x64 block from the center of the image
])


# Path to your directory of images
image_directory = os.getcwd()
output_directory = image_directory + "/croped_real"
os.makedirs(output_directory, exist_ok=True)


# Process each image in the directory
for image_path in glob.glob(os.path.join(image_directory, '*.png')):  # Assuming the images are PNGs
    image = Image.open(image_path).convert('RGB')  # Open and convert to RGB for consistency
    image = image.resize((128, 128))  # Ensure the image is 128x128

    # Apply the cropping transformation
    cropped_image = transform(image)

    # Save the cropped image
    base_name = os.path.basename(image_path)  # Get the original file name
    save_path = os.path.join(output_directory, base_name)  # Create a path to save the cropped image
    cropped_image.save(save_path)

print("All images have been cropped and saved.")