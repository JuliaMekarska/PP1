import random

class account():
    
    def __init__(self, number):
        
        self.account_no = number
        self.account_balance = 0
        
        
    def deposit(self, amount):
        
        self.account_balance += amount
        
    def withdraw(self, amount):
        
        if amount <= self.account_balance:
            
            self.account_balance -= amount
            
        else:
            
            print("Insufficient funds on the account.")
            
    def show_status(self):
        
        print(f"Bank Account No:{self.account_no}")
        print(f"Balance: PLN {self.account_balance}")
            
        
        