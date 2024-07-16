# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from expense import Expense
import datetime 

def main():
    """
    Main function to run the Budget Manager application. Provide a menu
    for the user to add, view, delete, and summarize expenses. 
    """

    print("\n" + "-"*50)
    print("\nWelcome to Budget Manager!")
    expense_file_path = "expense.csv" # Path to the CSV file storing expenses
    budget = 2000 # Budget limit in Euro

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
            choice = int(input ("Please select an option (1-5): "))
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
                print("Invalid choice. Plaese enter a number between 1 and 5.")
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
        


if __name__ == "__main__":
    main()