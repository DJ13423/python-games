from time import sleep

load_character_delay = 0.05
lines = ['|----------------------|',
         '|----[Python Games]----|',
         '|----------------------|',
         '|-------Coded by-------|',
         '|-----DJ (DJ13423)-----|',
         '|----------------------|']
for line in lines:
    current_line = ''
    for char in line:
        current_line += char
        print(current_line, end='\r')
        sleep(load_character_delay)
    print()

"""
answer = input()
if answer == '1':
    import games.dice_roll
"""
#Still working on this file
