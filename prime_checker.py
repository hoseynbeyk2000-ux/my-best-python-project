# Prime Number Checker with File Save to D:
# This program meets ALL your requirements:
# 1. Takes input number
# 2. Checks prime/composite
# 3. Uses IF conditions
# 4. Saves to D: drive

print("=" * 50)
print("PRIME NUMBER DETECTOR")
print("=" * 50)

# --- REQUIREMENT 1: INPUT FROM USER ---
user_input = input("Please enter a number: ")

# Check if input is valid integer
if not user_input.isdigit():
    print("ERROR: Please enter a positive integer!")
    exit()

number = int(user_input)

print("-" * 50)

# --- REQUIREMENT 2 & 3: CHECK PRIME WITH IF CONDITIONS ---
result = ""

# CONDITION 1: Check for numbers less than 2
if number < 2:
    result = "NOT PRIME"
    print(f"Number {number} is NOT PRIME (less than 2)")

# CONDITION 2: Check if number is 2
elif number == 2:
    result = "PRIME"
    print(f"Number {number} is PRIME")

# CONDITION 3: Check if even number
elif number % 2 == 0:
    result = "COMPOSITE"
    print(f"Number {number} is COMPOSITE (even number)")

# CONDITION 4: Check odd numbers
else:
    is_prime = True

    # Check divisors from 3 to sqrt(number)
    for i in range(3, int(number ** 0.5) + 1, 2):
        # CONDITION: Check divisibility
        if number % i == 0:
            is_prime = False
            result = "COMPOSITE"
            print(f"Number {number} is COMPOSITE (divisible by {i})")
            break

    # FINAL CONDITION: If no divisor found
    if is_prime:
        result = "PRIME"
        print(f"Number {number} is PRIME")

print("=" * 50)

# --- REQUIREMENT 4: SAVE TO D: DRIVE ---
print("\nSaving results to D: drive...")

# Create file path for D: drive
file_path = "D:/prime_number_results.txt"

try:
    # Open file for writing
    with open(file_path, "w") as file:
        # Write header
        file.write("PRIME NUMBER CHECK RESULTS\n")
        file.write("=" * 40 + "\n")

        # Write input number
        file.write(f"Input Number: {number}\n")

        # Write result
        file.write(f"Result: {result}\n")

        # Write conditions checked
        file.write("\nConditions Checked:\n")
        file.write("-" * 20 + "\n")

        if number < 2:
            file.write("1. Number < 2 → NOT PRIME\n")
        elif number == 2:
            file.write("1. Number == 2 → PRIME\n")
        elif number % 2 == 0:
            file.write("1. Number is even → COMPOSITE\n")
        else:
            file.write(f"1. Number is odd\n")
            file.write(f"2. Checked divisors up to {int(number ** 0.5)}\n")
            file.write(f"3. No divisors found → PRIME\n" if result == "PRIME"
                       else f"3. Divisor found → COMPOSITE\n")

        file.write("\n" + "=" * 40 + "\n")
        file.write("End of Report\n")

    print("✓ SUCCESS: File saved to D: drive!")
    print(f"📁 Location: {file_path}")

    # Show what was saved
    print("\n📄 File Contents:")
    print("-" * 30)
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())

except Exception as e:
    print(f"✗ ERROR: Could not save to D: drive")
    print(f"Error details: {e}")

    # Try alternative location
    print("\nTrying to save to Desktop...")
    import os

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "prime_results.txt")

    try:
        with open(desktop_path, "w") as file:
            file.write(f"Number: {number}, Result: {result}")
        print(f"✓ Saved to Desktop: {desktop_path}")
    except:
        print("✗ Could not save anywhere!")

print("\n" + "=" * 50)
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("=" * 50)

# Keep window open
input("\nPress Enter to exit...")