import json
import os
from datetime import datetime

class BudgetApp:
    def __init__(self, data_file="budget_data.json"):
        self.data_file = data_file
        self.budgets = {}  # {category: {"limit": float, "spent": float}}
        self.transactions = []  # List of {date, category, amount, description}
        self.load_data()

    def load_data(self):
        """Load budgets and transactions from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.budgets = data.get("budgets", {})
                self.transactions = data.get("transactions", [])
        else:
            self.budgets = {}
            self.transactions = []

    def save_data(self):
        """Save budgets and transactions to JSON file."""
        data = {
            "budgets": self.budgets,
            "transactions": self.transactions
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def set_budget(self, category, limit):
        """Set or update budget limit for a category."""
        if limit < 0:
            print("Budget limit cannot be negative!")
            return
        self.budgets[category] = {
            "limit": float(limit),
            "spent": self.budgets.get(category, {"spent": 0}).get("spent", 0)
        }
        self.save_data()
        print(f"Budget for {category} set to ${limit:.2f}")

    def log_transaction(self, category, amount, description=""):
        """Log a transaction and enforce budget rules."""
        if category not in self.budgets:
            print(f"No budget set for {category}. Please set a budget first.")
            return

        amount = float(amount)
        if amount < 0:
            print("Transaction amount cannot be negative!")
            return

        current_spent = self.budgets[category]["spent"]
        budget_limit = self.budgets[category]["limit"]
        new_spent = current_spent + amount

        # Check if transaction exceeds budget
        if new_spent > budget_limit:
            print(f"Warning: This transaction (${amount:.2f}) exceeds {category} budget!")
            override = input("Justify override (or 'cancel' to cancel): ")
            if override.lower() == "cancel":
                print("Transaction cancelled.")
                return
            
            print(f"Override approved with justification: {override}")
        elif new_spent >= budget_limit * 0.8:
            print(f"Alert: You've spent {new_spent/budget_limit*100:.1f}% of your {category} budget!")

        # Record transaction
        self.budgets[category]["spent"] = new_spent
        self.transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category,
            "amount": amount,
            "description": description
        })
        self.save_data()
        print(f"Transaction logged: ${amount:.2f} in {category} ({description})")

    def view_budget(self):
        """Display current budget status."""
        if not self.budgets:
            print("No budgets set yet.")
            return
        print("\nBudget Status:")
        for category, data in self.budgets.items():
            spent = data["spent"]
            limit = data["limit"]
            percent = (spent / limit * 100) if limit > 0 else 0
            print(f"{category}: ${spent:.2f} || ${limit:.2f} ({percent:.1f}% used)")

    def view_transactions(self):
        """Display all transactions."""
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        print("\nTransaction History:")
        for t in self.transactions:
            print(f"{t['date']} || {t['category']} || ${t['amount']:.2f} || {t['description']}")

def main():
    app = BudgetApp()

    while True:
        print("\nFinanceMe")
        print("1. Set Budget")
        print("2. Log Transaction")
        print("3. View Budget")
        print("4. View Transactions")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            category = input("Enter category (e.g., groceries): ")
            try: #people will try to type in letters
                limit = float(input("Enter budget limit: "))
                app.set_budget(category, limit)
            except ValueError:
                print("Invalid input. Please enter a number for the limit.")

        elif choice == "2":
            category = input("Enter category: ")
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description (optional): ")
                app.log_transaction(category, amount, description)
            except ValueError:
                print("Invalid input. Please enter a number for the amount.")

        elif choice == "3":
            app.view_budget()

        elif choice == "4":
            app.view_transactions()

        elif choice == "5":
            print("Exiting app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()