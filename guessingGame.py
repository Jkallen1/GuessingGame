import random #import random modules to use in func

def guess(x):
    num = random.randint(1,x) #storing random number computer selects in num
    guess = 0 #setting guess to 0 so it will never equal the random num automatically
    while guess != num: #keeps looping until correct number is guessed
        guess =int(input(f"Enter a number between 1 and {x}: "))
        if guess < num: #statement if num is to low
            print("Sorry, try again. Your guess is too low.")
        elif guess > num: #statement if num is to high
            print("Sorry, try again. Your guess is too high.")
    print(f"Congratulations you have correctly guessed the number {num}") # exits loop and prints this line when correct num guessed


    guess(10)
