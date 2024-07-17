"""
Budget Master application for managing expenses.
"""


import datetime
from expense import Expense


def main():
    """
    Main function to run the Budget Manager application. Provide a
    menu for the user to add, view, delete, and summarize expenses.
    """

    print("\n" + "-" * 50)
    print("\nWelcome to Budget Master!")
    budget = 2000  # Budget limit in Euro
    expenses = []  # List to store expenses

    while True:
        print("\n" + "-" * 50)
        print("Main Menu:")
        print("1. Add a New Expense")
        print("2. View Expenses")
        print("3. Delete an Expense")
        print("4. Summarize Expenses")
        print("5. Exit")
        print("\n" + "-" * 50)

        try:
            choice = int(input("Please select an option (1-5): "))
            if choice == 1:
                expense = get_user_expense()
                expenses.append(expense)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                delete_expense(expenses)
            elif choice == 4:
                summarize_expenses(expenses, budget)
            elif choice == 5:
                print("Thank you for using Budget Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_user_expense():
    """
    Prompt the user to enter details for a new expense.
    Returns expense of newly added.
    """

    print("Let's add a new expense!")
    date_input = input("Enter the date (DD-MM-YYYY): ").strip()
    try:
        expense_date = datetime.datetime.strptime(
            date_input, "%d-%m-%Y"
        ).date()
    except ValueError:
        print(
            "Invalid date format. Please enter a valid date in "
            "DD-MM-YYYY format."
        )
        return get_user_expense()

    expense_categories = [
        "Housing",
        "Utilities",
        "Groceries",
        "Transportation",
        "Entertainment",
        "Subscriptions",
        "Personal Hygiene",
        "Miscellaneous",
    ]

    while True:
        try:
            print("Select a category for your expense: ")
            for i, category_name in enumerate(expense_categories):
                print(f" {i + 1}. {category_name}")

            value_range = f"[1 - {len(expense_categories)}]"
            selected_index = (
                int(input(f"Enter a category number {value_range}: ")) - 1
            )

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                break
            print("Invalid category. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid category number.")

    description = input("Enter the expense description: ").strip()
    if not description:
        print("Expense description cannot be empty. Please try again.")
        return get_user_expense()

    try:
        expense_amount = float(input("Enter the expense amount (€): "))
        if expense_amount <= 0:
            print(
                "Expense amount must be greater than zero. "
                "Please try again."
            )
            return get_user_expense()
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return get_user_expense()

    new_expense = Expense(
        date=expense_date,
        category=selected_category,
        description=description,
        amount=expense_amount,
    )
    return new_expense


def view_expenses(expenses):
    """
    Displays the list of expenses.
    """
    print("Viewing expenses...")
    if not expenses:
        print("No expenses found.")
        return

    print("\n" + "-" * 50)
    for i, expense in enumerate(expenses):
        print(
            f"{i + 1}. {expense.date.strftime('%d-%m-%Y')}, "
            f"{expense.category}, {expense.description}, "
            f"€{expense.amount:.2f}"
        )
    print("-" * 50)


def delete_expense(expenses):
    """
    Prompt the user to select and delete an expense from the list.
    """
    if not expenses:
        print("No expenses to delete.")
        return expenses

    print("Select an expense to delete:")
    for i, expense in enumerate(expenses):
        print(
            f"{i + 1}. {expense.date.strftime('%d-%m-%Y')}, "
            f"{expense.category}, {expense.description}, "
            f"€{expense.amount:.2f}"
        )

    try:
        index_to_delete = (
            int(input("Enter the number of the expense to delete: ")) - 1
        )
        if 0 <= index_to_delete < len(expenses):
            expenses.pop(index_to_delete)
            print("Expense deleted successfully.")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return expenses


def summarize_expenses(expenses, budget):
    """
    Summarize expenses by category and display the total and remaining budget.
    """
    print("Summarizing your expenses...")
    if not expenses:
        print("No expenses found.")
        return

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("\nExpenses By Category:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: €{amount:.2f}")

    total_spent = sum(x.amount for x in expenses)
    print(f"\nTotal Spent: €{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Remaining Budget: €{remaining_budget:.2f}")


if __name__ == "__main__":
    main()
