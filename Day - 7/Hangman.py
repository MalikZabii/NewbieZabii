import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for _ in chosen_word]

stages = [
    """
      -----
      |   |
      |   O
      |  /|\
      |  / \
      |
    --------
    """,
    """
      -----
      |   |
      |   O
      |  /|\
      |  /
      |
    --------
    """,
    """
      -----
      |   |
      |   O
      |  /|\
      |
      |
    --------
    """,
    """
      -----
      |   |
      |   O
      |  /|
      |
      |
    --------
    """,
    """
      -----
      |   |
      |   O
      |   |
      |
      |
    --------
    """,
    """
      -----
      |   |
      |   O
      |
      |
      |
    --------
    """,
    """
      -----
      |   |
      |
      |
      |
      |
    --------
    """
]

lives = len(stages) - 1

print(" ".join(display))

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1

    print(" ".join(display))
    print(stages[len(stages) - 1 - lives])

if "_" not in display:
    print("Congratulations! You've guessed the word:", chosen_word)
else:
    print("Sorry, you've run out of lives. The word was:", chosen_word)
