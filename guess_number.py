import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I chose a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too low!")
    elif guess > secret_number:
        print("📈 Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
