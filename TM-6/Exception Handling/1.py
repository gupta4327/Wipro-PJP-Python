n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
try:
    div = n1//n2
except:
    print("Error : cannot divide by zero")
else:
    print("Ans:",div)        
