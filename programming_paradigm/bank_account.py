class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        self.balance += amount
        
    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds exist."""
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew: ${amount:.2f}"
    
    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current Balance: ${self.balance}")
