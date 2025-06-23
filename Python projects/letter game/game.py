import random


words = ["smartphone", "laptop", "ariphone", "window", "fan"]
word = random.choice(words).upper()  

total_chance = 7
guess_word = "-" * len(word)

while total_chance != 0:
    print("Word:", guess_word)
    letter = input("Guess a Letter: ").upper()

    if letter in word:
        new_guess = list(guess_word)
        for index in range(len(word)):
            if word[index] == letter:
                new_guess[index] = letter
        guess_word = ''.join(new_guess)

        if guess_word == word:
            print("You won!!")
            print("The word was:", word)
            break
    else:
        total_chance -= 1
        print("Wrong answer!")
        print("Remaining chances:", total_chance)

if guess_word != word:
    print("Game over!")
    print("You lost the game.")
    print("The correct word was:", word)
