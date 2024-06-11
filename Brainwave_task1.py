import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive!"
        self.balance += amount
        return f"${amount:.2f} deposited successfully! {self.check_balance()}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive!"
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"${amount:.2f} withdrawn successfully! {self.check_balance()}"

    def exit(self):
        return "Thank you for using the ATM. Goodbye!"

class ATMInterface:
    def __init__(self, root, atm):
        self.atm = atm
        self.root = root
        root.title("ATM Interface")

        # Balance display
        self.balance_label = tk.Label(root, text="Your Balance: $0.00", font=('Helvetica', 16))
        self.balance_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Amount entry
        self.amount_label = tk.Label(root, text="Amount", font=('Helvetica', 12))
        self.amount_label.grid(row=1, column=0, pady=5)
        
        self.amount_entry = tk.Entry(root, font=('Helvetica', 12))
        self.amount_entry.grid(row=1, column=1, pady=5)

        # Buttons
        self.check_balance_button = tk.Button(root, text="Check Balance", font=('Helvetica', 12), command=self.check_balance, width=15)
        self.check_balance_button.grid(row=2, column=0, pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", font=('Helvetica', 12), command=self.deposit, width=15)
        self.deposit_button.grid(row=2, column=1, pady=5)

        self.withdraw_button = tk.Button(root, text="Withdraw", font=('Helvetica', 12), command=self.withdraw, width=15)
        self.withdraw_button.grid(row=3, column=0, pady=5)

        self.exit_button = tk.Button(root, text="Exit", font=('Helvetica', 12), command=self.exit, width=15)
        self.exit_button.grid(row=3, column=1, pady=5)

        # Result display
        self.result_label = tk.Label(root, text="", font=('Helvetica', 12), fg='blue')
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def check_balance(self):
        result = self.atm.check_balance()
        self.result_label.config(text=result)
        self.update_balance_label()

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            result = self.atm.deposit(amount)
            self.result_label.config(text=result)
            self.update_balance_label()

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            result = self.atm.withdraw(amount)
            self.result_label.config(text=result)
            self.update_balance_label()

    def exit(self):
        result = self.atm.exit()
        messagebox.showinfo("Exit", result)
        self.root.quit()

    def update_balance_label(self):
        self.balance_label.config(text=f"Your Balance: ${self.atm.balance:.2f}")

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be positive")
            return amount
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Invalid amount: {e}")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM()
    atm_interface = ATMInterface(root, atm)
    root.mainloop()