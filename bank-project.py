import sys

class Customer:

    bank_name = 'State Bank of India'

    def __init__(self, name, amount = 0) -> None:
        self.customer_name = name
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("You can't withdraw", amount, 'it is lower than your current balance')
            sys.exit()
        self.balance -= amount
        print('After withdrawal your balance is: ', self.balance)

print('Welcome to ', Customer.bank_name)

print()

while True:
    customer = Customer(input('Name: '), float(input('enter your amount')))
    usr_choice = input('Choose d: deposit \nw: withdraw\ne: exit')
    if usr_choice.lower() == 'd':
        customer.deposit(float('enter the amount to be deposited: '))
    elif usr_choice.lower() == 'w':
        customer.withdraw(float(input('amount to be withdraw: ')))
    elif usr_choice.lower() == 'e':
        print('Please come again!!!')
        sys.exit()
    else:
        print('Please choose a valid input ')

