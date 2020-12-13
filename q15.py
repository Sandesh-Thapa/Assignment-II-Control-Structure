# Imagine you are designing a banking application. What would a customer look like? What attributes would she have? What methods would she have?

class Customer:
    def __init__(self, name, address, age, balance=0):
        self.name = name
        self.address = address
        self.age = age
        self.balance = balance
    
    def checkBalance(self):
        return self.balance

c = Customer('John', 'New York', 35, 5000)
print(c.checkBalance())