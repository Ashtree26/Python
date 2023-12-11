import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print(f"Sorry, wrong guess. You are too low.")
        elif guess > random_num:
            print(f"Sorry, wrong guess. You are too high.")
    print(f"yay! You guessed {random_num} correctly!")

guess(20)