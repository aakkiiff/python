import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password??\n"))
nr_symbols = int(input(f"How many symbols would you like in your password??\n"))
platform = input("for which platform are you using this password my boy?\n")


def gene8(number,section):
#numnber is how many of number/letter/symbol you want ,section is is it nember/symbol/letter section?
    pas=""
#pas is the var which will ultimetly hold raw password ,will will later be randomized
    for i in range(0,number):
        randomindex = random.randint(0,len(section)-1)
        generated_later=section[randomindex]
        pas = pas + generated_later
    return (pas)
pas=(gene8(number=nr_letters,section=letters))
pas+=gene8(number=nr_numbers,section=numbers)
pas+=gene8(number=nr_symbols,section=symbols)

#shuffling the raw password
pas=list(pas)
random.shuffle(pas)
pas = ''.join(map(str, pas))
print(f"Here's the Password {pas}")

#encryption
text = pas
shift = int(input("Type Your Secret Shift Code\n"))
shift = shift % 52

def caesar(start_text,shift_amount):
    end_text=""
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the Encrypted Password: {end_text}")
    print(f"This Encrypted Password Will Be Saved In secret.txt")
    a=end_text
    return (a)

koko=caesar(start_text=text, shift_amount=shift)


file=open("secret.txt","a")
file.write(f"{platform} : {koko}\n")
file.close()
