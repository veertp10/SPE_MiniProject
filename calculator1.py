# Import the math module for mathematical operations
import math

# Function to calculate and return the square root of x
def square_root(x):
    return math.sqrt(x)

# Function to calculate and return the factorial of n using recursion
def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursively calculate factorial

# Function to calculate and return the natural logarithm of x
def natural_log(x):
    return math.log(x)

# Function to calculate and return x raised to the power of b
def power(x, b):
    return math.pow(x, b)

# Main function to provide a menu-driven calculator interface
def main():
    print("Options:")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")

    # Get the user's choice of operation
    option = int(input("Enter your option: "))
    
    # Get the user's input value
    value = float(input("Enter the value: "))

    if option == 1:
        print("Square Root of", value, "is:", square_root(value))
    elif option == 2:
        print("Factorial of", value, "is:", factorial(int(value)))
    elif option == 3:
        print("Natural Logarithm of", value, "is:", natural_log(value))
    elif option == 4:
        # Get the exponent for the power function
        exponent = float(input("Enter the exponent: "))
        print(value, "raised to the power", exponent, "is:", power(value, exponent))
    else:
        print("Invalid option!")

# Call the main function when the script is executed
if __name__ == "__main__":
    main()
