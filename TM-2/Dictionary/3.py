d = {}
v = input("Enter value :")
k = input("Enter Key :")
d[v]=k
while(True):
    temp = input("Press X to exit any other key to continue adding: ")
    if temp=="X":
        break
    v = input("Enter value :")
    k = input("Enter Key :")
    d[v]=k
print(d)
name = input("Enter the key to be searched: ")
if name in d:
    print(name,"exists in the dictioary")
else:
    print(name,"does not exists in the dictioary")        
