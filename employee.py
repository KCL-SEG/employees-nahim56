"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        for key in Employees.keys():
           if key == self:
              print(Employees.get(key))

    def __str__(self):
        for key in Descriptions.keys():
           if key == self:
              print(Descriptions.get(key))


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800."
renee = Employee('Renee')

# "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410."
jan = Employee('Jan')

# "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500."
robbie = Employee('Robbie')

# "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200."
ariel = Employee('Ariel')

Employees = { billie:4000,charlie:2500,renee:3800,jan:4410,robbie:3500,ariel:4200}
Descriptions = {billie:"Billie works on a monthly salary of 4000.  Their total pay is 4000.",charlie:"Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.",renee:"Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.",jan:"Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.",robbie:"Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.",ariel:"Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200."}
