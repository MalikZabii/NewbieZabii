import random


def play_game():
    print("Welcome to the number guessing game!!!!!")
    print("Think of a number between 1 and 100.")
    difficulty = input(
        "Choose the difficulty between 'easy' and 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid difficulty choice.")
        return

    secret_number = random.randint(1, 100)

    print(f"You have {attempts} attempts to guess the number.")
    while attempts > 0:
        try:
            guess = int(input("Guess the number: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("That's not a valid number! Please enter an integer.")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print("Sorry, you're out of attempts. The number was", secret_number)


def main():
    while True:
        play_game()
        play_again = input(
            "Do you want to play again? Press 'y' for Yes or 'n' for No: ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
