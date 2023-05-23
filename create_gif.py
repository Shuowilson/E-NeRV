import os
from PIL import Image

# Directory path containing the images
directory = 'data/bunny'

# Create a list to store the image files
image_files = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Append the file path to the list
        image_files.append(os.path.join(directory, filename))

# Create a list to store the image objects
images = []

# Load each image using PIL and append to the list
for image_file in image_files:
    image = Image.open(image_file)
    images.append(image)

# Save the images as a GIF
output_path = 'data/animated.gif'
images[0].save(output_path, save_all=True, append_images=images[1:], optimize=False, duration=200, loop=0)

print(f"Animated GIF created at: {output_path}")