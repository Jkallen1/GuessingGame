import random

def guess(x):
    num = random.randint(1,x)
    guess = 0
    while guess != num:
        guess =int(input(f"Enter a number between 1 and {x}: "))
        if guess < num:
            print("Sorry, try again. Your guess is too low.")
        elif guess > num:
            print("Sorry, try again. Your guess is too high.")
    print(f"Congratulations you have correctly guessed the number {num}")


    guess(10)
