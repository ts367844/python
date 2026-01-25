''' 
    write a program to calculate & display gross annual income, tax and net income from  given monthly income as per below income tax rule 
    ---------------------------------------------------------------------------------
    annual income                           Tax Rate
    Above Rs. 24,00,000                     30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,000 to Rs. 16,00,000	    15%
    below 12,00,000                          0%

    steps 
    1) accept monthly income 
    2) calculate annual income 
    3) calculate tax as per rule
    4) calculate net income using gross annual income and tax 
    5) display gross income, tax, net income
''' 
m_income = float(input("Enter monthly income :"))
g_income = m_income * 12 
tax = None
if g_income<1200000:
    tax = 0
elif g_income>=1200000 and g_income<=1600000:
    tax = g_income * 0.15
elif g_income>=1600000 and g_income<=2000000:
    tax = g_income * 0.20
elif g_income>=2000000 and g_income<=2400000:
    tax = g_income * 0.25
else:
    tax = g_income * 0.30

n_income = g_income - tax
print(f"Gross Income = {g_income} ,tax = {tax} ,net income = {n_income}")
