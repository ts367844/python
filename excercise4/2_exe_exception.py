# EMI Calculator with Exception Handling

def calculate_emi(principal, annual_rate, tenure_years):
    # Raise exception for negative values
    if principal <= 0:
        raise ValueError("Loan amount must be greater than 0.")
    if annual_rate <= 0:
        raise ValueError("Interest rate must be greater than 0.")
    if tenure_years <= 0:
        raise ValueError("Tenure must be greater than 0.")

    monthly_rate = annual_rate / (12 * 100)
    months = tenure_years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi


try:
    # Taking user input
    loan_amount = float(input("Enter Loan Amount: "))
    interest_rate = float(input("Enter Annual Interest Rate (%): "))
    tenure = float(input("Enter Tenure (in years): "))

    emi_value = calculate_emi(loan_amount, interest_rate, tenure)

    print(f"\nYour Monthly EMI is: ₹{emi_value:.2f}")

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Something went wrong:", e)