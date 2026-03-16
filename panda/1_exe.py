import pandas as pd

# Create a dictionary of data
data = {
    "Name": ["Rahul", "Amit", "Sneha", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 88]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Student Data:")
print(df)

# Calculate average marks
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Filter students with marks greater than 80
high_scorers = df[df["Marks"] > 80]
print("\nStudents with Marks > 80:")
print(high_scorers)