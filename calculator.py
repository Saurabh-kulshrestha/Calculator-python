from art import logo  # Import the logo from art.py
from decimal import Decimal
# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def sub(a, b):
    return a - b

# Function for multiplication
def mul(a, b):
    return a * b

# Function for division with error handling
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def get_valid_operation():
    # Allowed operations
    valid_operations = ['+', '-', '*', '/']
    
    while True:
        # User input for the operation
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Check if the input is exactly one of the valid operations
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation! Please enter one of the following: +, -, *, /")

# Main calculator function
def calculator():
    print("\n" * 100)  # Add some space after the logo for cleaner display
    print(logo)  # Display the calculator logo

    # Dictionary storing operations
    operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div,
    }

    # Variable to control the loop
    should_accumulate = True

    # Taking the first input from the user
    num_1 = Decimal(input("Enter the first number:  "))

    while should_accumulate:  # Loop for continuous calculations
        # User picks an operation
        operation_symbol = get_valid_operation()

        # Taking the second input from the user
        num_2 = Decimal(input("What's the next number:  "))

        # Get the result of the operation
        result = operations[operation_symbol](num_1, num_2)

        # Print the result of the calculation
        print("\n"*100)
        print(f"{num_1} {operation_symbol} {num_2} = {result}")

        # Ask the user if they want to continue with the result
        user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ").lower()

        if user_choice == "y":
            num_1 = result  # Continue calculation with the current result
        elif user_choice == "n":
            calculator()  # Restart the calculator from the beginning

# Start the calculator
calculator()