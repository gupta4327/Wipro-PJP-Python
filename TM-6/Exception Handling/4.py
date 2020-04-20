list1=[1,-3,4,8,-5,-43,5,0]
index = int(input("Enter an index"))
try:
    if list1[index]>0:
        print("Positive")
    elif list1[index]<0:
        print("Negative")
    else:
        print("Number is zero")
except:
    print("Invalid Index !!")
