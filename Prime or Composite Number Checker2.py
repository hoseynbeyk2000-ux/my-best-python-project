def check_prime(number):
    """Function to check if a number is prime"""
    if number < 2:
        return "neither prime nor composite"
    elif number == 2:
        return "prime"
    elif number % 2 == 0:
        return "composite"

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return "composite"

    return "prime"


# Get number and display result
number = int(input("Enter a number: "))
result = check_prime(number)
print(f"{number} is {result}")