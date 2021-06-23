print("welcome to the bill splitting calculator")
bill =int(input("how much you guys need to  pay\n"))
people=int(input("how many guys are you?\n"))
vat=int(input("how much is vat?\n"))
name=[]
thedic={}
for i in range(people):
    a=input(f"type the name of person number {i+1} ?")
    name.append(a)

i=0
for p in name:
    a=input(f"how much {name[i]} spent?\n")
    thedic[name[i]]=int(a)
    i+=1
#perperson will be paying?
for o,i in thedic.items():
    print(f'{o} will be paying {i+(i*vat)/100}$')


