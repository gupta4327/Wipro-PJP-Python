list1=[]
n = int(input("enter number of elements"))
for i in range(n):
    list1.append(int(input("Enter number")))
tup = tuple(list1)
print(tup)

elem = int(input("Enter element to find its index: "))
if elem in tup:
    print(tup.index(elem))
else:
    print("Item does not exist")
