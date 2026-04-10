#logic for  running main file

def add_expense(expenses, amount, category):
    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)


def view_expenses(expenses):
    return expenses


def total_expense(expenses):
    return sum(exp["amount"] for exp in expenses)
