class BalException(Exception):
    pass

class BankAcc:
    #initializor 
    def __init__ (self, P, accname):
        self.balance = P
        self.name = accname
        print(f"\nAccount '{self.name}'  created. \nBalance = ${self.balance:.2f}")

    #method
    def getBal(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f} ")
    
    def deposit(self, amt):
        self.balance = self.balance + amt
        print(f"\nDeposit Complete.")
        self.getBal()

    
    def viabletransaction(self, amt):
        if self.balance >= amt:
            return 
        else:
            raise BalException("\nSorry, less balance!")
    
    def withdraw(self, amt):
        try:
            self.viabletransaction(amt)
            self.balance = self.balance - amt
            print("\nWithdraw Complete.")
            self.getBal()
        except BalException as error:
            print(f"Withdraw interrupted: {error}")

    
    def transfer(self, amt, acc):
        try:
            print("\n********\nBeginning Transfer!")
            self.viabletransaction(amt)
            self.withdraw(amt)
            acc.deposit(amt)
            print("\nTransfer Complete!\n\n")
        except BalException as error:
            print(f"Transfer interrupted: {error}")

class InterestRewards(BankAcc):
    def deposit(self, amt):
        self.balance = self.balance + (amt * 1.05)
        print("\nDeposit complete.")
        self.getBal()

class SavingsAcc(InterestRewards):
    def __init__(self, P, accname):
        super().__init__(P, accname)
        self.fee = 5
    
    def withdraw(self, amt):
        try:
            self.viabletransaction(amt + self.fee)
            self.balance = self.balance - (amt + self.fee)
            print("\nWithdraw complete.")
            self.getBal()
        except BalException as error:
            print(f"\nWithdraw interrupted: {error}.")




    


