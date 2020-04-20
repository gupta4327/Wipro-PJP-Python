name = input("enter file name: ")
try:
    f1 = open(name)
except:
    print("file does not exist")
n = int(input("enter no. of lines to read"))
for _ in range(n):
    print(f1.readline())
f1.close()
