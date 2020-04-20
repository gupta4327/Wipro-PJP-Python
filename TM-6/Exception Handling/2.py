try:
    num = int(input("Enter a number:"))
except:
    print("Please enter only an integer")
else:
    flag = True
    for i in range(2,num//2+1):
        if num%i==0:
            flag=False
    if flag==True:
        print("Prime")
    else:
        print("not a prime")             
