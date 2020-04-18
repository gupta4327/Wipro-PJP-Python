list1=[]
list2=[]
n = int(input("enter number of elements for list1 : "))
for i in range(n):
    list1.append(input("Enter items"))
n = int(input("enter number of elements for list2 : "))
for i in range(n):
    list1.append(input("Enter items"))
print("Appended list is", )
list1.extend(list2)
for i in list1:
    print(i,end=" ")
