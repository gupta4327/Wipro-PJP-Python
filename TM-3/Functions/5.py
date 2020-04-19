def even(arr):
    temp=[]
    for x in arr:
        if x%2==0:
            temp.append(x)
    return temp        

list1 =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Existing List: ",list1)
print("Even elements of list are:",even(list1))
