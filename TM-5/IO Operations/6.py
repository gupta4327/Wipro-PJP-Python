name = input("enter file name: ")
try:
    f1 = open(name)
except:
    print("file does not exist")
d = {}
for x in f1.read().split():
    d[x]=d.get(x,0)+1

word = input("enter word for the frequency : ")
word = word.lower()
if word in d:
    print(d[word])
else:
    print("word does not exist in file")
f1.close()
