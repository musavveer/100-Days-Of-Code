# Random Number Generator For Local Hack Day

# we are importing random and string modules
import random
import string

while True:
    try:
        pwdlen = int(input("Enter the length: "))

        s = string.digits

        # end prints without going to the new line
        print("Your number is: ", end="")

        # sample randomly chooses characters from string 's' of input length 
        print("".join(random.sample(s,pwdlen)))
        print("")
        

    # if the conditions are not met gives an exceptional error statement
    except:
        print("Enter the valid length!!")
        print("")