import os

# Directory containing the images
image_folder = r"D:\Ajit\jetson-train-main\data\model0110\JPEGImages"

# List of image file extensions to consider
image_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp']  # Add more extensions as needed

# Iterate through files in the directory
for filename in os.listdir(image_folder):
    # Check if the file has one of the specified image extensions
    if any(filename.endswith(ext) for ext in image_extensions):
        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        # Create the new filename by replacing the current extension with .png
        new_filename = os.path.splitext(filename)[0] + '.png'
        # Construct the full paths of the original and new files
        old_filepath = os.path.join(image_folder, filename)
        new_filepath = os.path.join(image_folder, new_filename)
        # Rename the file
        os.rename(old_filepath, new_filepath)

