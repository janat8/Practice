# This is a simple Python calculator that can perform basic arithmetic operations.

def main():
    print("Welcome, this is a Simple Calculator!")

    print("Please enter the first number:")
    x = float(input())

    print("Please enter the second number:")
    y = float(input()) 
   
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = input()

    if operation == '1':
        result = add(x, y)
        print(f"The result of {x} + {y} is: {result}")
    elif operation == '2':
        result = subtract(x, y)
        print(f"The result of {x} - {y} is: {result}")
    elif operation == '3':  
        result = multiply(x, y)
        print(f"The result of {x} * {y} is: {result}")
    elif operation == '4':
        result = divide(x, y)
        print(f"The result of {x} / {y} is: {result}")
    else:
        print("Invalid operation selected. Please choose a valid option.")
              
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
              

main()