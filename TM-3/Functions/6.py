def isPrime(n):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

n = int(input("Enter a number: "))
print("Prime" if isPrime(n) else "Not a Prime")
