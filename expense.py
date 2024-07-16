class Expense:
    def __init__(self, date, category, description, amount) -> None:
        """
        Initialize the expense with date, category, description, and amount.
        """
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __repr__(self):
        """
        Returns a string representation of the expense. 
        """
        return f"{self.date}, {self.category}, {self.description}, €{self.amount:.2f}"