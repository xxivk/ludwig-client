import pandas as pd


# Read the dataset into a DataFrame
df = pd.read_csv('preprocessed_data.csv')
df['Seattle'] = df['Seattle'].astype(object)
df['datetime'] = df['datetime'].astype(object)


# Check the data types of all columns
print(df.dtypes)

# Convert the problematic column to a numerical data type
df['Seattle'] = df['Seattle'].astype(float)
# Convert the 'datetime' column to datetime type
df['datetime'] = pd.to_datetime(df['datetime'])


# Verify the updated data types
print(df.dtypes)

# Retry training with the updated dataset
# Your Ludwig training code goes here





# Read the dataset into a pandas DataFrame
#df = pd.read_csv('preprocessed_data.csv')
#
## Fill in missing values in the 'Seattle' column with the previous non-missing value
#df['Seattle'].fillna(method='ffill', inplace=True)
#
## Continue with the rest of your preprocessing and training steps
#import pandas as pd
#
#df = pd.read_csv('preprocessed_data.csv')
#non_numeric_values = df[~df['Seattle'].apply(lambda x: str(x).replace('.', '').isdigit())]
#print(non_numeric_values)
#
#
#
#df['Seattle'] = pd.to_numeric(df['Seattle'], errors='coerce')
#
## Convert the "datetime" column to datetime data type
#df['datetime'] = pd.to_datetime(df['datetime'])
#print(df.dtypes)
#
## Check for missing values
#print(df.isnull().sum())
#
import pandas as pd

# Load your input data into a DataFrame
df = pd.read_csv('preprocessed_data.csv')

# Extract the timeseries input column
timeseries_data = df['Seattle']

# Determine the input shape
input_shape = timeseries_data.shape

print(f"Input Shape: {input_shape}")
