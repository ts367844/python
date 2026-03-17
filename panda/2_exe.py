import pandas as pd

# Read data from CSV file
df = pd.read_csv("students.csv")

# Display first 3 rows
print("First 3 Records:")
print(df.head(3))

# Display basic information
print("\nData Info:")
print(df.info())

# Find maximum marks
max_marks = df["Marks"].max()
print("\nMaximum Marks:", max_marks)

# Add a new column (Result)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")

# Display updated data
print("\nUpdated Data:")
print(df)