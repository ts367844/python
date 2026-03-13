# Grade Classification Program using Conditional Statements

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 35:
    print("Grade: Pass")
else:
    print("Grade: Fail")

print("Result evaluation completed.")