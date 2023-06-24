#import pandas as pd
#
## Read the CSV file
#df = pd.read_csv('train with ray\\ratings_sample.csv')
#
## Clean the 'sentence' column
#df['sentence'] = df['sentence'].str.strip()  # Remove leading/trailing whitespaces
#df['sentence'] = df['sentence'].str.replace('\n', ' ')  # Remove newlines
#df['sentence'] = df['sentence'].str.replace('\r', ' ')  # Remove carriage returns
#
## Save the cleaned data back to a CSV file
#df.to_csv('cleaned_file.csv', index=False)



import os

# Set the PYARROW_FS_URI environment variable
os.environ["PYARROW_FS_URI"] = "file:///"

# Specify the absolute file paths
config_path = "train with ray\\config.yaml"
dataset_path = "train with ray\\ratings_sample.csv"

# Run the Ludwig command with adjusted file paths
os.system(f'ludwig train --config "{config_path}" --dataset "{dataset_path}"')
