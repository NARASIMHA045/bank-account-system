


import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append((datetime.datetime.now(), f"Deposited ₹{amount}"))
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append((datetime.datetime.now(), f"Withdrew ₹{amount}"))
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Invalid or insufficient balance!")

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")

    def account_statement(self):
        print("\n--- Account Statement ---")
        for date, action in self.transactions:
            print(f"{date.strftime('%Y-%m-%d %H:%M:%S')} - {action}")
        print(f"Current Balance: ₹{self.__balance}")
        print("-------------------------")

    def get_owner(self):
        return self.owner


def main():
    print("Welcome to NO Bank")
    name = input("Enter your name to open an account: ")
    account = BankAccount(name)
    print(f"\nHello, {name}! Your account has been created.\n")

    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Account Statement")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            account.account_statement()
        elif choice == '5':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
