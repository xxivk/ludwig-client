#import os
#import csv
#
#dataset_dir = 'C:/Users/crypto/Desktop/ludwig-client/Simpsons character classifier at home/simpsons_dataset'
#csv_file = 'dataset.csv'
#
#with open(csv_file, 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(['image_name', 'label'])
#
#    for root, _, files in os.walk(dataset_dir):
#        for file in files:
#            if file.endswith('.jpg'):
#                image_path = os.path.join(root, file)
#                label = os.path.basename(root)
#                writer.writerow([image_path, label])
#
#print("CSV file created successfully!")


import os
import csv

# Path to the Simpsons dataset folder
dataset_folder = 'Simpsons character classifier at home\simpsons_dataset'

# Output CSV file path
csv_file = 'Simpsons character classifier at home/simpsons_dataset.csv'

# List to store image names and corresponding labels
data = []

# Iterate over the subfolders in the dataset folder
for subfolder in os.listdir(dataset_folder):
    subfolder_path = os.path.join(dataset_folder, subfolder)
    
    # Only process subfolders (character names)
    if os.path.isdir(subfolder_path):
        label = subfolder
        
        # Iterate over the images in the subfolder
        for image_name in os.listdir(subfolder_path):
            # Append the image name (without the path) and label to the data list
            data.append((image_name, label))

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image_name', 'label'])  # Write the header
    writer.writerows(data)  # Write the image names and labels

print("CSV file created successfully.")
#