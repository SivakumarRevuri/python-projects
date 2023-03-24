import random as rd
from typing import Final


intro = '''Let's play the game!!! 
    What is your choice among Rock, Paper, Scissors: '''
SYS_WIN_MSG: Final[str] = 'Computer wins!!!'
USR_WIN_MSG: Final[str] = 'Hurry! you win the game'
choices = ['rock', 'paper', "scissors"]
count = 0
while True:
    print('*'*20)
    usr_choice = input("throw a sign!!! ")
    sys_choice = rd.choice(choices)
    print('Computer throws {0}'.format(sys_choice))
    match usr_choice.lower():
        case 'rock':
            if sys_choice == 'paper':
                print(SYS_WIN_MSG)
            elif sys_choice == 'scissors':
                print(USR_WIN_MSG)
            else:
                print('Both thrown rock!!!, continue the game')
                continue
        case 'paper':
            if sys_choice == 'scissors':
                print(SYS_WIN_MSG)
            elif sys_choice == 'rock':
                print(USR_WIN_MSG)
            else:
                print('Both thrown paper!!!, continue the game')
                continue
        case 'scissors':
            if sys_choice == 'rock':
                print(SYS_WIN_MSG)
            elif sys_choice == 'paper':
                print(USR_WIN_MSG)
            else:
                print('Both thrown scissors!!!, continue the game')
                continue

