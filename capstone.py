import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load historical stock data (replace 'stock_data.csv' with your file)
data = pd.read_csv('stock_data.csv')

# Assuming the dataset has 'Date' and 'Close' columns
# For demonstration purposes, other features like volume, high, low, etc., can be used

# Data Preprocessing
data['Date'] = pd.to_datetime(data['Date'])
data = data.set_index('Date')

# Feature Selection (Using 'Close' price for prediction)
data['Prediction'] = data['Close'].shift(-1)  # Shifting prices up by 1 day to predict next day

# Separate the feature set and target variable
X = data.drop('Prediction', axis=1)
X = X[:-1]  # Remove the last row as it will have NaN in the prediction column
y = data['Prediction']
y = y[:-1]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model Building (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Predictions
predictions = model.predict(X_test)

# Visualization (plotting actual vs predicted prices)
plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test.values, label='Actual Price')
plt.plot(y_test.index, predictions, label='Predicted Price', linestyle='--')
plt.title('Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
