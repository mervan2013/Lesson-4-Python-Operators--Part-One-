import math

def square_root_calculator_math():
    """Calculates the square root of a non-negative number using math.sqrt()."""
    print("Welcome to the Square Root Calculator (using math.sqrt)!")
    while True:
        user_input = input("Enter a non-negative number (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        try:
            number = float(user_input)
            if number < 0:
                print("Error: math.sqrt() cannot handle negative numbers. Please enter a non-negative number.")
                continue
            result = math.sqrt(number)
            print(f"The square root of {number} is {result:.4f}")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# To run the calculator:
# square_root_calculator_math()