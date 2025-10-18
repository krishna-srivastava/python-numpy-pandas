import random

while True:
    print("\nDice Roller Menu:")
    print("1. Roll 1 die")
    print("2. Roll 2 dice")
    print("3. Roll 3 dice")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if(choice == 4):
        print("Game over!")
        break
    elif(choice == 1):
        rand1 = random.randint(1,6)
        print(rand1)
    elif(choice == 2):
        rand1 = random.randint(1,6)
        rand2 = random.randint(1,6)
        print(rand1 , rand2)
    elif(choice == 3):
        rand1 = random.randint(1,6)
        rand2 = random.randint(1,6)
        rand3 = random.randint(1,6)
        print(rand1 , rand2 , rand3)
    else:
        print("invalid choice!")
