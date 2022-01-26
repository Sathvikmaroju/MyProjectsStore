from password_strength import PasswordStats
#import math
import random
import string

def generatePassword(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.punctuation
    symbols = string.digits

    upper,lower,nums,sym = True, True, True, True
    # these must be set by user in next commit

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if sym:
        all += symbols

    password = "".join(random.sample(all,length))
    return password

def passwordStrength(password):
    result = PasswordStats(password)
    final = result.strength()
    # final_per = math.ceil(final*100)
    # ^- put this in gui
    
    if final>=0.66:
        return 'green' #strong
    elif final>0.10 and final<0.40:
        return 'yellow' #medium
    elif final<=0.10:
        return 'red' #weak

size = input("Enter length of password: ")
while not size.isnumeric() :
        print("\nInvalid!")
        print("Enter length of password: ")
        size = input()

password = generatePassword(int(size))
strength = passwordStrength(password)
print(f""" 
Given length of password: {size}
Password generated: '{password}'
Password strength: {strength}

red -> weak strength
yellow -> medium strength
green -> strong strength
""")