#Guess the number randomly chosen by the computer

import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess = int(input("Enter your guess: "))
        if guess < random_number:
            print("Guess higher.")
        elif guess > random_number:
            print("Guess lower.")
    print("Correct guess!!")

guess(100)