#!/usr/bin/env python3

class BankAccount:
    def __init__(self, initial_balance=0):    
        self.balance = initial_balance
        
    def display_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"Current Balance: {self.balance}")
        
    def check_balance(self, amount):
        """
        Check if the withdrawal amount is less than or equal to the current balance.
        """
        return amount <= self.balance
        
    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        """
        if not self.check_balance(amount):
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew: ${amount:.2f}"
    
if __name__ == "__main__":
    # Create an account with an initial balance of 1000
    my_account = BankAccount(initial_balance=1000)
    
    # Deposit 0 into the account
    my_account.deposit(0)
    
    # Attempt to withdraw 50
    result = my_account.withdraw(50)
    
    # Display the balance and withdrawal result
    my_account.display_balance()  # This will display the balance
    print(f"Final Balance: {my_account.balance}")
    print(f"Withdrawal Result: {result}")
