# Expense Tracker - CLI Application

FILE_NAME = "expenses.txt"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category},{note}\n")

    print("Expense added successfully.\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.\n")
            return

        print("\nAmount | Category | Note")
        print("-" * 30)

        for expense in expenses:
            amount, category, note = expense.strip().split(",")
            print(f"{amount} | {category} | {note}")

        print()

    except FileNotFoundError:
        print("No expenses file found.\n")


def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                amount = float(line.split(",")[0])
                total += amount

        print(f"\nTotal Expense: ₹{total}\n")

    except FileNotFoundError:
        print("No expenses file found.\n")


def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
