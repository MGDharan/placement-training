class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self, amount, category, description=""):
        expense = {"amount": amount, "category": category, "description": description}
        self.expenses.append(expense)
        print(f"Added expense: {expense}")
    def generate_report(self):
        report = {}
        for expense in self.expenses:
            if expense["category"] not in report:
                report[expense["category"]] = 0
            report[expense["category"]] += expense["amount"]
        return report
    def display_report(self):
        report = self.generate_report()
        print("Expense Report:")
        for category, total in report.items():
            print(f"{category}: ${total:.2f}"
tracker = ExpenseTracker()
tracker.add_expense(50, "Food", "Groceries")
tracker.add_expense(20, "Transport", "Bus ticket")
tracker.add_expense(100, "Entertainment", "Concert ticket")
tracker.display_report()
