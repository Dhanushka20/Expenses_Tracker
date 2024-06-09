import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Initialize expenses list
        self.expenses = []

        # Set up UI components
        self.setup_ui()

    def setup_ui(self):
        # Entry for expense description
        tk.Label(self.root, text="Description").grid(row=0, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=0, column=1, padx=10, pady=10)

        # Entry for expense amount
        tk.Label(self.root, text="Amount (LKR)").grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Add expense button with custom colors
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense, bg="green", fg="white")
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Listbox to display expenses
        self.expense_listbox = tk.Listbox(self.root, width=50, height=10)
        self.expense_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Delete expense button with custom colors
        self.delete_button = tk.Button(self.root, text="Delete Selected", command=self.delete_expense, bg="red",
                                       fg="white")
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Pie chart button with custom colors
        self.chart_button = tk.Button(self.root, text="Show Pie Chart", command=self.show_pie_chart, bg="blue",
                                      fg="white")
        self.chart_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Label to display the total amount
        self.total_label = tk.Label(self.root, text="Total: LKR 0.00")
        self.total_label.grid(row=6, column=0, columnspan=2, pady=10)

    def add_expense(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if description and amount:
            try:
                amount = float(amount)
                self.expenses.append((description, amount))
                self.update_expense_listbox()
                self.update_total()
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid amount.")
        else:
            messagebox.showerror("Input error", "Please enter both description and amount.")

    def delete_expense(self):
        selected_indices = self.expense_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Selection error", "Please select an expense to delete.")
            return

        for index in selected_indices[::-1]:
            del self.expenses[index]

        self.update_expense_listbox()
        self.update_total()

    def update_expense_listbox(self):
        self.expense_listbox.delete(0, tk.END)
        for description, amount in self.expenses:
            self.expense_listbox.insert(tk.END, f"{description}: LKR {amount:.2f}")

    def update_total(self):
        total = sum(amount for _, amount in self.expenses)
        self.total_label.config(text=f"Total: LKR {total:.2f}")

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def show_pie_chart(self):
        if not self.expenses:
            messagebox.showinfo("No Data", "There are no expenses to visualize.")
            return

        categories = [description for description, _ in self.expenses]
        amounts = [amount for _, amount in self.expenses]

        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Expense Visualize')
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
