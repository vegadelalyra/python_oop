class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.__balance) # ERROR!
print("Initial balance:", account._BankAccount__balance)

account.deposit(500)
account.withdraw(200)

print("Current balance:", account.get_balance())
