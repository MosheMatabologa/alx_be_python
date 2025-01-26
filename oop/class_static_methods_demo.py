class Calculator:
    """A class to demonstrate the use of static and class methods."""
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and display the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
