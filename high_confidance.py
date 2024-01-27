# Define the confidence score threshold
confidence_threshold = 0.2  # Adjust this threshold as needed

# Path to the new text file to save the high confidence detections
output_file = r'D:\Ajit\jetson-train-main\data\eval\high_confidence_detections.txt'

# Open the test.txt file for reading
with open(r'D:\Ajit\jetson-train-main\data\eval\det_test_headphone.txt', 'r') as file:
    lines = file.readlines()

# Open the output file for writing
with open(output_file, 'w') as output:
    # Process each line in the file
    for line in lines:
        # Split the line into components
        components = line.strip().split('\t')
        
        # Extract information from the components
        image_id = components[0]
        confidence_scores = [float(score) for score in components[1::5]]
        bounding_boxes = [(float(components[i]), float(components[i+1]), 
                           float(components[i+2]), float(components[i+3])) 
                          for i in range(2, len(components), 5)]
        
        # Write information about the high confidence detections to the output file
        for score, bbox in zip(confidence_scores, bounding_boxes):
            if score >= confidence_threshold:
                output.write(f"{image_id}\t{score}\t{bbox[0]}\t{bbox[1]}\t{bbox[2]}\t{bbox[3]}\n")
