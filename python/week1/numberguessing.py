import random

n = random.randint(1,100)
a = -1
guess = 0

while a != n:
    try:
        a = int(input("Guess the number: "))
        guess += 1

        if a > n:
            print("Lower number please...")
        elif a < n:
            print("Higher number please...")
            
    except ValueError:
        print("Invalid input! Please enter a valid number.")


print(f"you have guessed the number {n} correctly in {guess} attemps....")