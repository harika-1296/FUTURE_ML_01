import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("Everything is working perfectly!")
import pandas as pd

# Load CSV dataset
df = pd.read_csv("superstore.csv", encoding='latin1')

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract features
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Group data
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

print(monthly_sales.head())
import matplotlib.pyplot as plt

monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))
monthly_sales = monthly_sales.sort_values('Date')

plt.figure()
plt.plot(monthly_sales['Date'], monthly_sales['Sales'])
plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
monthly_sales['Time'] = range(len(monthly_sales))
from sklearn.linear_model import LinearRegression

X = monthly_sales[['Time']]
y = monthly_sales['Sales']

model = LinearRegression()
model.fit(X, y)
future_steps = 6

future_time = pd.DataFrame({
    'Time': range(len(monthly_sales), len(monthly_sales) + future_steps)
})

predictions = model.predict(future_time)

print("Future Predictions:", predictions)
plt.figure()

plt.plot(monthly_sales['Time'], y, label='Actual')
plt.plot(future_time['Time'], predictions, label='Forecast', linestyle='dashed')

plt.title("Sales Forecast")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.legend()

plt.show()
from sklearn.metrics import mean_absolute_error

y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)

print("MAE:", mae)
plt.figure()

# Actual
plt.plot(monthly_sales['Time'], y, label='Actual')

# Forecast (connect last actual point)
last_time = monthly_sales['Time'].iloc[-1]
last_value = y.iloc[-1]

plt.plot([last_time] + list(future_time['Time']),
         [last_value] + list(predictions),
         label='Forecast', linestyle='dashed')

plt.legend()
plt.title("Improved Sales Forecast")

plt.show()