list1=[]
n = int(input("enter number of elements: "))
for i in range(n):
    list1.append(input("Enter number: "))
print(list1)
index = int(input("Enter the index of element to be removed :"))
while(True):
    if index<len(list1):
        list1.pop(index)
        print(list1)
        break
    else:
        print("Index does not exist")
        index = int(input("Enter the index of element to beremoved :"))
