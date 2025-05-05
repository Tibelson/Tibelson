#Strict Budget App
#Strict Budget App is a command-line Python application designed to help users manage 
#their finances with discipline. It allows you to set monthly budgets 
#for different spending categories, track transactions, and enforce strict spending 
#limits to prevent overspending. The app warns users when they approach their budget 
#limits and requires justification for exceeding them, promoting mindful spending habits.
Features
	•	Set Budgets: Define monthly spending limits for categories like groceries, dining, or entertainment.
	•	Track Spending: Log transactions with amounts, categories, and optional descriptions.
	•	Strict Enforcement:
	◦	Alerts when you reach 80% of a category’s budget.
	◦	Blocks transactions exceeding the budget unless overridden with a justification.
	•	Persistent Storage: Saves budgets and transactions to a JSON file for continuity between sessions.
	•	View Insights: Displays current budget status and transaction history.
Installation
Prerequisites
	•	Python 3.6 or higher
	•	No external libraries required (uses only standard Python modules)
Steps
	1	Clone or Download:
	◦	Clone this repository:
git clone https://github.com/Tibelson/strict-budget-app.git
	◦	
Or download the ZIP file and extract it.
	2	Navigate to the Directory:
cd strict-budget-app
	3	
	4	Run the App:
python budget_app.py
	5	
Usage
	1	Launch the App: Run python budget_app.py to start the command-line interface.
	2	Menu Options:
	◦	1. Set Budget: Enter a category (e.g., “groceries”) and a spending limit (e.g., 200).
	◦	2. Log Transaction: Specify the category, amount, and an optional description. 
    The app checks against the budget and may 
    require justification for overspending.
	◦	3. View Budget: See current spending vs. limits for all categories.
	◦	4. View Transactions: Review your transaction history.
	◦	5. Exit: Save data and close the app.
	3	Example Interaction:
Strict Budget App
	4	1. Set Budget
	5	2. Log Transaction
	6	3. View Budget
	7	4. View Transactions
	8	5. Exit
	9	Choose an option (1-5): 1
	10	Enter category (e.g., groceries): groceries
	11	Enter budget limit: 200
	12	Budget for groceries set to $200.00
	13	
	14	Data Storage:
	◦	Budgets and transactions are saved to budget_data.json in the project directory.
	◦	The file is automatically created on first use and updated after every action.
File Structure
strict-budget-app/
│
├── budget_app.py        # Main application code
├── budget_data.json     # Data file for budgets and transactions (auto-generated)
└── README.md            # This file
Future Enhancements
	•	GUI Interface: Add a graphical interface using Tkinter, PyQt, or Kivy.
	•	Bank Integration: Sync with bank accounts via APIs like Plaid for real-time transaction tracking.
	•	Advanced Rules: Support weekly budgets, recurring expenses, or automatic savings transfers.
	•	Analytics: Visualize spending trends with charts or predict potential overspending.
	•	Security: Encrypt sensitive data and add user authentication.
