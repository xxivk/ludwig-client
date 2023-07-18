import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file
data = pd.read_csv('train1h.csv')

# Split the data into training and validation sets
train_data, val_data = train_test_split(data, test_size=0.2)  # 80% for training, 20% for validation

# Save the split datasets to separate CSV files
train_data.to_csv('train_data.csv', index=False)
val_data.to_csv('val_data.csv', index=False)
