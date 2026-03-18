import pandas as pd

# Step 1: Create Data
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya", "Kiran"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [50000, 40000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

# Step 2: Display Data
print("Employee Data:")
print(df)

# Step 3: Group By Department
grouped = df.groupby("Department")

# Step 4: Calculate Average Salary
print("\nAverage Salary by Department:")
print(grouped["Salary"].mean())

# Step 5: Find Total Salary
print("\nTotal Salary by Department:")
print(grouped["Salary"].sum())

# Step 6: Count Employees in each Department
print("\nEmployee Count by Department:")
print(grouped["Name"].count())