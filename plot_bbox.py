import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Path to the directory containing images
image_dir = r"D:\Ajit\jetson-train-main\data\model0110\JPEGImages"  # Replace this with the path to your image directory

# Path to the text file containing detections
detections_file = r"D:\Ajit\jetson-train-main\data\eval\det_test_headphone.txt"  # Replace this with the path to your detections file

# Read detections from the text file
all_detections = {}
with open(detections_file, 'r') as file:
    for line in file:
        data = line.strip().split('\t')
        image_id = int(data[0])
        confidence = float(data[1])
        bbox = [float(coord) for coord in data[2:]]
        if image_id not in all_detections:
            all_detections[image_id] = []
        all_detections[image_id].append((confidence, bbox))

# Process each image and its detections
for image_id, detections in all_detections.items():
    # Load the image
    image_path = f"{image_dir}\\{image_id}.png"
    image = Image.open(image_path)

    # Create a figure and axis object
    fig, ax = plt.subplots(1)

    # Display the image
    ax.imshow(image)

    # Add bounding boxes to the image
    for confidence, bbox in detections:
        x_min, y_min, x_max, y_max = bbox
        
        # Create a rectangle patch
        rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                 linewidth=2, edgecolor='r', facecolor='none')

        # Add the rectangle patch to the axis
        ax.add_patch(rect)

        # Add confidence score as text near the box
        ax.text(x_min, y_min, f'Confidence: {confidence:.2f}', backgroundcolor='red', fontsize=8, color='white')

    # Show the image with bounding boxes
    plt.show()
