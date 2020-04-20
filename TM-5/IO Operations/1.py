name = input("enter file name: ")
try:
    f1 = open(name)
except:
    print("file does not exist")
print(f1.read())
f1.close()
