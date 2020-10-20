# Random Password generator program

# we are importing random and string modules
import random
import string

while True:
    try:
        pwdlen = int(input("Enter the length: "))

        # gets all the letters, digits, punctuation from string module 
        s1 = string.ascii_letters
        s2 = string.digits
        s3 = string.punctuation

        # we are creating a blank string 's'
        s = []

        # extend adds s1,s2,s3 to 's'
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))

        # end prints without going to the new line
        print("Your password is: ", end="")

        # sample randomly chooses characters from string 's' of input length 
        print("".join(random.sample(s,pwdlen)))
        print("")
        break

    # if the conditions are not met gives an exceptional error statement
    except:
        print("Enter the valid length!!")
        print("")