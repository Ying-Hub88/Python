#!/usr/bin/env python3.10

# User guess a number in random number between 1 and 99

import random

small_num, big_num, random_num = None, None, None
playing = True

# Use function to replace the repeat code
def reset_game():
    global small_num, big_num, random_num
    small_num, big_num = 1, 99
    random_num = random.randint(small_num, big_num)

reset_game()

while playing:
    guess_num = None
    prompt = f"Guess a number from {small_num} to {big_num}: "

# Change the while loop conditions based on the game progress
    while guess_num is None or guess_num < small_num or guess_num > big_num:
        temp_num = input(prompt)
        prompt = f"Ooops! A number from {small_num} to {big_num} please: "
        if temp_num.isdigit():
            guess_num = int(temp_num)

    if guess_num > random_num:
        print("The number is lower than", guess_num)
        big_num = guess_num
    elif guess_num < random_num:
        print("The number is higher than", guess_num)
        small_num = guess_num
    elif guess_num == random_num:
        print("Congratulation! You got the number: ", guess_num)

        again = input("Do you want to play again? Enter Y to continue ")
        if again.lower() == 'y':
            reset_game()

        else:
            print("Game Over! See you!")
            playing = False
