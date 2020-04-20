name = input("Please enter a file name: ")
try:
    f1 = open(name,'r')
except:
    print("Error :file does not exist")
else:
    data = f1.read()
    print(data.title())    
