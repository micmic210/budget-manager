"""
Budget Manager Application

This module provides functionalities for managing a budget,
including adding, viewing, editing, deleting, summarizing,
and exporting expenses.
"""


import datetime
import csv
from expense import Expense


def print_error_message(message):
    """Prints a title message in red."""
    print(f"\033[91m{message}\033[0m")


def print_title_message(message):
    """Prints a title message in green."""
    print(f"\033[92m{message}\033[0m")


def main():
    """
    Main function to run the budget manager application.
    """
    # Display welcome message
    print("\n" + "*" * 50)
    print("\n Welcome to Budget Manager!")
    budget = 2000  # Budget limit in Euro
    expenses = []  # List to store expenses

    # Display the main menu
    while True:
        print("\n" + "*" * 50)
        print("    Main Menu:")
        print("    1. Add a New Expense")
        print("    2. View Expenses")
        print("    3. Edit an Expense")
        print("    4. Delete an Expense")
        print("    5. Summarize Expenses")
        print("    6. Export Data to CSV")
        print("    7. Exit")
        print("\n" + "*" * 50)

        try:
            # Get user choice and call the corresponding function
            choice = int(input(" Please select an option (1 - 7): "))
            if choice == 1:
                print_title_message("\n Let's Add a New Expense!")
                expense = get_user_expense()
                if expense:
                    expenses.append(expense)
            elif choice == 2:
                print_title_message("\n Viewing Your Expenses")
                view_expenses(expenses)
            elif choice == 3:
                print_title_message("\n Editing an Expense")
                edit_expense(expenses)
            elif choice == 4:
                print_title_message("\n Deleting an Expense")
                delete_expense(expenses)
            elif choice == 5:
                print_title_message("\n Summarizing Your Expenses")
                summarize_expenses(expenses, budget)
            elif choice == 6:
                print_title_message("\n Exporting Data to CSV")
                export_to_csv(expenses)
            elif choice == 7:
                # Exit the program
                print("\n Thank you for using Budget Manager. Goodbye!")
                print("\n")
                break
            else:
                # Handle invalid choices
                print_error_message(
                    " Invalid choice. Please enter a number between "
                    "1 and 7."
                )
        except ValueError:
            # Handle invalid input (non-numeric)
            print_error_message(
                " Invalid input. Please enter a number."
            )


def get_user_expense():
    """
    Prompt the user to enter details for a new expense.
    Returns:
        Expense: The newly created expense object.
    """
    # Prompt user for expense details
    date_input = input(" Enter the date (YYYY-MM-DD): ").strip()
    try:
        # Convert the input date to a datetime object
        expense_date = datetime.datetime.strptime(
            date_input, "%Y-%m-%d"
        ).date()
    except ValueError:
        # Handle invalid date format
        print_error_message(
            " Invalid date format. Please enter a valid date in "
            " YYYY-MM-DD format."
        )
        return None

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
            print("\n Select a category for your expense: ")
            for i, category_name in enumerate(expense_categories):
                print(f"    {i + 1}. {category_name}")

            # Get the selected category index
            value_range = f" [1 - {len(expense_categories)}]"
            selected_index = int(
                input(f" Enter a category number {value_range}: ")
            ) - 1
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                break
            print_error_message(
                " Invalid category. Please try again."
            )
        except ValueError:
            # Handle invalid category selection input
            print_error_message(
                " Invalid input. Please enter a valid category number."
            )

    # Get the expense description
    description = input(" Enter the expense description: ").strip()
    if not description:
        # Handle empty description
        print_error_message(
            " Expense description cannot be empty. Please try again."
        )
        return None

    try:
        # Get the expense amount
        expense_amount = float(input(" Enter the expense amount (€): "))
        if expense_amount <= 0:
            # Handle invalid (negative) amount
            print_error_message(
                " Expense amount must be greater than zero. "
                " Please try again."
            )
            return None
    except ValueError:
        # Handle invalid amount input
        print_error_message(
            " Invalid input. Please enter a valid amount."
        )
        return None

    return Expense(
        expense_date,
        selected_category,
        description,
        expense_amount
    )


def view_expenses(expenses):
    """
    Displays the list of expenses.
    """
    if not expenses:
        # Handle case with no expenses
        print_error_message(" No expenses found.")
        return

    # Print each expense
    print("\n" + "-" * 50)
    for i, expense in enumerate(expenses):
        print(f" {i + 1}. {expense} ")
    print("-" * 50)


def edit_expense(expenses):
    """
    Prompt the user to select and edit an expense from the list
    """
    if not expenses:
        print_error_message(" No expenses to edit.")
        return

    # Display the expenses for selection
    print("\n Select an expense to edit: ")
    for i, expense in enumerate(expenses):
        print(f" {i + 1}. {expense}")

    try:
        # Get the index of the expense to edit
        index_to_edit = int(
            input("\n Enter the number of the expense to edit: ")
        ) - 1
        if 0 <= index_to_edit < len(expenses):
            new_expense = get_user_expense()
            if new_expense:
                expenses[index_to_edit] = new_expense
                print(" Expense edited successfully.")
        else:
            print_error_message(
                " Invalid number. Please try again."
            )
    except ValueError:
        print_error_message(
            " Invalid input. Please enter a valid number."
        )


def delete_expense(expenses):
    """
    Prompt the user to select and delete an expense from the list.
    """
    if not expenses:
        # Handle case with no expenses to delete
        print_error_message(" No expenses to delete.")
        return

    # Display the expenses for selection
    print("\n Select an expense to delete:")
    for i, expense in enumerate(expenses):
        print(f" {i + 1}. {expense}, ")

    try:
        # Get the index of the expense to delete
        index_to_delete = int(
            input("\n Enter the number of the expense to delete: ")
        ) - 1
        if 0 <= index_to_delete < len(expenses):
            expenses.pop(index_to_delete)
            print(" Expense deleted successfully.")
        else:
            print_error_message(" Invalid number. Please try again.")
    except ValueError:
        print_error_message(
            " Invalid input. Please enter a valid number."
            )


def summarize_expenses(expenses, budget):
    """
    Summarize expenses by category and display the total and remaining budget.
    """
    if not expenses:
        print_error_message(" No expenses found.")
        return

    # Calculate total amount by category
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
        print(f"\n Data exported successfully to {file_name}")
    except (IOError, OSError) as e:
        print_error_message(
            f"\n Failed to export data due to file error: {e}"
        )
    except csv.Error as e:
        print_error_message(
            f"\n Failed to export data due to value error: {e}"
        )


if __name__ == "__main__":
    main()
