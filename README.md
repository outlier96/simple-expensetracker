# simple-expensetracker

This is a simple Python script for managing expenses. 

The script defines a list `expenses` and some functions to add, remove, and list expenses. 

- The `addExpense` function takes three parameters (`amount`, `category`, and `expense_name`) and creates a dictionary containing those values. The dictionary is then added to the `expenses` list using the `append` method.
- The `removeExpense` function allows the user to select an expense to remove from the `expenses` list. The function displays a list of all expenses, prompts the user to enter the number of the expense they want to remove, and then uses the `del` statement to remove that expense from the list.
- The `listExpenses` function displays a formatted list of all expenses in the `expenses` list.
- The `printMenu` function displays a simple menu with three options: add a new expense, remove an expense, or view expenses.

The `while` loop at the end of the script runs the `printMenu` function and prompts the user to select an option. Depending on the option selected, the script calls the `addExpense`, `removeExpense`, or `listExpenses` function. 

Note that this script is very basic and does not include any error handling or validation of user input. It is intended as an example of a simple Python script for managing expenses, but would need to be modified and improved for use in a real-world application.
