def func(n1,n2):
    digit1 , digit2 = n1%10,n2%10
    if digit1==digit2:
        return True
    else:
        return False

print("Enter the numbers separated by a space:",end="\n")
n1,n2 = list(map(int,input().split()))
print("True" if func(n1,n2) else "False")
