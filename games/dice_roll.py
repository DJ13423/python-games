from random import randint
from time import sleep
from utils import equals_or

answer = input('''
-------------------------
-------Dice roller-------
-------------------------
-|Press enter to start.|-\n''')
if equals_or(answer, 'exit', 'e'): exit()
print('- You can type \'exit\' or \'e\' at any time to leave,\n  and \'home\' or \'h\' to return to the main menu.')
sleep(1)
while True:
    print('\nEnter one of the following numbers: 1/2/3')
    sleep(0.4)
    print('| 1. Simple (1 die and 6 numbers)')
    sleep(0.4)
    print('| 2. Dual (2 dice and 6 numbers)')
    sleep(0.4)
    print('| 3. Advanced (Choose how many dice to roll and the numbers on the dice)')
    answer1 = input('-> ')
    if equals_or(answer1, 'exit', 'e'): exit()
    if equals_or(answer1, 'home', 'h'): continue
    if answer1 not in ['1', '2', '3']:
        print('Error: Please enter a whole number beetween 1 and 3')
        sleep(1)
        continue
    if answer1 == '1':
        print('Press enter to re-roll.\n')
        while True:
            answer2 = input(f'You rolled a {randint(1,6)}\n')
            if equals_or(answer2, 'exit', 'e'): exit()
            if equals_or(answer2, 'home', 'h'): break
        continue
    elif answer1 == '2':
        print('Press enter to re-roll.\n')
        while True:
            answer2 = input(f'You rolled a {randint(1,6)} and a {randint(1,6)}\n')
            if equals_or(answer2, 'exit', 'e'): exit()
            if equals_or(answer2, 'home', 'h'): break
        continue

    elif answer1 == '3':
        dice_amount = input('How many dice do you want to roll?\n-> ')
        if equals_or(dice_amount, 'exit', 'e'): exit()
        if equals_or(dice_amount, 'home', 'h'): continue
        try: dice_amount = int(dice_amount)
        except:
            print('Error: Please enter a whole number lager than 0.')
            sleep(1)
            continue
        if dice_amount < 1:
            print('Error: Please enter a whole number lager than 0.')
            sleep(1)
            continue
        dice_nums = input('What number do you want the dice to go up to?\n-> ')
        if equals_or(dice_nums, 'exit', 'e'): exit()
        if equals_or(dice_nums, 'home', 'h'): continue
        try: dice_nums = int(dice_nums)
        except:
            print('Error: Please enter a whole number lager than 1.')
            sleep(1)
            continue
        if dice_nums < 2:
            print('Error: Please enter a whole number lager than 1.')
            sleep(1)
            continue
        print('Press enter to re-roll.\n')
        while True:
            roll_message = ''
            if dice_amount == 1:
                roll_message = f'{randint(1,dice_nums)}'
            elif dice_amount == 2:
                roll_message = f'{randint(1,dice_nums)} and a {randint(1,dice_nums)}'
            else:
                for i in range(dice_amount-1):
                    roll_message += f'{randint(1,dice_nums)}, '
                roll_message += f'and {randint(1,dice_nums)}'
            answer2 = input(f'You rolled a {roll_message}\n')
            if equals_or(answer2, 'exit', 'e'): exit()
            if equals_or(answer2, 'home', 'h'): break
        continue
    else:
        print('An unexpected error has occured. Please enter values properly. Create a bug report if you are having problems.')
        sleep(1)
