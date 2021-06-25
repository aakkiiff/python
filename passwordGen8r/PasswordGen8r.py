import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
platform = input("for which platform are you using this password my boy?\n")
p=''
for i in range(0,nr_letters):
  a=random.randint(1,26)
  l=(letters[a])
  p=p+l

for i in range(0,nr_symbols):
  a=random.randint(1,8)
  l=(symbols[a])
  p=p+l

for i in range(0,nr_numbers):
  a=random.randint(1,9)
  p=p+str(a)

p=list(p)
random.shuffle(p)

password = ''.join(map(str, p))

print(password)

file=open("secret.txt","a")
file.write(f"{platform} : {password}\n")
file.close()
