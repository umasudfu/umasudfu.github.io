import os

def list_image_files(folder_path):
    # List of image extensions to check for
    image_extensions = {'.gif', '.jpg', '.png'}

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
folder_path = r'C:\Users\rayde\Downloads\umasudfu\imgs'

# Get the list of image files
image_files = list_image_files(folder_path)

# Define the path for the output TXT file
txt_file_path = ':3.txt'

# Write the formatted list to a TXT file
with open(txt_file_path, 'w') as txt_file:
    for image_file in image_files:
        line = f'''	<img src="images/{image_file}" width="300" height="300">\n'''
        txt_file.write(line)

print(f'Image tags have been saved to {txt_file_path}')
