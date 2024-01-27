import glob
import os
import numpy as np
import sys

current_dir = r"D:\Ajit\jetson-train-main\data\model0110\JPEGImages"
train_pct = 70  # Percentage of data for training
val_pct = 15    # Percentage of data for validation
test_pct = 15   # Percentage of data for testing

file_train = open(r"D:\Ajit\jetson-train-main\data\model0110\ImageSets\train.txt", "w")  
file_val = open(r"D:\Ajit\jetson-train-main\data\model0110\ImageSets\val.txt", "w")  
file_test = open(r"D:\Ajit\jetson-train-main\data\model0110\ImageSets\test.txt", "w")  

# Collect all image files in the current directory
image_files = glob.glob(os.path.join(current_dir, "*.png"))
total_images = len(image_files)

# Shuffle the image files
np.random.shuffle(image_files)

# Calculate the number of images for each set
num_train = int(total_images * (train_pct / 100))
num_val = int(total_images * (val_pct / 100))
num_test = int(total_images * (test_pct / 100))

# Write file paths to respective text files
for i, image_file in enumerate(image_files):
    title, ext = os.path.splitext(os.path.basename(image_file))
    if i < num_train:
        file_train.write(image_file + "\n")
    elif i < num_train + num_val:
        file_val.write(image_file + "\n")
    else:
        file_test.write(image_file + "\n")

file_train.close()
file_val.close()
file_test.close()
