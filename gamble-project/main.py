import random

MAX_LINES = 3

ROWS, COLS = 3,3

#collects deposit from the user:
def deposit():
    while True:
        amount = input("What would you like to deposit? $: ")
        if amount.isdigit(): #check, the input is number or not
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("No of lines should be between (1-3)")
    return lines

def get_bet(balance: int):
    while True:
        amount = input("What would you like to bet? $:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and balance >= amount:
                break
            else:
                print("Please enter a valid bet. Your balance is: {balance}")
        else:
            print(f"Please check your input!!!")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet_amount = get_bet(balance)
    
    print("Balance you have is {}$, and No of lines you bet on {}. Your bet amount is {}$".format(balance, lines, bet_amount))

main()