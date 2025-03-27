import csv
import os
# Simple budget manager to calculate income minus categorized expenses

# Dictionary to store expenses by category
expenses = {}

while True:
        # Prompt for income; "done" exits the program
        income = input("Please enter your monthly income (or 'done' to finish):")
        if income.lower() == "done":
            print("Exiting Program...")
            quit() # Clean exit
        else:
            try:
                income = float(income) # Convert to number
                if income >= 0:
                    break
                else:
                    print("Income must be a positive number")
            except:
                print("Income must be a number")

if os.path.exists("budget_data.csv"):
    with open("budget_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses[row["Category"]] = expenses.get(row["Category"], 0) + float(row["Amount"])

while True:
        # Get category; "done" ends input
        expense_category = input("Please enter an expense category (or 'done' to finish):")
        if expense_category.lower() == "done":
            break
        else:
            expense = input(f"Please enter the expense amount for {expense_category} (or 'done' to finish):")
            if expense.lower() == "done":
                break
            else: 
                try:   
                    expense = float(expense)
                    expense_category_stripped = expense_category.replace(" ", "") # Normalize category
                    if expense >= 0:
                        expenses[expense_category_stripped] = expenses.get(expense_category_stripped, 0) + expense
                    else:
                        print("Expense must be a positive number")  
                except:
                    print("Expense must be a number")

with open("budget_data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Amount"])
    for category, amount in expenses.items():
        writer.writerow([category, amount])


def printResults():
    # Calculate and display final results
    totalExpense = sum(expenses.values())
    balance = income - totalExpense
    print("\nResults:")
    for key, value in expenses.items():
        print(f"{key} : ${value}")
    print(f"Balance: ${balance}")
    print(f"Total Expenses: ${totalExpense}")
    quit()

printResults()