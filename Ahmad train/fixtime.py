#
#import pandas as pd
#
## Read the CSV file
#df = pd.read_csv('train.csv')
#
## Convert the 'DateIndex' column to datetime format
#df['DateIndex'] = pd.to_datetime(df['DateIndex'], infer_datetime_format=True)
#
## Save the updated dataframe back to a CSV file
#df.to_csv('train.csv', index=False)



import pandas as pd

# Read the CSV file
df = pd.read_csv('test.csv')

df['DateIndex'] = pd.to_datetime(df['DateIndex'], format='%Y-%m-%d %H:%M:%S')


# Save the updated dataframe back to a CSV file
df.to_csv('test.csv', index=False)
