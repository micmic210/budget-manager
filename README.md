# Budget Manager
![Budget Manager Header](/assets/images/mock.png)

## Introduction

The Budget Manager Application helps users manage their personal finances effectively. It offers functionalities to record, track, and analyze expenses, focusing on simplicity and user-friendliness. Features include expense tracking, budget summarization, and data export, making it a reliable tool for better control over spending habits.


[You can find my Budget Manager App here!](https://budget-manager-ab4ecb0da2c1.herokuapp.com/)

## Contents 
  * [Introduction](#introduction)
  * [System Design](#system-design)
      * [Simple Flowchart](#simple-flowchart)
      * [Detailed Flowchart](#detailed-flowchart)
  * [User Experience](#user-experience)
      * [User Stories](#user-stories)
      * [User Goals](#user-goals)
  * [Application Features](#application-features)
      * [Displaying Main Menu ](#1-main-menu-navigation)
      * [Adding a New Expense](#2-adding-a-new-expense)
      * [Viewing Expenses](#3-viewing-expenses)
      * [Editing an Expense](#4-editing-expense)
      * [Deleting an Expense](#5-deleting-an-expense)
      * [Summarizing Expenses](#6-summarizing-expenses)
      * [Exporting Data to CSV](#7-exporting-data-to-csv)
      * [User-Friendly Interface](#8-user-friendly-interface)
      * [Exit the Application](#9-exit-the-application)
  * [Future Features](#future-features)
  * [Technologies Used](#technologies-used)
  * [Deployment](#deployment)
  * [Testing](#testing)
      * [Bugs Fixed](#bugs-fixed)
  * [Credits](#credits)


## System Design

The Budget Manager application provides a comprehensive solution for managing your budget effectively. This section offers an in-depth look at the application’s design through both simple and detailed flowcharts.

### Simple Flowchart

The simple flowchart offers a high-level overview of the application’s core functionality. It serves as a draft idea to understand the overall concept and the main operations of the app. This visualization is helpful for quickly grasping the application’s workflow.

![Budget Manager Simple Chart](/assets/images/simple.png)

### Detailed Flowchart

The detailed flowchart provides a closer look at the application’s processes and logic. It breaks down each step involved in the workflow, including user inputs, validation processes, and error handling. This detailed visualization is crucial for comprehending the intricate workings of the app and ensuring that each component interacts seamlessly.

![Budget Manager Detailed Chart](/assets/images/detailed_chart.png)


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

### 1. Displaying a Main Menu
*   Display a welcome message to the user upon launching the application.
*   Present the main menu with options for each feature, including “Add a New Expense,” “View Expenses,” “Edit an Expense,” “Delete an Expense,” “Summarize Expenses,” “Export Data to CSV,” “Set a Budget Limit,” and “Exit the Application.”

![Main Menu](/assets/images/main.png)

### 2. Adding a New Expense
*	Prompt the user to enter the date, category, description, and amount for a new expense.
*	Validate the input to ensure all details are entered correctly.
*	Add the validated expense to the list of expenses.

![Add](/assets/images/add.png)

### 3. Viewing Expenses
*	Display a list of all recorded expenses with details including date, category, description, and amount.
*	Handle cases where no expenses are recorded and notify the user accordingly.

![View](/assets/images/view.png)

### 4. Editing an Expense
*	Allow the user to select an existing expense to edit from the list.
*	Prompt the user to enter the new details for the selected expense.
*	Update the expense with the new details upon validation.

![Edit](/assets/images/edit.png)

### 5. Deleting an Expense
*	Enable the user to select an existing expense to delete from the list.
*	Remove the selected expense from the list after confirmation.

![Delete](/assets/images/delete.png)

### 6. Summarizing Expenses
*	Provide a summary of expenses categorized by expense type (e.g., Housing, Utilities, Groceries, etc.).
*	Calculate and display the total amount spent.
*	Calculate and display the remaining budget based on the initial budget limit.

![Summarize](/assets/images/summarize.png)

### 7. Exporting Data to CSV
*	Export the list of expenses to a CSV file named expense_summary.csv.
*	Include columns for Date, Category, Description, and Amount in the CSV file.
*	Handle file-related errors and notify the user in case of any issues during the export process.

![Export-CSV](/assets/images/export.png)

### 8. User-Friendly Interface
*	Print informative and visually distinct messages for different actions (e.g., errors in red and titles in green).
*	Display a main menu with options for each feature.
*	Ensure all user inputs are validated and handle invalid inputs gracefully.

![User-Friendly](/assets/images/error.png)

### 9. Exiting the Application
*	Provide an option for the user to exit the application.
*	Display a thank-you message upon exiting.

![Exit](/assets/images/exit.png)


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

I performed both manual and automatic tests. The results of the manual tests can be found in the [TESTING.md.](/TESTING.md) 

For automatic tests, I used the following tools:

1.  Pycodestyle: Checks Python code against the PEP 8 style guide to ensure consistency and readability.

2.	Flake8: Combines Pycodestyle, pyflakes, and mccabe to check code style, detect errors, and measure complexity, ensuring a clean and manageable codebase.

3.	Pylint: A static code analysis tool that catches errors, enforces coding standards, and suggests refactoring to maintain high code quality.

### Bugs Fixed

1.	E501 - Line too long:
	_How I fixed_: I broke long lines of code into multiple lines to ensure they are within the PEP 8 recommended limit of 79 characters per line. I used line continuation characters (backslash) or wrapped lines within parentheses for better readability.

2.	E211 - Whitespace before:
	_How I fixed_: I removed any unnecessary whitespace before parentheses, brackets, or other punctuation. I ensured there was no space between a function name and the opening parenthesis when calling the function.

3.	E302 - Too many blank lines:
	_How I fixed_: I ensured there were no more than two blank lines separating top-level functions and class definitions. I maintained a single blank line between methods within a class.

4.	F821 - Undefined name:
	_How I fixed_: I made sure all variables and functions were defined before they were used. I checked for typos or missing imports that could cause names to be undefined.


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

