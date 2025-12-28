# Prime or Composite Number Checker in Python

# Get number from user
number = int(input("Enter a number: "))

# Condition 1: Check if number is less than 2
if number < 2:
    print(f"{number} is neither prime nor composite")
# Condition 2: Check if number is exactly 2
elif number == 2:
    print(f"{number} is a prime number")
# Condition 3: Check if number is even
elif number % 2 == 0:
    print(f"{number} is a composite number")
else:
    # Check odd numbers greater than 2
    is_prime = True  # Assume number is prime

    # Use for loop to check divisibility
    for i in range(3, int(number ** 0.5) + 1, 2):
        # Condition: If number is divisible by i
        if number % i == 0:
            is_prime = False
            break

    # Condition: Display final result
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a composite number")