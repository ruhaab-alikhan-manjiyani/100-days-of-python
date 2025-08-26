import random
print("🎮 Welcome to the Number Guessing Game!")
while True:
    level = input("\nChoose difficulty level - Easy, Medium, Hard: ").lower()
    if level == "easy":
        secret = random.randint(1, 10)
        max_range = 10
    elif level == "medium":
        secret = random.randint(1, 20)
        max_range = 20
    elif level == "hard":
        secret = random.randint(1, 50)
        max_range = 50
    else:
        print("Invalid choice! Defaulting to Medium level.")
        secret = random.randint(1, 20)
        max_range = 20
    attempts = 0
    max_attempts = 5
    guess = None
    print(f"\nI have selected a number between 1 and {max_range}. You have {max_attempts} attempts to guess it.")
    while attempts < max_attempts and guess != secret:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            if guess < 1 or guess > max_range:
                print(f"Please guess a number within the range 1 to {max_range}.")
                continue
            attempts += 1
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You've guessed the number {secret} correctly in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    if guess != secret:
        print(f"\nSorry, you've used all your attempts. The correct number was {secret}. Better luck next time!")
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thank you for playing! Goodbye!")
        break