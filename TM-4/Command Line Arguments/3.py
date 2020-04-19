from sys import argv

def isPrime(n):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    else:
        for x in range(2,n//2+1):
            if n%x==0:
                return False
        return True
sum =0
for i in argv[1:]:
    if isPrime(int(i)):
        sum+=int(i)

print("Sum of prime numbers :",sum)
