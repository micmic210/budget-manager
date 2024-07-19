"""
Budget Manager application for managing expenses.
"""


import datetime
import csv
from expense import Expense


def main():
    """
    Main function to run the Budget Manager application. Provide a
    menu for the user to add, view, delete, edit, and summarize expenses
    as well as export data to CSV.
    """
    # Display welcome message
    print("\n" + "-" * 50)
    print("\n Welcome to Budget Manager!")
    budget = 2000  # Budget limit in Euro
    expenses = []  # List to store expenses

    # Display the main menu
    while True:
        print("\n" + "-" * 50)
        print("    Main Menu:")
        print("    1. Add a New Expense")
        print("    2. View Expenses")
        print("    3. Edit an Expense")
        print("    4. Delete an Expense")
        print("    5. Summarize Expenses")
        print("    6. Export Data to CSV")
        print("    7. Exit")
        print("\n" + "-" * 50)

        try:
            # Get user choice and call the corresponding function
            choice = int(input(" Please select an option (1-5): "))
            if choice == 1:
                expense = get_user_expense()
                expenses.append(expense)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                edit_expense(expenses)
            elif choice == 4:
                delete_expense(expenses)
            elif choice == 5:
                summarize_expenses(expenses, budget)
            elif choice == 6:
                export_to_csv(expenses)
            elif choice == 7:
                # Exit the program
                print(" Thank you for using Budget Manager. Goodbye!")
                break
            else:
                # Handle invalid choices
                print(" Invalid choice. Please enter a number between 1 "
                      "and 5.")
        except ValueError:
            # Handle invalid input (non-numeric)
            print(" Invalid input. Please enter a number.")


def get_user_expense():
    """
    Prompt the user to enter details for a new expense.
    Returns:
        Expense: The newly created expense object.
    """
    # Prompt user for expense details
    print(" Let's add a new expense!")
    date_input = input(" Enter the date (YYYY-MM-DD): ").strip()
    try:
        # Convert the input date to a datetime object
        expense_date = datetime.datetime.strptime(
            date_input, "%Y-%m-%d"
        ).date()
    except ValueError:
        # Handle invalid date format
        print(
            " Invalid date format. Please enter a valid date in "
            " YYYY-MM-DD format."
        )
        return get_user_expense()

    # List of expense categories
    expense_categories = [
        "Housing",
        "Utilities",
        "Groceries",
        "Entertainment",
        "Miscellaneous",
    ]

    # Display the categories for selection
    while True:
        try:
            print(" Select a category for your expense: ")
            for i, category_name in enumerate(expense_categories):
                print(f"    {i + 1}. {category_name}")

            # Get the selected category index
            value_range = f" [1 - {len(expense_categories)}]"
            selected_index = (
                int(input(f" Enter a category number {value_range}: ")) - 1
            )

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                break
            print(" Invalid category. Please try again.")
        except ValueError:
            # Handle invalid category selection input
            print(" Invalid input. Please enter a valid category number.")

    # Get the expense description
    description = input(" Enter the expense description: ").strip()
    if not description:
        # Handle empty description
        print(" Expense description cannot be empty. Please try again.")
        return get_user_expense()

    try:
        # Get the expense amount
        expense_amount = float(input(" Enter the expense amount (€): "))
        if expense_amount <= 0:
            # Handle invalid (negative) amount
            print(
                " Expense amount must be greater than zero. "
                " Please try again."
            )
            return get_user_expense()
    except ValueError:
        # Handle invalid amount input
        print(" Invalid input. Please enter a valid amount.")
        return get_user_expense()

    return Expense(
        expense_date,
        selected_category,
        description,
        expense_amount,
    )


def view_expenses(expenses):
    """
    Displays the list of expenses.
    """
    print(" Viewing expenses...")
    if not expenses:
        # Handle case with no expenses
        print(" No expenses found.")
        return

    # Print each expense
    print("\n" + "-" * 50)
    for i, expense in enumerate(expenses):
        print(
            f" {i + 1}. {expense}, "
        )
    print("-" * 50)


def edit_expense(expenses):
    """
    Prompt the user to select and edit an expense from the list
    """
    if not expenses:
        print(" No expenses to edit.")
        return expenses

    # Display the expenses for selection
    print(" Select an expense to edit: ")
    for i, expense in enumerate(expenses):
        print(f" {i + 1}. {expense}")

    try:
        # Get the index of the expense to edit
        index_to_edit = int(
            input("\n Enter the number of the expense to edit: ")
        ) - 1
        if 0 <= index_to_edit < len(expenses):
            expenses[index_to_edit] = get_user_expense()
            print(" Expense edited successfully.")
        else:
            print(" Invalid number. Please try again.")
    except ValueError:
        print(" Invalid input. Please enter a valid number.")


def delete_expense(expenses):
    """
    Prompt the user to select and delete an expense from the list.
    """
    if not expenses:
        # Handle case with no expenses to delete
        print(" No expenses to delete.")
        return expenses

    # Display the expenses for selection
    print(" Select an expense to delete:")
    for i, expense in enumerate(expenses):
        print(
            f" {i + 1}. {expense}, "
        )

    try:
        # Get the index of the expense to delete
        index_to_delete = int(
            input("\n Enter the number of the expense to delete: ")) - 1
        if 0 <= index_to_delete < len(expenses):
            expenses.pop(index_to_delete)
            print(" Expense deleted successfully.")
        else:
            print(" Invalid number. Please try again.")
    except ValueError:
        print(" Invalid input. Please enter a valid number.")
    return expenses


def summarize_expenses(expenses, budget):
    """
    Summarize expenses by category and display the total and remaining budget.
    """
    print(" Summarizing your expenses...")
    if not expenses:
        print(" No expenses found.")
        return expenses

    # Calculate total amount bycategory
    amount_by_category = {}
    for expense in expenses:
        if expense.category in amount_by_category:
            amount_by_category[expense.category] += expense.amount
        else:
            amount_by_category[expense.category] = expense.amount

    # Print expenses by category
    print("\n Expenses By Category:")
    for category, amount in amount_by_category.items():
        print(f"    {category}: €{amount:.2f}")

    # Calculate and display total spent and remaining budget
    total_spent = sum(expense.amount for expense in expenses)
    print(f"\n Total Spent: €{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f" Remaining Budget: €{remaining_budget:.2f}")


def export_to_csv(expenses):
    """
    Export expenses to a CSV file.
    """
    confirm = input(
        "Do you want to export the data to CSV? (yes/no): "
    ).strip().lower()
    if confirm == 'yes':
        file_name = "expense_summary.csv"
        try:
            # Open the CSV file for writing
            with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Date', 'Category', 'Description', 'Amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write the header and the data
                writer.writeheader()
                for expense in expenses:
                    writer.writerow({
                        'Date': expense.date.strftime('%Y-%m-%d'),
                        'Category': expense.category,
                        'Description': expense.description,
                        'Amount': expense.amount
                    })
            print(f" Data exported successfully to {file_name}")
        except (IOError, OSError) as e:
            print(f" Failed to export data due to file error: {e}")
        except ValueError as e:
            print(f" Failed to export data due to value error: {e}")
        except csv.Error as e:
            print(f" Failed to export data due to CSV error: {e}")
    else:
        print(" Export cancelled.")


if __name__ == "__main__":
    main()
