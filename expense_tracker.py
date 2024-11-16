from expense import Expense

def main():
    print(f"Running expense tracker")
    expenses_file_path = "expenses.csv"
    
#Get user to iinput their expense
    expense = get_user_expenses()
    

#Write the expense to a file
    save_expense_to_file(expense, expenses_file_path)

#Read file and summarise the expenses
    summarize_expenses(expenses_file_path)


def get_user_expenses():
    print(f"Getting expenses")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories =["🚎Transport","🍝Food","🧃Drinks","🛍️Clothes","💄Beauty","🧼Skincare","🏠Home","🫰Personal","🍾Going out","🤔Other"]
    
    while True:
        print(" Select a category")
        for i, category_name in enumerate(expense_categories):
            print(f"   {i + 1}. {category_name}")
        value_range = f'[1 - {len(expense_categories)}]'
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            new_expense = Expense(name=expense_name,category=expense_categories[selected_index], amount= expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again! ")
        

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.category},{expense.name},{expense.amount},{expense.date}\n ")

    


def summarize_expenses(expense_file_path):
    print("Summarize expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as r:
        lines = r.readlines()
        for line_number, line in enumerate(lines, start=1):
            if not line.strip():
                if line_number == len(lines):
                    break
                print(f"Skipping empty line {line_number}")
                continue
            try:
                expense_category, expense_name, expense_amount, date = line.strip().split(",")
                expense_amount = float(expense_amount)
            except ValueError:
                print(f"Error on line {line_number}: '{line.strip()}' - Not enough values to unpack")

            line_expense = Expense(name=expense_name, category=expense_category, amount=expense_amount)  
            line_expense.date = date  
            expenses.append(line_expense)
       

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
             amount_by_category[key] = expense.amount

    print("Expenses by category")   
    for key, amount in amount_by_category.items():
        print(f" {key}: {amount} Lek")   

    total_spent =sum([x.amount for x in expenses]) 
    print(f"💰Total expenses: {total_spent} Lek")          


if __name__ == '__main__':
    main()