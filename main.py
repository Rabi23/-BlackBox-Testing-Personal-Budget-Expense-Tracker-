import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Global variable to track all transactions and the running balance
transactions = []
current_balance = 0.0

def add_transaction():
    global current_balance
    try:
        amount_str = entry_amount.get().strip()
        date_str = entry_date.get().strip()
        category = entry_category.get().strip()
        description = entry_desc.get().strip()

        # 1. Input Validation (Black Box Test Focus)
        if not amount_str or not date_str or not category:
            messagebox.showerror("Error", "Amount, Date, and Category are required.")
            return

        amount = float(amount_str)
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be positive.")
            return

        # Date Format Check (YYYY-MM-DD)
        try:
            transaction_date = datetime.strptime(date_str, "%Y-%m-%d")
            if transaction_date > datetime.now():
                 messagebox.showerror("Error", "Date cannot be in the future.")
                 return
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return
            
        # 2. Calculation Logic
        current_balance -= amount # For simplicity, treat all as expenses for this test
        transactions.append((date_str, amount, category, description))

        # 3. UI Update
        update_display()
        
        # Clear fields after successful addition
        entry_amount.delete(0, tk.END)
        entry_desc.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric amount.")


def update_display():
    # Update the transaction list and balance label
    transaction_list.delete(0, tk.END)
    for date, amount, category, desc in transactions:
        transaction_list.insert(tk.END, f"{date} | {category}: -${amount:.2f} ({desc})")
    
    balance_label.config(text=f"Current Balance (Simulated): ${current_balance:.2f}")


# ---------------- UI DESIGN ---------------- #

root = tk.Tk()
root.title("Personal Budget & Expense Tracker (Finance Sector)") # Unique Title
root.geometry("600x550")
root.resizable(False, False)

title = tk.Label(root, text="Expense Tracker V1.0", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10, relief=tk.GROOVE, borderwidth=1)
input_frame.pack(pady=5)

tk.Label(input_frame, text="Amount ($)").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_amount = tk.Entry(input_frame)
entry_amount.grid(row=0, column=1)

tk.Label(input_frame, text="Date (YYYY-MM-DD)").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_date = tk.Entry(input_frame)
entry_date.insert(0, datetime.now().strftime("%Y-%m-%d")) # Default date
entry_date.grid(row=1, column=1)

tk.Label(input_frame, text="Category").grid(row=2, column=0, padx=5, pady=5, sticky="w")
category_options = ["Food", "Transport", "Bills", "Misc"]
entry_category = tk.StringVar(root)
entry_category.set(category_options[0])
category_menu = tk.OptionMenu(input_frame, entry_category, *category_options)
category_menu.grid(row=2, column=1)

tk.Label(input_frame, text="Description").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_desc = tk.Entry(input_frame)
entry_desc.grid(row=3, column=1)

# Button
tk.Button(root, text="Add Expense", command=add_transaction,
          bg="#FF6347", fg="white", width=25).pack(pady=10)

# Result Display
balance_label = tk.Label(root, text="Current Balance (Simulated): $0.00", font=("Arial", 12, "bold"))
balance_label.pack(pady=5)

tk.Label(root, text="Transaction History:", font=("Arial", 10)).pack()
transaction_list = tk.Listbox(root, height=8, width=70)
transaction_list.pack(padx=10, pady=5)

root.mainloop()