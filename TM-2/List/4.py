list1=[]
count=0
n = int(input("enter number of elements"))
for i in range(n):
    list1.append(input("Enter number"))
print(list1,end="\n")    
x = input("Enter element for count")
for i in list1:
    if i==x:
        count+=1
print(count)
