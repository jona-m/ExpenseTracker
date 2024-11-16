from datetime import datetime

class Expense:

    def __init__(self, name, category, amount) -> None:
       self.name = name
       self.category = category
       self.amount = amount
       self.date = datetime.now().strftime('%d-%m-%Y')
       

    def __repr__(self):
          return f"<Expense:   {self.category}, {self.name} {self.amount} on {self.date}>" 