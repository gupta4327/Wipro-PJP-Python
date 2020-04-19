def sumList(arr):
    return sum(arr)

list1=[]
n = int(input("Enter no. of elements: "))
for i in range(n):
    list1.append(int(input("Enter number: ")))

print("Sum of list is: ",sumList(list1))    
