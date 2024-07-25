# Testing

## Introduction

This document details the testing procedures for the Budget Manager application. Each feature is tested for expected functionality and any deviations are noted.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome Message | Launch the application | Welcome message is displayed | Works as expected |
| Main Menu| Application displays main menu | Main menu options (1-7) are displayed| Works as expected | 
| Add Expense | Select “Add a New Expense” from the menu| Prompt to enter expense details is displayed| Works as expected | 
| Add Expense | Enter valid expense details | Expense is added to the list| Works as expected | 
| Add Expense | Enter invalid date format| Error message for invalid date is displayed| Works as expected | 
| Add Expense | Enter empty description| Error message for empty description is displayed| Works as expected | 
| Add Expense | Enter non-numeric expense amount| Error message for invalid amount is displayed| Works as expected | 
| View Expenses | Select “View Expenses” from the menu| List of all expenses is displayed| Works as expected | 
| Edit Expense| Select “Edit an Expense” from the menu| List of expenses for selection is displayed| Works as expected | 
| Edit Expense| Select a valid expense to edit and enter new details|Selected expense is updated with new details | Works as expected | 
| Edit Expense|Select an invalid expense number | Error message for invalid number is displayed| Works as expected | 
| Delete Expense | Select “Delete an Expense” from the menu| List of expenses for selection is displayed| Works as expected | 
| Delete Expense |Select a valid expense to delete|Selected expense is removed from the list | Works as expected | 
| Delete Expense |Select an invalid expense number| Error message for invalid number is displayed| Works as expected | 
| Summarize Expenses| Select “Summarize Expenses” from the menu| Summary of expenses by category and budget status is displayed| Works as expected | 
| Summarize Expenses| No expenses in the list| Message indicating no expenses found is displayed| Works as expected | 
| Export Data to CSV | Select “Export Data to CSV” from the menu| Data is exported to a CSV file| Works as expected | 
| Exit Application | Select “Exit” from the menu|Application exits with a goodbye message| Works as expected | 

This document ensures that each feature of the Budget Manager application is functioning as expected. If any discrepancies are found during testing, they will be documented under the “Actual Result” column.

Go back to [README.md](/README.md)

