d = {}
v = input("Enter value :")
k = input("Enter Key :")
d[v]=k
print(d)
while(True):
    temp = input("Press X to exit any other key to continue adding: ")
    if temp=="X":
        break
    v = input("Enter value :")
    k = input("Enter Key :")
    d[v]=k
    print(d)
