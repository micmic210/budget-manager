# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from expense import Expense
import datetime 
import csv

def main():
    """
    Main function to run the Budget Manager application. Provide a menu
    for the user to add, view, delete, and summarize expenses. 
    """

    print("\n" + "-"*50)
    print("\nWelcome to Budget Manager!")
    expense_file_path = "expense.csv"  # Path to the CSV file storing expenses
    budget = 2000  # Budget limit in Euro

    while True: 
        print("\n" + "-"*50)
        print("Main Menu:")
        print("1. Add a New Expense")
        print("2. View Expenses")
        print("3. Delete an Expense")
        print("4. Summarize Expenses")
        print("5. Exit")
        print("\n" + "-"*50)

        try:
            choice = int(input("Please select an option (1-5): "))
            if choice == 1: 
                expense = get_user_expense()
                save_expense_to_file(expense, expense_file_path)
            elif choice == 2:
                view_expenses(expense_file_path)
            elif choice == 3:
                delete_expense(expense_file_path)
            elif choice == 4:
                summarize_expenses(expense_file_path, budget)
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
        expense_date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
    except ValueError:
        print("Invalid date format. Please enter a valid date in DD-MM-YYYY format.")
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
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                break
            else: 
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
            print("Expense amount must be greater than zero. Please try again.")
            return get_user_expense()
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return get_user_expense()
    
    new_expense = Expense(
        date=expense_date, category=selected_category, description=description,
        amount=expense_amount
    )
    return new_expense   

def save_expense_to_file(expense: Expense, expense_file_path):
    """
    Save the input expense to a CSV file.
    """
    print("Saving your expense...")
    try: 
        with open(expense_file_path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([expense.date.strftime('%d-%m-%Y'), expense.category, expense.description, f"{expense.amount:.2f}"])
        print("Expense saved successfully!")
    except IOError as e:
        print(f"Error saving expense: {e}")

def view_expenses(expense_file_path):
    """
    Read expenses from a CSV file and displays them.
    """
    print("Viewing expenses...")
    expenses = read_expenses_from_file(expense_file_path)
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n" + "-"*50)
    for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense.date.strftime('%d-%m-%Y')}, {expense.category}, {expense.description}, €{expense.amount:.2f}")
    print("-" * 50)

def delete_expense(expense_file_path):
    """
    Prompt the user to select and delete an expense from the CSV file.
    """
    expenses = read_expenses_from_file(expense_file_path)
    if not expenses:
        print("No expenses to delete.")
        return

    print("Select an expense to delete:")
    for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense.date.strftime('%d-%m-%Y')}, {expense.category}, {expense.description}, €{expense.amount:.2f}")
    
    try:
        index_to_delete = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index_to_delete < len(expenses):
            expenses.pop(index_to_delete)
            write_expenses_to_file(expenses, expense_file_path)
            print("Expense deleted successfully.")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def summarize_expenses(expense_file_path, budget):
    """
    Summarize expenses by category and display the total and remaining budget.
    """
    print("Summarizing your expenses...")
    expenses = read_expenses_from_file(expense_file_path)
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

    total_spent = sum([x.amount for x in expenses])
    print(f"\nTotal Spent: €{total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Remaining Budget: €{remaining_budget:.2f}")


def read_expenses_from_file(expense_file_path):
    """
    Read expenses from a CSV file and return them as a list of Expense objects.
    """
    expenses = []
    try: 
        with open(expense_file_path, "r", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # Add this to avoid processing empty lines
                    date, category, description, expense_amount = row
                    expense = Expense(
                        date=datetime.datetime.strptime(date, "%d-%m-%Y").date(),
                        category=category,
                        description=description,
                        amount=float(expense_amount),
                    )
                    expenses.append(expense)
    except IOError as e:
        print(f"Error reading expenses: {e}")
    return expenses

def write_expenses_to_file(expenses, expense_file_path):
    """
    Write a list of expenses to a CSV file.
    """
    try: 
        with open(expense_file_path, "w", newline='') as f:
            writer = csv.writer(f)
            for expense in expenses:
                writer.writerow([expense.date.strftime('%d-%m-%Y'), expense.category, expense.description, f"{expense.amount:.2f}"])
        print("Expenses saved successfully.")
    except IOError as e:
        print(f"Error writing expenses: {e}")

if __name__ == "__main__":
    main()