
expenses = []

def add_expense():
    try:
        amount = float(input("Enter expense amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category (Food, Travel, etc.): ").strip()
        if not category:
            print("Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | {expense['description']}"
        )

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ₹{total:.2f}")

while True:
    print("\n===== Student Expense Tracker =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you for using the Expense Tracker!")
        break
    else:
        print("Invalid option. Choose 1, 2, 3, or 4.")
