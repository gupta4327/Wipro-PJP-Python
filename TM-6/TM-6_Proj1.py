name = input("Enter file name: ")
try:
    f1 = open(name)
except:
    print("Error -- File does not exist")
else:
    dis =0
    count=0
    summ=0
    free =0
    final =0
    while(True):
        line = f1.readline()
        if not line:
            break
        if not line.isspace():
            list1 = line.split()
            print(list1)
            if list1[1] == '0' or  list1[1] == "free":
                pass
            elif list1[0] == "discount":
                pass
            else:
                count =count+1
            if list1[1]=='0' or list1[1]=="free":
                free +=1
            if list1[1] != "free" and list1[0]!="discount":
                summ += float(list1[1])
            if list1[0]=="discount":
                dis = int(list1[1])
    final=summ- dis
    print("No. of item Purchased:",count)
    print("No. of free items:",free)
    print("Amount to pay:",summ)
    print("Discount Given:",dis)
    print("Final amount paid:",final)
