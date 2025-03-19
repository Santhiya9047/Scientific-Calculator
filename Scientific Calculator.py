import math

# Function for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function for scientific operations
def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return math.factorial(x)

# Main calculator function
def scientific_calculator():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm (base 10)")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")

    while True:
        try:
            choice = input("\nEnter choice (1-11) or 'exit' to quit: ")

            if choice == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
                num1 = float(input("Enter first number: "))

                if choice in ['1', '2', '3', '4', '5']:
                    num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")
                elif choice == '6':
                    print(f"Square root of {num1} = {square_root(num1)}")
                elif choice == '7':
                    print(f"Log of {num1} = {log(num1)}")
                elif choice == '8':
                    print(f"Sine of {num1} = {sine(num1)}")
                elif choice == '9':
                    print(f"Cosine of {num1} = {cosine(num1)}")
                elif choice == '10':
                    print(f"Tangent of {num1} = {tangent(num1)}")
                elif choice == '11':
                    print(f"Factorial of {int(num1)} = {factorial(int(num1))}")

            else:
                print("Invalid input. Please enter a valid choice.")
        except ValueError:
            print("Invalid input! Please enter numerical values.")

# Run the calculator
if __name__ == "__main__":
    scientific_calculator()