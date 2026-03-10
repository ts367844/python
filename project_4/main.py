import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
description TEXT,
amount REAL,
category TEXT
)
""")

while True:

    print("\n------ Expense Manager ------")
    print("1 Add Expense")
    print("2 Search Expense")
    print("3 Delete Expense")
    print("4 View All Expenses")
    print("5 Monthly Report (Graph)")
    print("6 Exit")

    choice = input("Enter your choice: ")

    # 1 ADD EXPENSE
    if choice == "1":

        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        if "uber" in description.lower():
            category = "Transport"
        elif "netflix" in description.lower():
            category = "Entertainment"
        elif "grocery" in description.lower():
            category = "Food"
        else:
            category = "Other"

        cursor.execute(
        "INSERT INTO expenses(date, description, amount, category) VALUES(?,?,?,?)",
        (date, description, amount, category)
        )

        conn.commit()
        print("Transaction saved!")

    # 2 SEARCH EXPENSE
    elif choice == "2":

        keyword = input("Enter description to search: ")

        cursor.execute(
        "SELECT * FROM expenses WHERE description LIKE ?",
        ('%' + keyword + '%',)
        )

        results = cursor.fetchall()

        if results:
            print("\nSearch Results")
            for row in results:
                print(row)
        else:
            print("No record found")

    # 3 DELETE EXPENSE
    elif choice == "3":

        expense_id = input("Enter Expense ID to delete: ")

        cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Expense deleted")
        else:
            print("Expense not found")

    # 4 VIEW ALL EXPENSES
    elif choice == "4":

        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()

        print("\nAll Expenses\n")
        print("ID | Date | Description | Amount | Category")

        for row in rows:
            print(row)

    # 5 MONTHLY REPORT
    elif choice == "5":

        df = pd.read_sql_query("SELECT * FROM expenses", conn)

        df['date'] = pd.to_datetime(df['date'])

        monthly = df.groupby(df['date'].dt.month)['amount'].sum()

        print("\nMonthly Spending")
        print(monthly)

        monthly.plot(kind="bar", title="Monthly Expense Report")

        plt.xlabel("Month")
        plt.ylabel("Total Expense")

        plt.show()

    # 6 EXIT
    elif choice == "6":
        break

    else:
        print("Invalid Choice")

conn.close()
print("Program Closed")