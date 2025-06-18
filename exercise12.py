import random

secret = random.randint(1, 100)
guess = None

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    if guess < secret:
        print("Higher")
    elif guess > secret:
        print("Lower")
    else:
        print("Correct! You guessed it.")
