import random

def number():
    return random.randint(1,6)

print("Dice simulator\n")

while True:
    print("Enter 'y' to roll the dice.")
    user_inp = input()
    if user_inp == 'y':
        num = number()
        if num == 1:
            print("---------", "|       |", "|   o   |", "|       |", "---------",sep='\n')
        elif num == 2:
            print("---------", "|       |", "| o   o |", "|       |", "---------",sep='\n')
        elif num == 3:
            print("---------", "|   o   |", "|   o   |", "|   o   |", "---------",sep='\n')
        elif num == 4:
            print("---------", "| o   o |", "|       |", "| o   o |", "---------",sep='\n')
        elif num == 5:
            print("---------", "| o   o |", "|   o   |", "| o   o |", "---------",sep='\n')
        elif num == 6:
            print("---------", "| o   o |", "| o   o |", "| o   o |", "---------",sep='\n')
    else:
        break