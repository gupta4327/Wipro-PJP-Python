name = "alex"
count=0
string = input("Enter the string :")
for word in string.lower().split():
    if word==name:
        count+=1

print(count)
