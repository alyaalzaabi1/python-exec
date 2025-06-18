import random

best_score = None

def play_game():
    number = random.randint(1, 50)
    guesses = 0

    while True:
        try:
            guess = int(input("Guess the number (1–50): "))
            guesses += 1
            if guess < number:
                print("Higher")
            elif guess > number:
                print("Lower")
            else:
                print(f"Correct! You guessed it in {guesses} tries.")
                return guesses
        except ValueError:
            print("Please enter a valid number.")

while True:
    score = play_game()
    if best_score is None or score < best_score:
        best_score = score
    print(f"Best score so far: {best_score} guesses")
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break
