# Rock Paper or Scissors game

# we are using random module
import random

# initially the score is zero 
comp_wins = 0
player_wins = 0

# defining a function for user
def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")

    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "p"    
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "s"  
    else:
        print("Error!! Try Again!")
        Choose_Option()
    return user_choice  

# defining a function for computer 
# random.radint randomly chooses r,p,s
def Computer_Option():
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"    
    else:
        comp_choice = "s"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("") 

    # we are incrementing to store the score
    if user_choice == "r":
        if comp_choice == "r":
            print("You choose Rock. The Computer choose Rock. You tied!")
        elif comp_choice == "p":
            print("You choose Rock. The Computer choose Paper. You lose!")
            comp_wins += 1
        elif comp_choice == "s":
            print("You choose Rock. The Computer choose Scissors. You win!")
            player_wins += 1    

    elif user_choice == "p":
        if comp_choice == "r":
            print("You choose Paper. The Computer choose Rock. You win!")
            player_wins += 1
        elif comp_choice == "p":
            print("You choose Paper. The Computer choose Paper. You tied!") 
        elif comp_choice == "s":
            print("You choose Paper. The Computer choose Scissors. You lose!")
            comp_wins += 1          
                     
    elif user_choice == "s":
        if comp_choice == "r":
            print("You choose Scissors. The Computer choose Rock. You lose!")
            comp_wins += 1
        elif comp_choice == "p":
            print("You choose Scissors. The Computer choose Paper. You win!")
            player_wins += 1   
        elif comp_choice == "s":
            print("You choose Scissors. The Computer choose Scissors. You tied!")                 

    # score is displayed
    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("--------------------")