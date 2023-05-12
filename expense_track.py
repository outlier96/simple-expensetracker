expenses = []
expense1 = {'amount':'2000','category':'clothing','expense_name':'pants'}
expenses.append(expense1)
expense2 = {'amount':'2000','category':'transport','expense_name':'petrol'}
expenses.append(expense2)
expense3 = {'amount':'2000','category':'clothing','expense_name':'pants'}
expenses.append(expense3)


def removeExpense():
    while True:
        listExpenses()
        print('what expense would you like to remove...')
        try:
        
            expenseToRemove = int(input(">"))
            del expenses[expenseToRemove]
        except:
            print('invalid input pls enter the expense number...')
def addExpense(amount,category,expense_name):
    expense = {'amount': amount, 'category':category, 'expense_name':expense_name}
    expenses.append(expense)

def printMenu():
    print("please choose an option")
    print("1, Add a new expense")
    print("2, Remove a expense")
    print("3,view expenses")

def listExpenses():
    print("\nThis are all your expenses")
    print("________________________________________________________________________________________________________________________________")
    counter = 0
    for expense in expenses:
        print("#",counter, "-",expense['amount']," - ",expense['category']," - ",expense['expense_name'],)
        counter += 1
    print("\n\n")


if __name__ == "__main__": 
   while True:
     printMenu()
     optionSelected = input("enter Option")
     if (optionSelected == "1"):
         print("enter amount of expense?")
         while True:
            try:
                amountToAdd = input("> ")
                break
            except:
                print("invalid input")
         print("enter category of expense?")
         while True:
            try:
                category = input("> ")
                break
            except:
                print("invalid input")
         print("enter name of expense?")
         while True:
             try:
                expense_name = input(">")
                break
             except:
                 print("invalid input")

         addExpense(amountToAdd,category,expense_name)
     elif(optionSelected =="2"):
        removeExpense()
     elif(optionSelected =="3"):
        listExpenses()
     else:
        print("invalid option please try again")
         