import pandas as pd

# Load CSV file
data = pd.read_csv("transactions.csv")

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Create Day column
data['Day'] = data['Date'].dt.day_name()

# Create Category column
data['Category'] = "Other"

# Categorize using keywords
data.loc[data['Description'].str.contains("Starbucks|Netflix|Amazon", case=False), 'Category'] = "Luxury"
data.loc[data['Description'].str.contains("Grocery", case=False), 'Category'] = "Food"
data.loc[data['Description'].str.contains("Uber", case=False), 'Category'] = "Transport"
data.loc[data['Description'].str.contains("Electricity", case=False), 'Category'] = "Bills"
data.loc[data['Description'].str.contains("Salary", case=False), 'Category'] = "Income"

# Show categorized data
print("\nTransaction Data:")
print(data)

# Monthly spending per category
category_spending = data.groupby("Category")["Amount"].sum()

print("\nTotal Spending Per Category:")
print(category_spending)

# Spending per day of week
day_spending = data.groupby("Day")["Amount"].sum()

print("\nSpending Per Day:")
print(day_spending)

# Day with highest spending
highest_spending_day = day_spending.idxmin()

print("\nDay you spend the most money:", highest_spending_day)