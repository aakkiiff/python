print("welcome to the bill splitting calculator")
bill =int(input("how much you guys need to  pay\n"))
people=int(input("how many guys are you?\n"))
vat=int(input("how much is vat?"))

net=(bill+(bill*vat)/100)/people
print(f"per person will be paying: {net}$")
