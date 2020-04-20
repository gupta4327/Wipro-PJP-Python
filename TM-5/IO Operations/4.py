lines =[]
name = input("enter file name: ")
try:
    f1 = open(name)
except:
    print("file does not exist")
for i in f1.readlines():
    lines.append(i[:-1])
    # -1 to remove \n

print(lines)
f1.close()
