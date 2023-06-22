#import pandas as pd
#
## Specify the correct file path and name
#file_path = 'forecasting\\temperature.csv'
#
## Load the CSV file
#df = pd.read_csv(file_path)
#
## Convert the problematic column to float data type
#df['Seattle'] = df['Seattle'].astype(float)
#
## Save the modified DataFrame back to a CSV file
#df.to_csv('fixed_file.csv', index=False)
#

import pandas as pd

# Read the CSV file
df = pd.read_csv('forecasting//temperature.csv')

# Convert the 'datetime' column to datetime type with inferred format
df['datetime'] = pd.to_datetime(df['datetime'], infer_datetime_format=True)

# Convert the 'Seattle' column to numerical type
df['Seattle'] = pd.to_numeric(df['Seattle'], errors='coerce')

# Save the preprocessed DataFrame to a new CSV file
df.to_csv('preprocessed_data.csv', index=False)
