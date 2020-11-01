
with open('rates.txt') as f:
    lines = f.readlines()

ratesDict = {}
for line in lines:
    parsed = line.split("\t")  
    ratesDict[parsed[0]] = parsed[1]

amount = int(input("Enter Amount: \n"))
print("Enter the name of currency you want to convert: \n")
[print(item) for item in ratesDict.keys()]
currency = input("Please enter one of the above values: \n")
print(f"{amount} INR is equal to {amount * float(ratesDict[currency])} {currency}")
