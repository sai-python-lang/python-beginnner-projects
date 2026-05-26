print("welcome to number guessing game 🎮 of pyhton 🐍 ")

import random

# RANDOM module introduces unpredicatbility into programs for efficiency

def play_game():
    secret_number = random.randint(1, 100)
  
  # RANDINT function introduces a random number between the inclusives (upper bound and lower bound)
  
    attempts = 0
  
    print("Guess a number between 1 and 100.😁")
    while True:
        try:
            guess = int(input("Enter guess: "))
            attempts += 1
            if guess < secret_number: print("Too low!")
            elif guess > secret_number: print("Too high!")
            else:
                print(f"Correct! Tries: {attempts}")
                break
        except ValueError: print("Invalid input.")

play_game()
