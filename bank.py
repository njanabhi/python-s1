class Bank:
    def getdata(self, accountNo, name, accounttype, balance):
        self.accountNo=accountNo
        self.name=name
        self.accounttype=accounttype
        self.balance=balance

    def displayaccountinfo(self):
        print("\n--- Account Information ---")
        print("Account Number:", self.accountNo)
        print("Name:", self.name)
        print("Account Type:", self.accounttype)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount   
        print("Amount Deposited:", amount)
        print("Available Balance:", self.balance)

    def withdraw(self, amount):
        if amount>self.balance:              
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
            print("Available Balance:", self.balance)
no = int(input("Enter Account Number: "))
n = input("Enter Name: ")
t = input("Enter Account Type (SB/C): ")
b = int(input("Enter the Opening Balance: "))
obj = Bank()
obj.getdata(no, n, t, b)
obj.displayaccountinfo()
deposit_amt = int(input("\nEnter amount to deposit: "))
obj.deposit(deposit_amt)
withdraw_amt = int(input("\nEnter amount to withdraw: "))
obj.withdraw(withdraw_amt)

