# Enhanced version with error handling
def enhanced_prime_checker():
    """Enhanced prime checker with error handling"""
    try:
        # Get input from user
        number = int(input("Enter a positive integer: "))

        # Validate input
        if number < 0:
            print("Please enter a non-negative number")
            return

        # Check special cases
        if number < 2:
            print(f"{number} is neither prime nor composite")
            return

        # Check for 2
        if number == 2:
            print(f"{number} is a prime number")
            return

        # Check even numbers
        if number % 2 == 0:
            print(f"{number} is a composite number")
            return

        # Check odd numbers
        is_prime = True
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break

        # Display result
        if is_prime:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is a composite number")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# Run the program
enhanced_prime_checker()