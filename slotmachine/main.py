import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for key, value in symbols.items():
        for _ in range(value):
            all_symbols.append(key)
    random.shuffle(all_symbols)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
        
    return columns

# transposing
def print_slot_machine(columns):
    print(columns)
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=' | ')
        else:
            print()
            # if i != len(columns) -1:
            #     print(column[row], end='|')
            # else:
            #     print(columns[row])

def deposit() -> int:
    while True:
        amount = input('What would you like to deposit $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than zero')
        else:
            print('Please enter a number')
    return amount

def get_number_of_lines() -> int:
    while True:
        lines = input('Enter the number of lines to bet on (1, '+str(MAX_LINES)+')? ')
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines')
        else:
            print('Please enter a number')
    return lines

def get_bet():
    while True:
        amount = input('What would you like to bet on each line $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('Please enter a number')
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You don't have enough balance to bet. Your balance {balance}")
        else:
            break
    
    print(f'You are betting {bet} on {lines} lines. Total bet will be {total_bet}')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    

if __name__ == '__main__':
    print('Main block!!!')
    main()