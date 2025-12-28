import random

print("Hello! Welcome to the Number Guessing Game 🎉")
number = random.randint(1, 100)  # Random number between 1 and 100
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < number:
        print("Go higher!")
    elif guess > number:
        print("Go lower!")
    else:
        print(f"Congratulations! 🎊 You guessed the number {number} in {attempts} attempts!")
        break
