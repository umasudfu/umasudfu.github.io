import os
import json

def list_image_files(folder_path):
    # List of image extensions to check for
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

    # List to store image file names
    image_files = []

    # Walk through the folder
    for filename in os.listdir(folder_path):
        # Get the file extension
        _, ext = os.path.splitext(filename)

        # Check if the file is an image
        if ext.lower() in image_extensions:
            image_files.append(filename)

    return image_files

# Define the path to your image folder
folder_path = r'C:\Users\rayde\Downloads\umasudfu.github.io-main\Loadingscreen_images'

# Get the list of image files
image_files = list_image_files(folder_path)

# Define the path for the output JSON file
json_file_path = 'image_files.json'

# Write the list to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(image_files, json_file, indent=4)

print(f'Image filenames have been saved to {json_file_path}')