# Budget Manager
link !!!

## Introduction 

Welcome to Budget Manager, an easy-to-use application designed to help you manage and track your expenses
efficiently. Whether you're looking to keep an eye on your daily spending, set budget limits, or just need 
a better way to organize your finances, Budget Manger provides the tools you need to stay on top of your
budget. 

## Contents 
### [Introduction](#introduction)
### [User Experience](#user-experience)
#### [User Stories](#user-stories)
#### [User Goals](#user-goals)
### [Application Features](#application-features)
### [Future Features](#future-features)
### [Technologies Used](#technologies-used)
### [Deployment](#deployment)
### [Testing](#testing)
### [Credits](#credits)



## User Experience

### User Stories

1. Log My Daily Expenses Easily
    * Story: As a user, I want to add my daily expenses quickly and easily, so I can
      keep track of where my money is going.
    * Acceptance Criteria: The application allows me to enter the date, select a 
      category, write a description, and specify the amount for each expense.
2. View My Expense History
    * Story: As a user, I want to view a list of all my expenses, so I can review my 
      spending habits and ensure accuracy. 
    * Acceptance Criteria: The application displays all logged expenses in a clear
      and organized manner.
3. Delete Incorrect or Unnecessary Expenses
    * Story: As a user, I want to delete any expenses that were entered incorrectly 
      or are no longer relevant, so my records remain accurate. 
    * Acceptance Criteria: The application allows me to select and delete any 
      expense from the list. 
4. Summarize My Expenses by Category
    * Story: As a user, I want to see a summary of my expenses categorized by type, 
      so I can understand where I'm spending the most money.
    * Acceptance Criteria: The application provides a summary of total spending per
      category and calculates the remaining budget. 
5. Understand My Remaining Budget
    * Story: As a user, I want to see how much of my budget remains, so I can manage
      my finances better.
    * Acceptance Criteria: The application displays the total amount spent and the
      remaining budget after logging expenses.
6. Navigate the Application Easily
    * Story: As a user, I want a simple and intuitive menu to navigate through 
      different options, so I can use the application efficiently. 
    * Acceptance Criteria: The application provides a clear main menu with options
      to add, view, delete and summarize expenses, as well as to exit the program. 

### User Goals

1. Efficient Expense Management
    * Goal: Enable user to efficiently log and manage their daily expenses.
    * Metric: Time taken to log an expense should be minimal, with a user-friendly
      input process.
2. Clear Overview of Spending
    * Goal: Provide users with a clear and organized overview of their spending 
      history.
    * Metric: Users should be able to view all expenses at a glance, categorized and 
      detailed for easy review. 
3. Accurate Records
    * Goal: Maintain accurate records by allowing users to delete incorrect or 
      unnecessary expense entries.
    * Metric: Users should be able to delete expenses with minimal steps and 
      without errors. 
4. Insightful Expense Summaries
    * Goal: Offer insightful summaries that help users understand their spending
      patterns.
    * Metric: Summaries should break down expenses by category and provide totals
      that are easy to interpret. 
5. Budget Awareness
    * Goal: Help users stay aware of their remaining budget to prevent overspending.
    * Metric: The remaining budget should be prominently displayed and updated in 
      real-time as expenses are logged. 
6. Intuitive Navigation
    * Goal: Ensure the application is easy to navigate for all users, regardless 
      of technical skill. 
    * Metric: Users should be able to navigate the main menu and access different
      functionalities without confusion. 

## Application Features

1. Main Menu Navigation
    * Function: main()
    * Description: The main function serves as the entry point to the application. 
      It displays a welcome message and a main menu with options to add, view, 
      delete, summarize expenses, or exit the application. 
    * Logic: 
        * A while loop is used to keep the application running until the user
          chooses to exit. 
        * The user is prompted to select an option from the menu, and the 
          corresponding function is called based on the user's input. 

2. Adding a New Expense
    * Function: get_user_expense()
    * Description: Prompts the user to enter the details of a new expense, including 
      the date, category, description, and amount. Validates the input and creates an Expense object.
    * Logic: 
        * The user is asked to enter the date of the expense, which is then parsed
          and validated.
        * The user selects a category from a predefined list. The input is validated
          to ensure a valid category is chosen. 
        * The user provides a description and the amount for the expense. The amount
          is validated to ensure it is a positive number. 
        * An expense object is created and returned. 

3. Viewing Expenses
    * Function: view_expenses(expenses)
    * Description: Displays the list of all recorded expenses in a formatted manner. 
    * Logic: 
        * Checks if there are any expenses to display.
        * Iterates through the list of expenses and prints each one with its details
          (date, category, description, and amount).

4. Deleting an Expense
    * Function: delete_expense(expenses)
    * Description: Allows the user to delete an expense from the list by selecting 
      its number.
    * Logic:
        * Checks if there are any expenses to delete.
        * Displays the list of expenses and prompts the user to enter the number 
          of the expense they wish to delete.
        * Validates the input and removes the selected expense from the list.

5. Summarizing Expenses
    * Function: summarize_expenses(expenses, budget)
    * Description: Provides a summary of expenses by category and displays the 
      total spending and remaining budget.
    * Logic
        * Checks if there are any expenses to summarize.
        * Uses a dictionary to calculate the total amount spent per category.
        * Prints the total amount spent in each category.
        * Calculates the total amount spent and the remaining budget, then displays 
          these values. 

6. Handling User Input and Validation
    * Description: Throughout the application, user inputs are validated to ensure
      correctness and robustness. 
    * Logic:
        * Date inputs are validated using datetime.strptime. 
        * Category selection is validated by checking if the selected index is 
          within the range of available categories. 
        * Description inputs are checked to ensure they are not empty. 
        * Amount inputs are validated to ensure they are positive numbers. 

7. Expense Class
    * Module: Expense
    * Class: Expense
    * Description: Represents an expense with attributes for date, category, 
      description, and amount.
    * Attributes:
        * date: The date of the expense.
        * category: The category of the expense (ex. Housing, Utilities).
        * description: A brief description of the expense.
        * amount: The amount spent in Euro. 

## Future Features

1. Expense Editing
    * Description: Allow users to edit existing expenses to correct mistakes 
      or update information. 
    * Implementation: Add a new menu option and corresponding function to 
      select and edit expense details. 

2. Income Tracking
    * Description: Enable users to log their income and calculate the net 
      balance after expenses.
    * Implementation: Add a new section for income entries, similar to 
      expenses, and adjust the budget summary to include income. 

3. Recurring Expenses
    * Description: Allow users to set up recurring expenses that are automatically
      added to their expenses at specified intervals. 
    * Implementation: Implement a scheduling system to automatically log 
      recurring expenses. 

4. Data Export and Import
    * Description: Enable users to export their expense data to CSV, Excel, or 
      PDF formats and import data from these formats. 
    * Implementation: Implement functions to read from and write to these file
      formats using libraries.

## Technologies Used
    ### Python

## Deployment

1. Log in to Heroku
2. Navigate to the Dashboard and click "New".
3. From the "New", select "Create new app".
4. Enter an app name and choose a region, and click "Create app". 
5. Under "Deployment method", select "GitHub".
6. Search for your repository, connect to GitHub and click "Connect".
7. Navigate to "Settings" and click "Add buildpack". 
8. Select "Python" and click "Add buildpack". 
9. Return to "Deploy" and go to "Manual deploy". 
10. Select a branch to deploy and click "Deploy Branch".
11. A message will display: "Your app was successfully deployed".
12. Click the "View" button to check if it's deployed.    

## Testing 

### Tools Used
1. Pycodestyle
2. Flake8
3. Pyling 

### Steps to Perform Testing
1. Set up a virtual environment: python -m venv env 
2. Activate the virtual environment: source env/bin/activate
3. Install the required tools: pip install pycodestyle flake8 pyling
4. Run the code style and linting tools: 
   pycodestyle run.py
   flake8 run.py
   pylint run.py 
5. Review and correct errors based on the messages provided by these tools.

## Credits
### Content References
### External Resources
### Acknowledgements



