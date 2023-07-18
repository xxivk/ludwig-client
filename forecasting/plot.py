import pandas as pd
import matplotlib.pyplot as plt

# Read the predicted values from the predict.csv file
df_predicted = pd.read_csv('forecasting\Predict\Seattle_next_predictions.csv', header=None)  # Assuming there are no column names in the predict.csv file
predicted_close = df_predicted[0]

# Read the real values from the test.csv file
df_real = pd.read_csv('forecasting\preprocessed_data.csv')
real_rate = df_real['Seattle']

# Plotting the predicted values
plt.plot(predicted_close.index, predicted_close, label='Predicted rating')

# Plotting the real values
plt.plot(real_rate.index, real_rate, label='Real rate')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Rate Value')
plt.title('Predicted vs Real Rate Values')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend
plt.legend()

# Display the plot
plt.show()
