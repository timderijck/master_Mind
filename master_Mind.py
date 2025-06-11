#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
import random

print("MasterMind")

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]


def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    se_Co = {}
    gu_Co = {}

    for s, g in zip(secret, guess):
        if s != g:
            se_Co[s] = se_Co.get(s, 0) + 1
            gu_Co[g] = gu_Co.get(g, 0) + 1

    white_Pegs = sum(min(se_Co.get(d, 0), gu_Co.get(d, 0)) for d in gu_Co)

    return black_Pegs, white_Pegs


def show_Secret(mystery):
    print(mystery)


def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1-6. You have tries.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip()
            valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_Guess:
                print("Invalid input. Enter 4 digits, each from 1 to 6.")
            show_Secret(secret_Code) if guess == "cheat" else False

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct): {black}, White pegs (wrong): {white}")

        if black == 4:
            print(f"Congratulations! You win: {''.join(secret_Code)}")
            return

    print(f"You've used all attempts. Right code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()