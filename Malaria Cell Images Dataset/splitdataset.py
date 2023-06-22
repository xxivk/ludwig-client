import os
import random
import shutil

def split_dataset(source_path, target_train_path, target_validation_path, target_test_path, split_ratio):
    # Create target directories if they don't exist
    os.makedirs(target_train_path, exist_ok=True)
    os.makedirs(target_validation_path, exist_ok=True)
    os.makedirs(target_test_path, exist_ok=True)

    # Get the list of image files in the source directory
    image_files = os.listdir(source_path)

    # Shuffle the image files randomly
    random.shuffle(image_files)

    # Calculate the number of samples for each split
    total_samples = len(image_files)
    train_samples = int(total_samples * split_ratio[0])
    validation_samples = int(total_samples * split_ratio[1])
    test_samples = total_samples - train_samples - validation_samples

    # Copy files to the respective target directories
    for i, image_file in enumerate(image_files):
        source_file = os.path.join(source_path, image_file)
        if i < train_samples:
            target_file = os.path.join(target_train_path, image_file)
        elif i < train_samples + validation_samples:
            target_file = os.path.join(target_validation_path, image_file)
        else:
            target_file = os.path.join(target_test_path, image_file)
        shutil.copy(source_file, target_file)

# Example usage
source_path = "Covid-19 Novel Coronavirus 2019"
target_train_path = "Covid-19 Novel Coronavirus 2019/Parasitized_train"
target_validation_path = "Covid-19 Novel Coronavirus 2019/Parasitized_validation"
target_test_path = "Covid-19 Novel Coronavirus 2019/Parasitized_test"
split_ratio = [0.6, 0.2]  # 60% for training, 20% for validation, 20% for testing

split_dataset(source_path, target_train_path, target_validation_path, target_test_path, split_ratio)
