# Multiply two numbers (integer, decimal, positive or negative)

def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)  # accept all kinds of numbers
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get two numbers from the user
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Multiply
result = num1 * num2

# Show the result
print("\nThe multiplication result =", result)

# Keep the program open until Enter is pressed
input("\nPress Enter to exit...")
