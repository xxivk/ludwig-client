import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


import pandas as pd
import matplotlib.pyplot as plt

# Read the predicted values from the predict.csv file
df_predicted = pd.read_csv('Predict/Close_predictions.csv', header=None)
predicted_close = df_predicted[0]

# Read the real values from the test.csv file
df_real = pd.read_csv('val_data.csv', parse_dates=['timestamp'])
df_real = df_real.set_index('timestamp')
real_close = df_real['close']

# Interpolate missing values
df_real_interpolated = df_real.interpolate()

# Sort the DataFrame by the index in ascending order
df_real_interpolated = df_real_interpolated.sort_index()

# Extract the close prices
real_close = df_real_interpolated['close']
date_index = df_real_interpolated.index

# Plotting the predicted values
plt.plot(date_index, predicted_close[:len(date_index)], label='Predicted Close')

# Plotting the real values
plt.plot(date_index, real_close, label='Real Close')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Predicted vs Real Close Prices')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend
plt.legend()

# Display the plot
plt.show()
