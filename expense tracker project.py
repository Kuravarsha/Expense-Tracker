import json
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ["Food", "Transportation", "Entertainment", "Bills", "Other"]

    # Add an expense
    def add_expense(self, amount, description, category):
        if category not in self.categories:
            raise ValueError(f"Invalid category. Choose from {self.categories}")
        
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        }
        self.expenses.append(expense)

    # Save expenses to a file
    def save_expenses(self, filename="expenses.json"):
        try:
            with open(filename, "w") as file:
                json.dump(self.expenses, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    # Load expenses from a file
    def load_expenses(self, filename="expenses.json"):
        try:
            with open(filename, "r") as file:
                self.expenses = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

    # View all expenses
    def view_expenses(self):
        for exp in self.expenses:
            print(f"{exp['date']}: {exp['description']} - {exp['category']} - ${exp['amount']}")

    # Monthly summary
    def monthly_summary(self, month, year):
        total = 0
        for exp in self.expenses:
            exp_date = datetime.datetime.strptime(exp['date'], "%Y-%m-%d")
            if exp_date.month == month and exp_date.year == year:
                total += exp['amount']
        print(f"Total expenses for {month}/{year}: ${total}")

    # Category-wise summary
    def category_summary(self):
        summary = {category: 0 for category in self.categories}
        for exp in self.expenses:
            summary[exp['category']] += exp['amount']
        for cat, total in summary.items():
            print(f"Total spent on {cat}: ${total}")

# Main interaction
def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Save Expenses")
        print("6. Load Expenses")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            try:
                amount = float(input("Enter the amount: "))
                description = input("Enter a brief description: ")
                category = input(f"Choose a category {tracker.categories}: ")
                tracker.add_expense(amount, description, category)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            tracker.view_expenses()
        
        elif choice == "3":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (YYYY): "))
            tracker.monthly_summary(month, year)
        
        elif choice == "4":
            tracker.category_summary()
        
        elif choice == "5":
            tracker.save_expenses()
            print("Expenses saved successfully!")
        
        elif choice == "6":
            tracker.load_expenses()
            print("Expenses loaded successfully!")
        
        elif choice == "7":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
