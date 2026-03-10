import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("expenses.db")

# Load data into pandas
data = pd.read_sql_query("SELECT * FROM expenses", conn)

# Convert date
data['date'] = pd.to_datetime(data['date'])

# Monthly spending
monthly = data.groupby(data['date'].dt.month)['amount'].sum()

print("Monthly Spending")
print(monthly)

# Category spending
category = data.groupby('category')['amount'].sum()

print("\nCategory Spending")
print(category)

# Graph
category.plot(kind='bar', title="Expense by Category")

plt.show()

conn.close()