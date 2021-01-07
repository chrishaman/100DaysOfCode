import random
import os
from hagman_word import word_list
from hagman_art import logo
from hagman_art import stages

# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(logo)
lives = 6
#Testing code
print(f'The solution is {chosen_word}.')

display = []
word = len(chosen_word)
for char in range(word):
    display += "_"
print(f"{' '.join(display)}")

dead = False
while not dead:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    print(logo)
    for letter in range(word):
        letters = chosen_word[letter]
        if letters == guess:
            display[letter] = letters

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            dead = True
            print("You don't have live anymore!")

    print(stages[lives])
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        dead = True
        print("You Win!")


