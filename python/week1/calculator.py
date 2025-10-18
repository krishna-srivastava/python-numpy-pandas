import math

def menu():
    print('''\nAdvanced Calculator:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Power
    6. Modulus
    7. Square Root
    8. Logarithm
    9. Trigonometry (sin, cos, tan)
    10. Factorial
    11. Exit''')

def add(a, b): return a + b
def subs(a, b): return a - b
def mult(a, b): return a * b

def div(a, b):
    if (b != 0):
        return a / b 
    else: "Error: Division by zero"

def power(a, b): return a ** b
def mod(a, b): return a % b

def square_root(a): return math.sqrt(a)
def log(a): return math.log10(a)

def trig(func, angle_deg):
    angle_rad = math.radians(angle_deg)
    if func == 'sin':
        return math.sin(angle_rad)
    elif func == 'cos':
        return math.cos(angle_rad)
    elif func == 'tan':
        return math.tan(angle_rad)
    
def fact(n): return math.factorial(n)

while True:
    menu()
    try:
        choice = int(input("Enter your choice (1-11): "))
        if choice == 11:
            print("Thank you for using the calculator!")
            break

        if choice in [1, 2, 3, 4, 5, 6]:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subs(num1, num2))
            elif choice == 3:
                print("Result:", mult(num1, num2))
            elif choice == 4:
                print("Result:", div(num1, num2))
            elif choice == 5:
                print("Result:", power(num1, num2))
            elif choice == 6:
                print("Result:", mod(num1, num2))

        # For single-input operations
        elif choice == 7:
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot take square root of a negative number.")
            else:
                print("Result:", square_root(num))

        elif choice == 8:
            num = float(input("Enter number: "))
            if num <= 0:
                print("Error: Logarithm undefined for zero or negative numbers.")
            else:
                print("Result:", log(num))

        elif choice == 9:
            angle = float(input("Enter angle in degrees: "))
            print("sin =", trig('sin', angle))
            print("cos =", trig('cos', angle))
            print("tan =", trig('tan', angle))

        elif choice == 10:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Error: Factorial of negative number not defined.")
            else:
                print("Result:", fact(num))
        else:
            print("Invalid choice! Please select between 1 and 11.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print("Error:", e)
