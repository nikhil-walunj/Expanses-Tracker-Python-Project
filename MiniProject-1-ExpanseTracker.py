
from datetime import datetime

# Here we store expenses using empty list
expenses = []

# Welcome Message
print("\nWelcome to the Expense Tracker!!")

while True:
    print("\nOptions:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Categorized Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add expense
        while True:
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                expense_date = datetime.strptime(date, "%Y-%m-%d")
                current_date = datetime.now()

                # Check if the date is within the current month
                if expense_date.year == current_date.year and expense_date.month == current_date.month:
                    break
                else:
                    print("Error: Date must be within the current month. Please try again.")
            except ValueError:
                print("Error: Invalid date format. Please use YYYY-MM-DD.")

        description = input("Enter a description: ")
        category = input("Enter category (e.g., Food, Transport, etc.): ")
        amount = input("Enter the amount: ₹ ")

        expenses.append((date, description, category, float(amount)))
        print("Expense added successfully.")

    elif choice == "2":
        # View expenses
        print("\nExpenses:")
        if expenses:
            for expense in expenses:
                expense_str = f"{expense[0]}, {expense[1]}, {expense[2]}, {expense[3]}"
                print(expense_str)
        else:
            print("No expenses found. Add some first!")

    elif choice == "3":
        # Total expenses
        total = 0
        if expenses:
            for expense in expenses:
                total += expense[3]
            print(f"Total Expenses: ₹{total}")
        else:
            print("No expenses found. Add some first!")

    elif choice == "4":
        # Categorized Summary
        categories = {}
        if expenses:
            for expense in expenses:
                category = expense[2]
                amount = expense[3]
                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount
            print("\nExpenses by Category:")
            for category, total in categories.items():
                print(f"{category}: ₹{total}")
        else:
            print("No expenses found. Add some first!")

    elif choice == "5":
        # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


#OUTPUT:
'''
Welcome to the Expense Tracker!!

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 1
Enter the date (YYYY-MM-DD): 2024-12-14
Enter a description: Pay for Vada Pav
Enter category (e.g., Food, Transport, etc.): Food
Enter the amount: ₹ 20
Expense added successfully.

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 1
Enter the date (YYYY-MM-DD): 2024-01-14
Error: Date must be within the current month. Please try again.
Enter the date (YYYY-MM-DD): 2024-12-27 
Enter a description: Pay for Cloth
Enter category (e.g., Food, Transport, etc.): Shopping
Enter the amount: ₹ 1000
Expense added successfully.

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 2

Expenses:
2024-12-14, Pay for Vada Pav, Food, 20.0
2024-12-27, Pay for Cloth, Shopping, 1000.0

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 3
Total Expenses: ₹1020.0

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 1
Enter the date (YYYY-MM-DD): 2024-12-17
Enter a description: Pay for hotel bill
Enter category (e.g., Food, Transport, etc.): Food
Enter the amount: ₹ 3747
Expense added successfully.

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 2

Expenses:
2024-12-14, Pay for Vada Pav, Food, 20.0
2024-12-27, Pay for Cloth, Shopping, 1000.0
2024-12-17, Pay for hotel bill, Food, 3747.0

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 3
Total Expenses: ₹4767.0

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 4

Expenses by Category:
Food: ₹3767.0
Shopping: ₹1000.0

Options:
1. Add Expense
2. View Expenses
3. Total Expenses
4. Categorized Summary
5. Exit
Enter your choice (1-5): 5
Goodbye!

'''
