d = {}
def printDict():
    for k,v in d.items():
        print(k+":"+v)


for i in range(3):
    name = input("Enter name: ")
    fact = input("Enter fact: ")
    d[name]=fact
printDict()

name = input("Enter new name: ")
fact = input("Enter fact: ")
d[name]=fact
printDict()
name = input("Enter name whose fact is to be changed: ")
fact = input("Enter the new fact: ")
if name in d:
    d[name]=fact
else:
    print("name does not exist")
printDict()
