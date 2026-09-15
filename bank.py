import pandas as pd

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(["Deposit", amount])

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(["Withdraw", amount])
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.balance)

    def save_transactions(self):
        df = pd.DataFrame(self.history,
                          columns=["Transaction", "Amount"])
        df.to_csv("transactions.csv", index=False)
        print("Transactions saved!")

# Main Program
acc = BankAccount("Rida", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.deposit(200)

acc.show_balance()

acc.save_transactions()

# Pandas Analysis
df = pd.read_csv("transactions.csv")

print("\nTransaction History")
print(df)

print("\nTotal Amount:")
print(df["Amount"].sum())

print("\nNumber of Transactions:")
print(len(df))