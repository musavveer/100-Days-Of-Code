# random number guessing game

# random module helps in guessing the hidden number
import random

while True:
    flag = True
    while flag:
        num = input("Enter the number for an upper bound: ")

        # we are using .isdigit to check if the input is integer
        if num.isdigit():
            print("Let's start the game!")
            num = int(num)
            flag = False
        else:
            print("Invalid input! Try again.")    

    # randint helps in generating random number
    memory = random.randint(1,num)
    guess = None
    count = 1

    while guess != memory:
        guess = input("Please enter your guess between 1 and " + str(num) + ": ")        
        if guess.isdigit():
            guess = int(guess)

        if guess == memory:
            print("You're genius!!")

        elif guess>num:
            print("You're going out of the selected range!")

        else:
            print("Oops Wrong guess! Please try again.")
            count += 1

    print("It took you" , count, "guesses!")
    print("Play Again :)")                