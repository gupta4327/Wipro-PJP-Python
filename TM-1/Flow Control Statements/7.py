def isPrime(num):
    if num>1:
        if num==2 or num==3:
            return True
        for i in range(2,num//2+1):
            if num%i==0:
                return False
        return True
    else:
        return False

a=10
b=99
for x in range(a,b):
    if isPrime(x):
        print(x,end=" ")
