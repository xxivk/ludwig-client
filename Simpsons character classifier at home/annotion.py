
import os

# Directory path containing the Simpsons character dataset
dataset_dir = 'Simpsons character classifier at home\simpsons_dataset'

# Output annotation directory
output_dir = 'annotations'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over the subdirectories (character folders) in the dataset directory
for character_dir in os.listdir(dataset_dir):
    character_path = os.path.join(dataset_dir, character_dir)
    # Skip any non-directory files
    if not os.path.isdir(character_path):
        continue

    # Generate the annotation file name
    annotation_file = f'{character_dir}.csv'
    annotation_path = os.path.join(output_dir, annotation_file)

    # Open the annotation file for writing
    with open(annotation_path, 'w') as f:
        # Iterate over the image files in the character directory
        for image_file in os.listdir(character_path):
            image_path = os.path.join(character_path, image_file)
            # Write the image path and character label to the annotation file
            f.write(f'{image_path}\t{character_dir}\n')
