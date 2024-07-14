class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        current_balance = amount + self.account_balance
        return current_balance
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            self.account_balance = self.account_balance
            return False
        
    def display_balance(self):
        float(print(f"Current Balance: ${self.account_balance}"))