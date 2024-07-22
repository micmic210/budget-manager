# Budget Manager
![Budget Manager Header](/assets/images/home.png)

## Introduction

Welcome to Budget Manager, an easy-to-use application designed to help you manage and track your expenses efficiently. Whether you’re looking to keep an eye on your daily spending, set budget limits, or just need a better way to organize your finances, Budget Manager provides the tools you need to stay on top of your budget.


[You can find my Budget Manager App here!](https://budget-manager-ab4ecb0da2c1.herokuapp.com/)

## Contents 
  * [Introduction](#introduction)
  * [Design Blueprint](#design-blueprint)
  * [User Experience](#user-experience)
      * [User Stories](#user-stories)
      * [User Goals](#user-goals)
  * [Application Features](#application-features)
      * [Displaying Main Menu ](#1-main-menu-navigation)
      * [Adding a New Expense](#2-adding-a-new-expense)
      * [Viewing Expenses](#3-viewing-expenses)
      * [Editing Expense](#4-editing-expense)
      * [Deleting an Expense](#5-deleting-an-expense)
      * [Summarizing Expenses](#6-summarizing-expenses)
      * [Exporting Data to CSV](#7-exporting-data-to-csv)
      * [Handling User Input and Validation](#8-handling-user-input-and-validation)
      * [Expense Class](#9-expense-class)
  * [Future Features](#future-features)
  * [Technologies Used](#technologies-used)
  * [Deployment](#deployment)
  * [Testing](#testing)
  * [Credits](#credits)

## Design Blueprint

Below is the design blueprint of the Budget Manager application. This diagram outlines the main components and interactions within the system, providing a clear overview of the application's architecture.
![Budget Manager Design Blueprint](/assets/images/blue_print.png)

## User Experience

### User Stories

1. Log My Daily Expenses Easily
	* Story: As a user, I want to add my daily expenses quickly and easily, so I can keep track of where my money is going.
	* Acceptance Criteria: The application allows me to enter the date, select a category from a list, write a description, and specify the amount for each expense. The application prompts for re-entry in case of invalid input.

2. View My Expense History
	* Story: As a user, I want to view a list of all my expenses, so I can review my spending habits and ensure accuracy.
	* Acceptance Criteria: The application displays all logged expenses in a clear and organized manner, with each expense showing the date, category, description, and amount.

3.	Edit Incorrect or Outdated Expenses
	  * Story: As a user, I want to edit any expenses that were entered incorrectly or have changed, so my records remain accurate.
	  * Acceptance Criteria: The application allows me to select and edit any expense from the list, updating details such as date, category, description, and amount.

4. Delete Incorrect or Unnecessary Expenses
	  * Story: As a user, I want to delete any expenses that were entered incorrectly or are no longer relevant, so my records remain accurate.
	  * Acceptance Criteria: The application allows me to select and delete any expense from the list.

5. Summarize My Expenses by Category
	  * Story: As a user, I want to see a summary of my expenses categorized by type, so I can understand where I’m spending the most money.
	  * Acceptance Criteria: The application provides a summary of total spending per category and calculates the remaining budget.

6. Understand My Remaining Budget
	  * Story: As a user, I want to see how much of my budget remains, so I can manage my finances better.
	  * Acceptance Criteria: The application displays the total amount spent and the remaining budget after logging expenses, helping me to avoid overspending.

7. Navigate the Application Easily
	  * Story: As a user, I want a simple and intuitive menu to navigate through different options, so I can use the application efficiently.
	  * Acceptance Criteria: The application provides a clear main menu with options to add, view, edit, delete, summarize expenses, export data to CSV, and exit the program.

### User Goals

1. Efficient Expense Management
	* Goal: Enable users to efficiently log and manage their daily expenses.
	* Metric: The time taken to log an expense should be minimal, with a user-friendly input process that handles errors gracefully.

2. Clear Overview of Spending
	* Goal: Provide users with a clear and organized overview of their spending history.
	* Metric: Users should be able to view all expenses at a glance, categorized and detailed for easy review.

3. Accurate Records
	* Goal: Maintain accurate records by allowing users to edit or delete incorrect or unnecessary expense entries.
	* Metric: Users should be able to edit or delete expenses with minimal steps and without errors.

4. Insightful Expense Summaries
	* Goal: Offer insightful summaries that help users understand their spending patterns.
	* Metric: Summaries should break down expenses by category and provide totals that are easy to interpret.

5. Budget Awareness
	* Goal: Help users stay aware of their remaining budget to prevent overspending.
	* Metric: The remaining budget should be prominently displayed and updated in real-time as expenses are logged.

6. Intuitive Navigation
	* Goal: Ensure the application is easy to navigate for all users, regardless of technical skill.
	* Metric: Users should be able to navigate the main menu and access different functionalities without confusion.

## Application Features

### 1. Main Menu Navigation 
* Function: main()
	* Description: The main function serves as the entry point to the application. It displays a welcome message and a main menu with options to add, view, edit, delete, summarize expenses, export data to CSV, or exit the application.
	* Logic:
		* A while loop is used to keep the application running until the user chooses to exit.
		* The user is prompted to select an option from the menu, and the corresponding function is called based on the user’s input.

![Main Menu](/assets/images/menu.png)

### 2. Adding a New Expense
* Function: get_user_expense()
	* Description: Prompts the user to enter the details of a new expense, including the date, category, description, and amount. Validates the input and creates an Expense object.
	* Logic:
	    * The user is asked to enter the date of the expense, which is then parsed and validated.
	    * The user selects a category from a predefined list. The input is validated to ensure a valid category is chosen.
	    * The user provides a description and the amount for the expense. The amount is validated to ensure it is a positive number.
	    * An Expense object is created and returned.

![Add](/assets/images/add.png)

### 3. Viewing Expenses
* Function: view_expenses(expenses)
	* Description: Displays the list of all recorded expenses in a formatted manner.
	* Logic:
	    * Checks if there are any expenses to display.
	    * Iterates through the list of expenses and prints each one with its details (date, category, description, and amount).

![View](/assets/images/view.png)

### 4. Editing Expense
* Function: edit_expense(expenses)
	* Description: Allows the user to edit the details of an existing expense by selecting its number.
	* Logic:
	    * Checks if there are any expenses to edit.
	    * Displays the list of expenses and prompts the user to enter the number of the expense they wish to edit.
	    * Validates the input and allows the user to update the selected expense’s details.

![Edit](/assets/images/edit.png)

### 5. Deleting an Expense
* Function: delete_expense(expenses)
	* Description: Allows the user to delete an expense from the list by selecting its number.
	* Logic:
	    * Checks if there are any expenses to delete.
	    * Displays the list of expenses and prompts the user to enter the number of the expense they wish to delete.
	    * Validates the input and removes the selected expense from the list.

![Delete](/assets/images/delete.png)

### 6. Summarizing Expenses
* Function: summarize_expenses(expenses, budget)
* Description: Provides a summary of expenses by category and displays the total spending and remaining budget.
	* Logic:
	    * Checks if there are any expenses to summarize.
	    * Uses a dictionary to calculate the total amount spent per category.
	    * Prints the total amount spent in each category.
	    * Calculates the total amount spent and the remaining budget, then displays these values.

![Summarize](/assets/images/summarize.png)

### 7. Exporting Data to CSV
* Function: export_to_csv(expenses)
	* Description: Exports the list of expenses to a CSV file for record-keeping or further analysis.
	* Logic:
	    * Prompts the user to confirm the export action.
	    * Opens a CSV file for writing, using UTF-8 encoding.
	    * Writes the headers and expense data to the CSV file.
	    * Handles any file I/O errors gracefully.

![Export-yes](/assets/images/export-yes.png)
![Export-no](/assets/images/export-no.png)

### 8. Handling User Input and Validation
* Description: Throughout the application, user inputs are validated to ensure correctness and robustness.
	* Logic:
	    * Date inputs are validated using datetime.strptime.
	    * Category selection is validated by checking if the selected index is within the range of available categories.
	    * Description inputs are checked to ensure they are not empty.
	    * Amount inputs are validated to ensure they are positive numbers.

### 9. Expense Class
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

1. Income Tracking
    * Description: Enable users to log their income and calculate the net 
      balance after expenses.
    * Implementation: Add a new section for income entries, similar to 
      expenses, and adjust the budget summary to include income. 

2. Recurring Expenses
    * Description: Allow users to set up recurring expenses that are automatically
      added to their expenses at specified intervals. 
    * Implementation: Implement a scheduling system to automatically log 
      recurring expenses. 


## Technologies Used
### Python

## Deployment

1. Log in to Heroku
    * Ensure you have a Heroku account and are logged in.

2. Navigate to the Dashboard and click "New".
    * In the top right corner of the Heroku Dashboard, click the “New” button.

3. From the "New", select "Create new app".
    * Click on “Create new app” from the dropdown menu.

4. Enter an app name and choose a region, and click "Create app". 
    * Provide a unique app name and select the appropriate region (United States or Europe), then click “Create app”.

5. Under "Deployment method", select "GitHub".
    * In the app dashboard, navigate to the “Deploy” tab.
	* Under “Deployment method”, choose “GitHub”.

6. Search for your repository, connect to GitHub and click "Connect".
	* Authorize Heroku to access your GitHub account if prompted.
	* Search for your GitHub repository and click “Connect”.

7. Navigate to "Settings" and click "Add buildpack". 
	* Go to the “Settings” tab.
	* Scroll down to the “Buildpacks” section and click “Add buildpack”.

8. Select "Python" and click "Add buildpack". 
	* Choose “Python” from the list and click “Save changes”.

9. Return to "Deploy" and go to "Manual deploy". 
    * Go back to the “Deploy” tab.
	* In the “Manual deploy” section, select the branch you want to deploy.

10. Select a branch to deploy and click "Deploy Branch".
	* Choose the branch you want to deploy (e.g., main, master) and click “Deploy Branch”.

11. A message will display: "Your app was successfully deployed".
	* After the deployment process completes, you should see a success message.

12. Click the "View" button or "Open app" to check if it's deployed. 
	* Click “View” or “Open app” to access your deployed application.
    Here's the link: [micmic210/budget-manager](https://budget-manager-ab4ecb0da2c1.herokuapp.com/)

13. Clone the repository
	* You can clone your repository using the provided command:
    ```bash
       git clone https://github.com/micmic210/budget-manager.git 
    ```

## Testing 

### Tools Used
1. Pycodestyle: Checks Python code against the PEP 8 style guide to ensure consistency and readability.

2.	Flake8: Combines Pycodestyle, pyflakes, and mccabe to check code style, detect errors, and measure complexity, ensuring a clean and manageable codebase.

3.	Pylint: A static code analysis tool that catches errors, enforces coding standards, and suggests refactoring to maintain high code quality.

### Steps to Perform Testing
1. Set up a virtual environment: 
    ```
    python -m venv env
    ```
2. Activate the virtual environment: 
    ```
    source env/bin/activate
    ```
3. Install the required tools: 
    ```
    pip install pycodestyle flake8 pylint
    ```
4. Run the code style and linting tools: 
   ```
   pycodestyle run.py
   flake8 run.py
   pylint run.py
   ```
5. Review and correct errors based on the messages provided by these tools.

## Credits

### External Resources

1. [Python.org](https://docs.python.org/3/) - Python Documentation. 
2. [Python.org](https://docs.python.org/3/tutorial/index.html) - Python Tutorials. 
3. [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - ask questions and find solutions. 
4. Tutorials from [pixegami](http://www.youtube.com/@pixegami).
5. Tutorials from [Tech With Tim](www.youtube.com/@TechWithTim).


### Acknowledgements

I would like to thank the following people and organizations for their support and contributions:

1. Mr.Jubril Akolade for his invaluable guidance and feedback throughout the development of this project.

2. My family and friends for their patience and encouragement during long coding sessions.



