d = {}
def UserInput():
    name = input("Enter Name: ")
    math = int(input("Enter marks in Maths: "))
    phy = int(input("Enter marks in Physics: "))
    chem = int(input("Enter marks in Chemistry: "))
    d[name]=[math,phy,chem]
    return

UserInput()
print("Enter Y if you want to add more records")
while(True):
    UserInput()
    temp =input("Enter Y if you want to add more records")
    if temp != "Y":
        break
name1 = input("Enter name :")
if name1 in d:
    print("Average percentage mark: ",sum(d[name1])/3)
