list1=[]
n = int(input("enter number of elements: "))
for i in range(n):
    list1.append(input("Enter number: "))
print(list1)
item = input("Enter the element to be removed :")
while(True):
    if item in list1:
        list1.remove(item)
        print(list1)
        break
    else:
        print("Item does not exist")
        item = input("Enter the element to be removed :")
