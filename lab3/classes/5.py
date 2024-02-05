class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"deposit of {amount} accepted. New balance:{self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"withdraw of {amount} accepted. new balance:{self.balance}")
        else:
            print("insufficient funds")

account = Account(input("owner is: "), abs(float(input("the balance is:"))))

account.deposit(float(input("write the amount u wanna deposit: ")))
account.withdraw(float(input("write the amount u wanna withdraw:")))
