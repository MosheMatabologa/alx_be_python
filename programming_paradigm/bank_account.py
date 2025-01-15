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
        Check if the withdrawal amount is less than or equal to the current balance and print the result.
        """
        if amount <= self.balance:
            print(True)
        else:
            print(False)
        
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
        self.check_balance(amount)  # Check balance before withdrawal
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
if __name__ == "__main__":
    # Create an account with an initial balance of 1000
    my_account = BankAccount(initial_balance=1000)
    
    # Deposit 0 into the account
    my_account.deposit(0)
    
    # Attempt to withdraw 550
    result = my_account.withdraw(550)
    
    # Display the balance and withdrawal result
    my_account.display_balance()  # This will display the balance
    print(f"Final Balance: {my_account.balance}")
    print(f"Withdrawal Result: {result}")
