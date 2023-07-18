import pandas as pd
import matplotlib.pyplot as plt

# Read the predicted values from the predict.csv file
df_predicted = pd.read_csv('Predict/Close_next_predictions.csv', header=None)  # Assuming there are no column names in the predict.csv file
predicted_close = df_predicted[0]

#df_predict = pd.read_csv('Predict/Close_next_predictions.csv', dtype={'Close_next': float})
#predicted_close = df_predict['Close_next']

# Read the real values from the test.csv file
df_real = pd.read_csv('test.csv' , parse_dates=['DateIndex'])
real_close = df_real['Close']
date_index = df_real['DateIndex']

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


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the predicted values from the predict.csv file
df_predicted = pd.read_csv('Predict/Close_next_predictions.csv', header=None)  # Assuming there are no column names in the predict.csv file
predicted_close = df_predicted[0]

# Read the real values from the test.csv file
df_real = pd.read_csv('test.csv', parse_dates=['DateIndex'])
df_real = df_real.set_index('DateIndex')

# Interpolate missing values
df_real_interpolated = df_real.interpolate()

# Extract the close prices
real_close = df_real_interpolated['Close']
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
