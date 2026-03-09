import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("weather_data.csv")

# Convert Date column into datetime
data['Date'] = pd.to_datetime(data['Date'])

# Set date as index
data.set_index('Date', inplace=True)

# Handle missing values
data['Temperature'] = data['Temperature'].fillna(data['Temperature'].mean())

# Resample daily data into yearly average
yearly_temp = data['Temperature'].resample('YE').mean()

# Calculate Moving Average (5 year)
moving_avg = yearly_temp.rolling(window=5).mean()

# Display results
print("\nYearly Average Temperature:")
print(yearly_temp)

print("\n5-Year Moving Average Temperature:")
print(moving_avg)

# Plot graph
plt.figure(figsize=(10,5))

plt.plot(yearly_temp, label="Yearly Average Temperature")
plt.plot(moving_avg, label="5 Year Moving Average")

plt.title("Temperature Trend Over 20 Years")
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.legend()

plt.show()