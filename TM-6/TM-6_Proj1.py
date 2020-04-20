name = input("Enter file name: ")
try:
    f1 = open(name)
except:
    print("Error -- File does not exist")
else:
    dis =0
    count=0
    sum=0
    free =0
    final =0
    while(True):
        line = f1.readline()
        if not line:
            break
        if not line.isspace():
            count+=1
            list1 = line.split()
            if list1[1]=='0':
                free +=1
            sum += float(list1[1])
            if list1[0]=="discount":
                dis = int(list1[1])
    final=sum-(sum*(dis/100))
    print("No. of item Purchased:",count)
    print("No. of free items:",free)
    print("Amount to pay:",sum)
    print("Discount Given:",dis)
    print("Final amount paid:",final)
