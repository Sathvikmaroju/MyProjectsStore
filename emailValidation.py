import re

email_con = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_inp = input("Enter a email id: ")

if re.search(email_con, user_inp):
    print("Valid Email.")
else:
    print("Invalid email.")