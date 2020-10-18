"""
Email Slicer Program
This program separates the username and domain name from the user input
"""
 
# taking input of an Email from the user
email = input("Enter your Email address: ").strip() # removes whitespaces from the input

# try helps in testing for errors  
try:               
    user_name = email[:email.index("@")] # slice out the username
    domain_name = email[email.index("@")+1:] # slice out the domain name
    output = "Your username is '{}' and your domain name is '{}' ".format(user_name,domain_name) # stores data in '{}'
    print("")
    print(output)  
    print("") 

# except helps to handle the error 
except:
    print("")
    print("Invalid Email address!")
    print("")    