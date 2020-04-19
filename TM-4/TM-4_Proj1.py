from sys import argv
good = list(map(int,argv[1].split("-")))
bad = list(map(int,argv[2].split("-")))
list1 = list(map(int,argv[3].split("-")))
happyness = 0
for i in list1:
    if i in good:
        happyness+=1
    elif i in bad:
        happyness-=1

print("happyness:",happyness)
