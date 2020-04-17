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
n = int(input("Enter a number: "))
print("Prime Number" if isPrime(n) else "Not a Prime Number")
