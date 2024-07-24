# Budget Manager
![Budget Manager Header](/assets/images/home.png)

## Introduction

The Budget Manager Application is a comprehensive tool designed to help users effectively manage their personal finances. This application provides a range of functionalities that allow users to record, track, and analyze their expenses. With a focus on simplicity and user-friendliness, the Budget Manager ensures that even users with minimal technical expertise can efficiently manage their budgets and stay on top of their financial health. By offering features such as expense tracking, budget summarization, and data export, the application serves as a reliable assistant for anyone looking to gain better control over their spending habits.


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
The Budget Manager Application is designed with a user-friendly interface, ensuring ease of navigation and interaction. Users are greeted with clear and color-coded messages that guide them through various functionalities. The application uses a simple main menu to access different features, providing straightforward prompts and error messages to help users manage their expenses effectively.

### User Stories

1. As a user, I want to add new expenses so that I can keep track of my spending.
	* Scenario: The user selects the option to add a new expense, inputs the date, category, description, and amount, and the expense is saved successfully.

2. As a user, I want to view all my recorded expenses so that I can review my spending habits.
	* Scenario: The user selects the option to view expenses, and a list of all recorded expenses is displayed in an organized manner.

3.	As a user, I want to edit an existing expense so that I can correct any mistakes or update the details.
	* Scenario: The user selects the option to edit an expense, chooses the specific expense to update, modifies the details, and the changes are saved successfully.

4.	As a user, I want to delete an expense so that I can remove any incorrect or unnecessary records.
	* Scenario: The user selects the option to delete an expense, confirms the deletion, and the expense is removed from the records.

5.	As a user, I want to see a summary of my expenses categorized by type so that I can understand where my money is going.
	* Scenario: The user selects the option to summarize expenses, and a categorized summary is displayed showing the total spent in each category and the remaining budget.

6.	As a user, I want to export my expenses to a CSV file so that I can analyze my data in other applications or keep a backup.
	* Scenario: The user selects the option to export data, and the expenses are successfully saved to a CSV file.

### User Goals

1. Track Expenses: Users can add, view, edit, and delete their expenses to maintain an accurate and comprehensive record of their spending.

2.	Stay Within Budget: The application helps users monitor their spending against a predefined budget, providing alerts when they approach their limit.

3.	Analyze Spending: Users can generate summaries of their expenses by category, allowing them to identify spending patterns and areas for potential savings.

4.	Export Data: Users can export their expense data to a CSV file, facilitating further analysis in spreadsheet programs or sharing with others.

5.	Maintain Accurate Records: Users have the tools to correct or remove any erroneous entries, ensuring that their expense records are precise and reliable.

6.	User-Friendly Interaction: The application offers an intuitive interface with clear prompts and feedback, making it accessible to users of all technical skill levels.

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
    python3 -m venv env
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



