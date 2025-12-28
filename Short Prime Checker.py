# Short Prime Checker with D: drive save

# Get number
num = int(input("Enter number: "))

# Check prime with IF conditions
if num < 2:
    res = "NOT PRIME"
elif num == 2:
    res = "PRIME"
elif num % 2 == 0:
    res = "COMPOSITE"
else:
    prime = True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            prime = False
            break
    res = "PRIME" if prime else "COMPOSITE"

print(f"Result: {res}")

# Save to D: drive
with open("D:/result.txt", "w") as f:
    f.write(f"Number: {num}\nResult: {res}")
print("Saved to D:/result.txt")