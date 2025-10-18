import random

# snake : 1, water : -1, gun: = 0
yourdict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reversedict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

while True:
    yourchoice = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    if yourchoice in yourdict:
        break
    else:
        print("Invalid input! Please enter 's', 'w', or 'g'.")

you = yourdict[yourchoice]
computerchoice = random.choice([1, 0, -1])

print(f"You chose {reversedict[you]} and computer chose {reversedict[computerchoice]}")

if you == computerchoice:
    print("Draw!")
elif (you == 1 and computerchoice == -1) or \
     (you == 0 and computerchoice == 1) or \
     (you == -1 and computerchoice == 0):
    print("You win!")
else:
    print("You lose!")
