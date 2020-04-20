def time(f1):
    count=0
    while(f1.readline()):
        count+=1
    if count<=12:
        return str(count)+" AM"
    else:
        return str(count-12)+" PM"
    f1.close()

def place():
    f1=open(name)
    d={}
    data = f1.read()
    for i in data.split():
        d[i]=d.get(i,0)+1
    print(d)
    m = 0
    place = ""
    for k,v in d.items():
        if v>m:
            m=v
            place = k
    return (place+" Street")
    f1.close()

name = input("enter file name: ")
try:
    f1 = open(name)
except:
    print("file does not exist")

print("Meeting Time: ",time(f1))
print("Meeting Place: ",place())
