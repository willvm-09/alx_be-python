class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        deposit = amount + self.account_balance
        return deposit
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            self.account_balance = self.account_balance
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")