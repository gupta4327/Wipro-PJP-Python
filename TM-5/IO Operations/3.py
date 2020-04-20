name = input("enter file name: ")
try:
    f1 = open(name,'a')
except:
    print("file does not exist")
string = input("enter strig to append to file\n")
f1.write(string)
f1.close()    
