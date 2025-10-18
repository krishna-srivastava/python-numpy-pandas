import random

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$*/-+"
password = ""

try:
    n = int(input("Enter the length of the password: "))
    if n <= 0:
        print("Password length must be greater than 0.")
    else:
        for i in range(n):
            password += random.choice(s)
        print("Generated password:", password)
except ValueError:
    print("Invalid length....")
