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


#function to have computer guess your secret number

def computer_guess(x):
    low = 1 #setting the lowest option to guess
    high = x #setting high point
    feedback = "" 
    while feedback != "c": #looping through feedback empty string
        if low != high: #makes sure low and high are not equal
            guess = random.randint(low, high) #has the computer guess a random number
        else:
            guess = high
        feedback = input(f"Is {guess} to high (H), to low (L), or correct (C)").lower() #gets user input to manually tell the computer if too high or low
        if feedback == 'h':
            high = guess - 1 #changes the high minus one to know to stay under that number 
        elif feedback == 'l':
            low = guess + 1 #changes the low plus one to know to stay above that number
    print(f"Congrats!! The computer guessed your number, {guess}, correctly!") #prints when correctly guessed



computer_guess(1000)
