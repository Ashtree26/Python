import random

def guess(x):
    low = 1
    high = x
    feedback = " "

    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could be high too as low = high
        feedback=input(f"is {guess} too high(h), too low(l), correct(c)??\n")    
        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess+1
    print(f"yay computer guessed {guess} your number correctly.")

guess(100)