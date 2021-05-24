class Bank:
    def __init__(self):
        self.balance = 0
        print("The new account is created")
    def deposit(self):
        self.amount = float(input("Enter  amount to be deposited:"))
        self.balance = self.balance+self.amount
        print(f"Deposit is successful and the balance is {self.balance}")
    def withdraw(self):
        self.amount=float(input("Enter amount to be withdraw: "))
        if(self.balance >= self.amount):
             self.balance = self.balance-self.amount
             print(f"Withdraw is successful and the balance is {self.balance}")
        else:
             print("Insuficient balance")
    def enquiry(self):
            print(f"Balance on your account is {self.balance}")

account = Bank()
account.deposit()
account.withdraw()
account.enquiry()
