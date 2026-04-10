#main functioning inputs and outputs    

print("RUNNING FILE")
from expense_manager import add_expense, view_expenses, total_expense
from storage import load_expenses, save_expenses

expenses = load_expenses()

while True:
    print("\n1. Add 2. View 3. Total 4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        add_expense(expenses, amount, category)
        save_expenses(expenses)

    elif choice == "2":
        all_expenses = view_expenses(expenses)
        if not all_expenses:
            print("No expenses recorded.")
        else:
            for exp in all_expenses:
                print(exp)

    elif choice == "3":
        total = total_expense(expenses)
        print("Total:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
while True:
    print("LOOP WORKING")
    break