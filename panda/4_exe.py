import pandas as pd
import numpy as np

# Step 1: Create Data with Missing Values
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya", "Kiran"],
    "Age": [20, 21, None, 22, None],
    "Marks": [85, None, 78, 88, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Check Missing Values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Step 3: Fill Missing Values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(0, inplace=True)

# Step 4: Drop rows if still missing (optional)
df_cleaned = df.dropna()

# Step 5: Display Clean Data
print("\nCleaned Data:")
print(df_cleaned)