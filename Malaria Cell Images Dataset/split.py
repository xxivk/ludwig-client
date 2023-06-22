import os
import shutil

# Create the new directories
base_dir = "C:/Users/crypto/Desktop/ludwig-client/Covid-19 Novel Coronavirus 2019"
directories = ["Parasitized_train", "Parasitized_validation", "Parasitized_test", "Uninfected_all", "Uninfected_train", "Uninfected_validation", "Uninfected_test"]

for directory in directories:
    os.makedirs(os.path.join(base_dir, directory), exist_ok=True)

# Transfer data into the specific directories
print("---Parasitized---")
parasitized_all_dir = os.path.join(base_dir, "Parasitized_all")
parasitized_train_dir = os.path.join(base_dir, "Parasitized_train")
parasitized_validation_dir = os.path.join(base_dir, "Parasitized_validation")
parasitized_test_dir = os.path.join(base_dir, "Parasitized_test")

parasitized_files = os.listdir(parasitized_all_dir)
for i in range(5000):
    shutil.copy2(os.path.join(parasitized_all_dir, parasitized_files[i]), parasitized_train_dir)

for i in range(5000, 10000):
    shutil.copy2(os.path.join(parasitized_all_dir, parasitized_files[i]), parasitized_validation_dir)

for i in range(10000, len(parasitized_files)):
    shutil.copy2(os.path.join(parasitized_all_dir, parasitized_files[i]), parasitized_test_dir)

print("---Uninfected---")
uninfected_all_dir = os.path.join(base_dir, "Uninfected_all")
uninfected_train_dir = os.path.join(base_dir, "Uninfected_train")
uninfected_validation_dir = os.path.join(base_dir, "Uninfected_validation")
uninfected_test_dir = os.path.join(base_dir, "Uninfected_test")

uninfected_files = os.listdir(uninfected_all_dir)
for i in range(5000):
    shutil.copy2(os.path.join(uninfected_all_dir, uninfected_files[i]), uninfected_train_dir)

for i in range(5000, 10000):
    shutil.copy2(os.path.join(uninfected_all_dir, uninfected_files[i]), uninfected_validation_dir)

for i in range(10000, len(uninfected_files)):
    shutil.copy2(os.path.join(uninfected_all_dir, uninfected_files[i]), uninfected_test_dir)
